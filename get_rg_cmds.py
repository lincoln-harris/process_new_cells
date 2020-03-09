import os

for f in os.listdir('./bam'):
	if '.bai' not in f:
		i = 'bam/' + f
		o = 'bam_rg/' + f.split('.')[0] + '_rg.bam'
		cmd = 'gatk AddOrReplaceReadGroups -I ' + i + ' -O ' + o + ' -RGID 4 -RGLB lib1 -RGPL illumina -RGPU unit1 -RGSM 20'
		print(cmd)
