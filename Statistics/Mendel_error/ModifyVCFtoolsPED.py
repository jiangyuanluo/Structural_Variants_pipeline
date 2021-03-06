#! /bin/python3

# Because the PED file generated by vcftools does not contain the family structure information, I need to manually correct them, given PedStructSeqID.txt.

import sys

pedfile=sys.argv[1]
pedStruct=sys.argv[2]
outfile=sys.argv[3]

d={} # dictionary, with seqID as key, family ID, person ID, father ID, mother ID as value
with open(pedfile) as f, open(pedStruct) as s, open(outfile,'w') as o:
	s.readline() # skip the header line
	for line in s:
		temp=line.strip().split()
		if temp[7]!='NA':
			#print (temp[7])
			d[temp[7]]=temp[0:6]
	#print (d)
	for line in f:
		temp=line.strip().split()
		token=d[temp[0]]
		if token[2]!='0':
			token[2]=token[0]+':'+token[2]
		if token[3]!='0':
			token[3]=token[0]+':'+token[3]
		token[1]=token[0]+':'+token[1]
		if token[4]=='m':
			token[4]='1'
		elif token[4]=='f':
			token[4]='2'
		else:
			token[4]='other'
		token[5]='1'
		outline='\t'.join(token+temp[6:])
		o.write(outline+'\n')
	
