import os

bam_dir = 'bam_rg/'
vcf_dir = 'vcf/'

vcf_list = []
for f in os.listdir(vcf_dir):
	root = f.strip('.vcf')
	vcf_list.append(root)

#print(vcf_list)

for f in os.listdir(bam_dir):
	if '.bai' not in f:
		root = f.strip('_rg.bam')
		if root in vcf_list:
			print(root)
			os.remove(bam_dir + f)

