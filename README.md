#sv2bed
-------

# Install 

`pip install https://github.com/dantaki/sv2bed/releases/download/0.0.1/sv2bed-0.0.1.tar.gz `

-----------------

# Usage
```
.d8888. db    db  .d888b.  d8888b. d88888b d8888b. 
88'  YP 88    88  VP  `8D  88  `8D 88'     88  `8D 
`8bo.   Y8    8P     odD'  88oooY' 88ooooo 88   88 
  `Y8b. `8b  d8'   .88'    88~~~b. 88~~~~~ 88   88 
db   8D  `8bd8'   j88.     88   8D 88.     88  .8D 
`8888Y'    YP     888888D  Y8888P' Y88888P Y8888D' 

            convert a sv vcf to bed
--------------------------------------------------

Version:  0.0.1
Author:   Danny Antaki <dantaki at ucsd dot com>
About:    convert a vcf of svs to a bed file with bcftools
Usage:    sv2bed [-h] <vcf> [options]

Options:
    -f    STR         format string for bcftools query
    -i    STR         include option for bcftools query
    -e    STR         exclude option for bcftools query
    -o    FILE        output file [default: /dev/stdout]

    -h                print this message and exit

Notes:
    sv2bed by default outputs a tab delimited bed file using
    INFO/END as the end position and INFO/SVTYPE in the 
    fourth column [CHROM POS0 INFO/END INFO/SVTYPE]

    sv2bed requires bcftools to be in the environment path

    when using the -f option, pass each variable as a comma
    separated string.
    for example:    sv2bed in.vcf -f %%CHROM,%%POS0,%%ID 

    when using the -i or -e options, format the argument as
    if you were using bcftools query or view.
    for example:    sv2bed in.vcf -e 'INFO/SVTYPE~"DEL"'
```


