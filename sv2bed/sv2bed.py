#!/usr/bin/env python
from argparse import RawTextHelpFormatter
import argparse
import os
import sys
#####################
__version__='0.0.1'

__usage__='''

.d8888. db    db  .d888b.  d8888b. d88888b d8888b. 
88'  YP 88    88  VP  `8D  88  `8D 88'     88  `8D 
`8bo.   Y8    8P     odD'  88oooY' 88ooooo 88   88 
  `Y8b. `8b  d8'   .88'    88~~~b. 88~~~~~ 88   88 
db   8D  `8bd8'   j88.     88   8D 88.     88  .8D 
`8888Y'    YP     888888D  Y8888P' Y88888P Y8888D' 

            convert a sv vcf to bed
--------------------------------------------------

Version:  {}
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
    for example:    sv2bed in.vcf -f %CHROM,%POS0,%ID 

    when using the -i or -e options, format the argument as
    if you were using bcftools query or view.
    for example:    sv2bed in.vcf -e 'INFO/SVTYPE~"DEL"'

'''.format(__version__)
def exit():
	sys.stderr.write(__usage__+'\n')
	sys.exit(0)
class Args(object):
	def __init__(self):
		parser = argparse.ArgumentParser(formatter_class=RawTextHelpFormatter, usage=__usage__, add_help=False)
		parser.add_argument('vcf',type=str,nargs='?')	
		if len(sys.argv)==1: exit()
		if sys.argv[1] in ['-h','--help','-help']: exit()
		args = parser.parse_args(sys.argv[1:2])
		if args.vcf == None: self.vcf ='/dev/stdin'
		else: self.vcf = args.vcf 

		parser = argparse.ArgumentParser(formatter_class=RawTextHelpFormatter, usage=__usage__, add_help=False)
		parser.add_argument('-f',type=str, required=False,default=None)
		parser.add_argument('-i',type=str, required=False,default='')
		parser.add_argument('-e',type=str, required=False,default='')
		parser.add_argument('-o',type=str, required=False,default='')
		parser.add_argument('-h','-help',required=False,action="store_true", default=False)
		
		args = parser.parse_args(sys.argv[2:])
	
		if args.h == True: exit()	
		if args.f == None:
			args.f = "%CHROM{0}%POS0{0}%INFO/END{0}%INFO/SVTYPE{1}".format("\\t","\\n")
		else: 
			form = args.f.split(',')
			args.f = '\\t'.join(form)+'\\n'	
		if args.i != '': args.i = " -i '{}' ".format(args.i)
		if args.e != '': args.e = " -e '{}' ".format(args.e) 
		if args.o != '': args.o = " -o {} ".format(args.o)
		self.args=args
	

def main():
	args = Args()
	cmd = "bcftools query -f '{}' {}{}{} {}".format(args.args.f,
							args.args.o,
							args.args.i,
							args.args.e,
							args.vcf)
	os.system(cmd)

if __name__=='__main__': main()
