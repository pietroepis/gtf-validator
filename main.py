import re

"""
        0        1         2        3      4      5       6        7         8           9
    <seqname> <source> <feature> <start> <end> <score> <strand> <frame> [attributes] [comments] 
"""

def is_field_valid(field, allowed_values):
    return True if field in allowed_values else False

def parse_attributes(field):
    re.findall(r"([\w\s]+) (\"[^\"]+\"|[0-9]+)", field)

file_name = "./samples/file-1.gtf"
lines = []
violations = {
    "missing_cds": True,
    "missing_start_codon": True,
    "missing_stop_codon": True,
    "start_codon_more_than_3": False,
    "stop_codon_more_than_3": False,
    "invalid_fields_number": [],
    "start_codon_invalid_frame": [],
    "stop_codon_invalid_frame": [],
    "inter_trascript_id_not_empty": [],
    "inter_CNS_trascript_id_not_empty": [],
    "intron_CNS_trascript_id_empty": [],
    "start_not_valid": [],
    "stop_not_valid": [],
    "start_greater_than_end": [],
    "score_invalid": [],
    "strand_invalid": [],
    "frame_invalid": [],
    "missing_gene_id": [],
    "missing_transcript_id": [],
    "invalid_attributes_order": [],
    "invalid_attributes_separator": [],
    "text_attribute_not_doublequotes": []
}

with open(file_name, "r") as input_file:
    lines = input_file.readlines()

#for index, line in enumerate(lines):
for index in range(0, 20): 
    line = lines[index]
    # Ignore if whole line is a comment
    if line[0] == "#":
        continue

    # Ignore characters after "#" (comments)
    record = (re.sub("#.*", "", line)).split("\t")

    # Record fields number check 
    if (len(record) < 9):
        violations["invalid_fields_number"].append(index)
        continue

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
        violations["missing_cds"] = False

    # start_codon feature check
    # A "start_codon" record is required
    if record[2] == "start_codon":
        violations["missing_start_codon"] = False            

    # stop_codon feature check
    # A "stop_codon" record is required
    if record[2] == "stop_codon":
        violations["missing_stop_codon"] = False
            
    # start and stop check
    # 4th field (index 3) and 5th field (index 4) respectively
    # start must be less than or equal to stop
    valid_start_stop = True
    if not (record[3].isdigit() and int(record[3]) >= 1):
        violations["start_not_valid"].append(index)
        valid_start_stop = False

    if not (record[4].isdigit() and int(record[4]) >= 1):
        violations["stop_not_valid"].append(index)
        valid_start_stop = False

    if (valid_start_stop and record[3] > record[4]):
        violations["start_greater_than_end"].append(index)

    # score check
    # 6th field (index 5)
    # It must be an Integer or Floating Point value. "." allowed too
    if not (record[5] == "." or record[5].isnumeric()):
        violations["score_invalid"].append(index)

    # strand check
    # 7th field (index 6)
    # Allowed value: {+, -}
    if not is_field_valid(record[6], {"+", "-"}):
        violations["strand_invalid"].append(index) 

    # frame check
    # 8th field (index 7)
    # Generic record allowed values: {0, 1, 2, .}
    # "start_codon" or "stop_codon" feature allowed values: {0, 1, 2}
    if not is_field_valid(record[7], {"0", "1", "2", "."}):
        violations["frame_invalid"].append(index)
        
    if record[2] == "start_codon" and not is_field_valid(record[7], {"0", "1", "2"}):
        violations["start_codon_invalid_frame"].append(index)
    elif record[2] == "stop_codon"and not is_field_valid(record[7], {"0", "1", "2"}):
        violations["stop_codon_invalid_frame"].append(index)