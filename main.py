import re
from violations_ds import violations

"""
        0        1         2        3      4      5       6        7         8           9
    <seqname> <source> <feature> <start> <end> <score> <strand> <frame> [attributes] [comments] 
"""

def write_report():
    n_issues = 0
    file_out = open("report.txt", "w")
    file_out.write("#\tRecord\tProblem\n")

    for key in violations:
        if type(violations[key]["value"]) == bool: 
            if violations[key]["value"]:
                n_issues += 1
                file_out.write(str(n_issues) + "\t" + "/" + "\t\t" + violations[key]["msg"] + "\n")
        else:
            for row in violations[key]["value"]:
                n_issues += 1
                file_out.write(str(n_issues) + "\t" + str(row + 1) + "\t\t" + violations[key]["msg"] + "\n")
        
def is_field_valid(field, allowed_values):
    return True if field in allowed_values else False

def parse_attributes(field):
    return re.findall(r"(\s?\w+) ((?:(?:\"[^\"]*\")|(?:[0-9]+)|(?:[^\s;]+[\s;]));?)", field)

start_codon_bp, stop_codon_bp = 0, 0
prev_source = ""
lines = []

# Read File
print("Input File: samples/", end="")
file_name = input()
with open("./samples/" + file_name, "r") as input_file:
    lines = input_file.readlines()

for index, line in enumerate(lines):
    # Ignore if whole line is a comment
    if line[0] == "#":
        continue

    # Ignore characters after "#" (comments)
    record = (re.sub("#.*", "", line)).split("\t")

    # Record fields number check 
    if (len(record) < 9):
        violations["invalid_fields_number"]["value"].append(index)
        continue

    # source check
    # 2nd field (index 1)
    # source must be unique in the file
    if prev_source != "" and prev_source != record[1]:
        violations["source_not_unique"]["value"] = True
    
    prev_source = record[1]

    # feature check
    # 3rd field (index 2)
    # Allowed values: {"CDS", "start_codon", "stop_codon", "5UTR", "3UTR", "inter", "inter_CNS", "intron_CNS", "exon"}
    # Line is ignored whether value is not allowed
    if not is_field_valid(record[2], {"CDS", "start_codon", "stop_codon", 
        "5UTR", "3UTR", "inter", "inter_CNS", "intron_CNS", "exon"}):
        continue

    # CDS feature check
    # A "CDS" record is required
    if record[2] == "CDS":
        violations["missing_cds"]["value"] = False

    # start_codon feature check
    # A "start_codon" record is required
    if record[2] == "start_codon":
        violations["missing_start_codon"]["value"] = False
        try:     
            start_codon_bp += int(record[4]) - int(record[3]) + 1       
        except:
            # In case of non-numeric values, violation will be noticed later
            pass

    # stop_codon feature check
    # A "stop_codon" record is required
    if record[2] == "stop_codon":
        violations["missing_stop_codon"]["value"] = False
        try:
            stop_codon_bp += int(record[4]) - int(record[3]) + 1   
        except:
            pass

    # start and end check
    # 4th field (index 3) and 5th field (index 4) respectively
    # start must be less than or equal to stop
    # in "start_codon" and "stop_codon" records, if they're contiguous frame must be 0
    valid_start_stop = True
    if not (record[3].isdigit() and int(record[3]) >= 1):
        violations["start_not_valid"]["value"].append(index)
        valid_start_stop = False

    if not (record[4].isdigit() and int(record[4]) >= 1):
        violations["end_not_valid"]["value"].append(index)
        valid_start_stop = False

    if valid_start_stop:
        if int(record[3]) > int(record[4]):
            violations["start_greater_than_end"]["value"].append(index)
        elif int(record[4]) - int(record[3]) == 2:
            if record[2] == "start_codon" and record[7] != "0":
                violations["invalid_frame_contig_start_codon"]["value"].append(index)
            elif record[2] == "stop_codon" and record[7] != "0":
                violations["invalid_frame_contig_stop_codon"]["value"].append(index)

    # score check
    # 6th field (index 5)
    # It must be an Integer or Floating Point value. "." allowed too
    if not (record[5] == "." or record[5].isnumeric()):
        violations["score_invalid"]["value"].append(index)

    # strand check
    # 7th field (index 6)
    # Allowed value: {+, -}
    if not is_field_valid(record[6], {"+", "-"}):
        violations["strand_invalid"]["value"].append(index) 

    # frame check
    # 8th field (index 7)
    # Generic record allowed values: {0, 1, 2, .}
    # "start_codon" or "stop_codon" feature allowed values: {0, 1, 2}
    if not is_field_valid(record[7], {"0", "1", "2", "."}):
        violations["frame_invalid"]["value"].append(index)
    else:
        if record[2] == "start_codon" and not is_field_valid(record[7], {"0", "1", "2"}):
            violations["start_codon_invalid_frame"]["value"].append(index)
        elif record[2] == "stop_codon"and not is_field_valid(record[7], {"0", "1", "2"}):
            violations["stop_codon_invalid_frame"]["value"].append(index)

    # attributes check
    # 9th field (index 8)
    # Every record must have gene_id and transcript_id attributes
    # Any other attribute must apper after these two
    # Every attribute must end in a semicolon and be separated from the next one by exactly one space
    found_gene_id, found_transcript_id = False, False
    for j, attribute in enumerate(parse_attributes(record[8])):
        if attribute[1][-1] != ";" or (j > 0 and not (attribute[0][0] == " " and attribute[0][1] != " ")):
            violations["invalid_attributes_separator"]["value"].append(index)

        attr_value = attribute[1].replace(";", "")

        if "gene_id" in attribute[0]:
            found_gene_id = True
        elif "transcript_id" in attribute[0]:
            found_transcript_id = True
            if record[2] == "inter" and attr_value != "\"\"":
                violations["inter_trascript_id_not_empty"]["value"].append(index)
            elif record[2] == "inter_CNS" and attr_value != "\"\"":
                violations["inter_CNS_trascript_id_not_empty"]["value"].append(index)
            elif record[2] == "intron_CNS" and attr_value == "\"\"":
                violations["intron_CNS_trascript_id_empty"]["value"].append(index)
        elif not found_gene_id or not found_transcript_id:
            violations["invalid_attributes_order"]["value"].append(index)

        if re.search(r"(?:\"[^\"]*\")|(?:[0-9]+)", attr_value) == None:
            violations["text_attribute_not_doublequotes"]["value"].append(index)

    if not found_gene_id:
        violations["missing_gene_id"]["value"].append(index)

    if not found_transcript_id:
        violations["missing_transcript_id"]["value"].append(index)

# start_codon and stop_codon are not necessarily atomic, but their total lenght must be less than or equal to 3
if start_codon_bp > 3:
    violations["start_codon_more_than_3"]["value"] = True
if stop_codon_bp > 3:
    violations["stop_codon_more_than_3"]["value"] = True

write_report()
print("report.txt successfully generated")