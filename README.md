# gtf-validator
GTF (Gene Transfer Format) file standard validator\
"Elementi di Bioinformatica" Lab Project - UniMiB

The script takes a GTF file as input and checks whether it respects the syntax rules defined by the format.\
The documentation about GTF file standard that was considered is available at https://mblab.wustl.edu/GTF22.html

`samples` folder contains a set of test files. Every file contains one or more errors, but all related to a _single violation_ of those detected by the validator. Every file is associated to its corresponding violation in the description below. `file-0.gtf` doesn't contain any error.

The possible violations that are assessed and evaluated by the script are descripted in following table:
| Error | Description | Sample File |
|-------|-------------|-------------|
| Source not unique | The _source_ field of every record must be the same in the whole file | file-1.gtf |
| Missing CDS | At least one _CDS_ feature is required in the file | file-2.gtf |
| Missing start codon | At least one _start_codon_ feature is required in the file | file-3.gtf |
| Missing stop codon | At least one _stop_codon_ feature is required in the file | file-4.gtf |
| Start codon is more than 3bp long | _start_codon_ feature is allowed to be non-atomic, anyhow its total length is up to 3bp in total | file-5.gtf |
| Stop codon is more than 3bp long | _stop_codon_ feature is allowed to be non-atomic, anyhow its total length is up to 3bp in total | file-6.gtf |
| Invalid fields number | Every record is composed of 9 fields, separated by `\t` (_seqname_, _source_, _feature_, _start_, _end_, _score_, _strand_, _frame_, _attributes_) | file-7.gtf |
| Start codon invalid frame | The allowed values for the _frame_ field of a _start_codon_ feature are {0, 1, 2} | file-8.gtf |
| Stop codon invalid frame | The allowed values for the _frame_ field of a _stop_codon_ feature are {0, 1, 2} | file-9.gtf |
| "transcript_id" not empty in _inter_ feature | "transcript_id" attribute must have `""` as value in _inter_ feature records | file-10.gtf |
| "transcript_id" not empty in _inter_CND_ feature | "transcript_id" attribute must have `""` as value in _inter_CNS_ feature records | file-11.gtf |
| "transcript_id" empty in _intron_CNS_ feature | _intron_CNS_ should have an associated "transcript_id", therefore attribute value should be different from `""` | file-12.gtf |
| Start not valid | _start_ field of every record must be an integer value, greater than or equal to 1 | file-13.gtf |
| End not valid | _end_ field of every record must be an integer value, greater than or equal to 1 | file-14.gtf |
| Start greater than end | _start_ field must be less than or equal to _end_ field | file-15.gtf |
| Invalid frame for contiguous start_codon | If _start_codon_ feature is not split in more records (and so contiguous), its _frame_ value must be 0 | file-16.gtf |
| Invalid frame for contiguous stop_codon | If _stop_codon_ feature is not split in more records (and so contiguous), its _frame_ value must be 0 | file-17.gtf |
| Invalid score | _score_ field must contain a numeric value. A dot is allowed too | file-18.gtf |
| Invalid strand | _strand_ field allowed values are {+, -} | file-19.gtf |
| Invalid frame | _frame_ field allowed values are {0, 1, 2, .} (dot is not allowed for _start_codon_ and _stop_codon_ as stated above) | file-20.gtf |
| Missing "gene_id" | The "gene_id" attribute is required in every record | file-21.gtf |
| Missing "transcript_id" | The "transcript_id" attribute is required in every record, even if with empty value as shown before | file-22.gtf |
| Invalid attributes order | "gene_id" and "transcript_id" attributes must always be the first. Every other possible attribute will follow these two | file-23.gtf |
| Invalid attributes separator | Every attribute must be followed by a semicolon. Whether it's not the last in the list, it will alsa be separated by the following one with exactly one space | file-24.gtf |
| Text attribute not in `""` | Text attributes must be wrapped by double quotes | file-25.gtf |
| Start codon not in CDS coordinates | A _start_codon_ feature (that is not required to be atomic and can be defined in several records as separated intervals) must be included in the intervals of coordinates of the _CDS_ | file-26.gtf |
| Stop codon in 3UTR coordinates | A _stop_codon_ feature (that is not required to be atomic and can be defined in several records as separated intervals) must not be included in the intervals of coordinates of _3UTR_ feature | file-27.gtf |


After validation, detected violations are listed in `report.txt` file, that is written in current directory. Every entry of the report shows a progressive number of the error (a counter), the 1-based index of the line record where the error happened (`/` means that the error doesn't refer to a specific line, but has a global meaning in the file, such as "Missing CDS") and a description of the violation.
