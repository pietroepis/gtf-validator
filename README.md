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


After validation, detected violations are listed in `report.txt` file, that is written in current directory.
