import re

file_name = "./samples/file-1.gtf"
lines = []
violations = {
    "missing_cds": True,
    "missing_start_codon": True,
    "missing_stop_codon": True,
    "start_codon_more_than_3": False,
    "stop_codon_more_than_3": False,
    "start_codon_invalid_frame": [],
    "stop_codon_invalid_frame": [],
    "inter_trascript_id_not_empty": [],
    "inter_CNS_trascript_id_not_empty": [],
    "intron_CNS_trascript_id_empty": [],
    "start_not_integer": [],
    "stop_not_integer": [],
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
    if line[0] == "#":
        continue

    record = (re.sub("#.*", "", line)).split("\t")

    if record[2] == "CDS":
        violations["missing_cds"] = False
    if record[2] == "start_codon":
        violations["missing_start_codon"] = False
    if record[2] == "stop_codon":
        violations["missing_start_codon"] = False
        