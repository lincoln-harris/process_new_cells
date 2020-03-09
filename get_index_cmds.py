import os

for f in os.listdir('./bam_rg'):
	#print(f)
	i = './bam_rg/' + f
	o = './bam_rg/' + f + '.bai'
	cmd = 'samtools index ' + i + ' ' + o
	print(cmd)
