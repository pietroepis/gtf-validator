# - Dictionary used to store detected errors
# - The key represents the error_code. Both "value" and "msg" are stored in the same data structure to avoid keys redundancy
# - "value" is a boolean whether it refers to a global inter-record error, 
#   whereas it's a list if it holds line numbers of error occurrences
# - "msg" is the message that will be printed in the report
violations = {
    "source_not_unique": {
        "value": False,
        "msg": "\"source\" field must be unique"
    },
    "missing_cds": {
        "value": True,
        "msg": "A \"CDS\" record is required"
    },
    "missing_start_codon": {
        "value": True,
        "msg": "A \"start_codon\" record is required"
    },
    "missing_stop_codon": {
        "value": True,
        "msg": "A \"stop_codon\" record is required"
    },
    "start_codon_more_than_3": {
        "value": False,
        "msg": "\"start_codon\" total lenght must be less than or equal to 3"
    },
    "stop_codon_more_than_3": {
        "value": False,
        "msg": "\"stop_codon\" total lenght must be less than or equal to 3"
    },
    "invalid_fields_number": {
        "value": [],
        "msg": "invalid number fields in the record"
    },
    "start_codon_invalid_frame": {
        "value": [],
        "msg": "\"frame\" value not valid. \"start_codon\" record allowed values for \"frame\": {0, 1, 2}"
    },
    "stop_codon_invalid_frame": {
        "value": [],
        "msg": "\"frame\" value not valid. \"stop_codon\" record allowed values for \"frame\": {0, 1, 2}"
    },
    "inter_trascript_id_not_empty": {
        "value": [],
        "msg": "\"trascript_id\" attribute must be empty for a \"inter\" record"
    },
    "inter_CNS_trascript_id_not_empty": {
        "value": [],
        "msg": "\"trascript_id\" attribute must be empty for a \"inter_CNS\" record"
    },
    "intron_CNS_trascript_id_empty": {
        "value": [],
        "msg": "\"trascript_id\" attribute must be non-empty for a \"intron_CNS\" record"
    },
    "start_not_valid": {
        "value": [],
        "msg": "\"start\" must be an integer greater than or equal to 1"
    },
    "end_not_valid": {
        "value": [],
        "msg": "\"end\" must be an integer greater than or equal to 1"
    },
    "start_greater_than_end": {
        "value": [],
        "msg": "\"start\" must be less than or equal to \"end\""
    },
    "invalid_frame_contig_start_codon": {
        "value": [],
        "msg": "if \"start_codon\" is contiguous, frame must be 0"
    },
    "invalid_frame_contig_stop_codon": {
        "value": [],
        "msg": "if \"stop_codon\" is contiguous, frame must be 0"
    },
    "score_invalid": {
        "value": [],
        "msg": "\"score\" must be a numeric value. Dot allowed too"
    },
    "strand_invalid": {
        "value": [],
        "msg": "\"strand\" value not valid. Allowed values: {+, -}"
    },
    "frame_invalid": {
        "value": [],
        "msg": "\"frame\" value not valid. Allowed values: {0, 1, 2, .}"
    },
    "missing_gene_id": {
        "value": [],
        "msg": "\"gene_id\" attribute is required"
    },
    "missing_transcript_id": {
        "value": [],
        "msg": "\"transcript_id\" attribute is required"
    },
    "invalid_attributes_order": {
        "value": [],
        "msg": "Invalid attributes order. \"gene_id\" and \"transcript_id\" must precede all the others"
    },
    "invalid_attributes_separator": {
        "value": [],
        "msg": "Every attribute must end in a semicolon and be separated from the next one by exactly one space"
    },
    "text_attribute_not_doublequotes": {
        "value": [],
        "msg": "Text attributes must be wrapped by double quotes"
    },
}