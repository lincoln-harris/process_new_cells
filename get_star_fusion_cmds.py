import os

roots = []
for f in os.listdir('fastq/'):
	root = f.split('_')[0] + '_' + f.split('_')[1]

	if root in roots:
		continue
	else:
		fq1 = root + '_R1.fastq.gz'
		fq2 = root + '_R2.fastq.gz'
		cmd = '/usr/local/src/STAR-Fusion/STAR-Fusion --left_fq ' + fq1 + ' --right_fq ' + fq2 + ' --genome_lib_dir `pwd`/ctat_genome_lib_build_dir -O StarFusionOut/' + root + '/ --FusionInspector validate --examine_coding_effect --denovo_reconstruct --CPU 8'
		print(cmd)
		roots.append(root)