import os

for f in os.listdir('./bam_rg'):
	if '.bai' not in f:
		i = 'bam_rg/' + f
		o = 'vcf/' + f.split('_')[0] + '_' + f.split('_')[1] + '.vcf'

		cmd = 'gatk HaplotypeCaller -R ref/hg38-plus/hg38-plus.fa -O ' + o + ' -I ' + i + ' --disable-read-filter MappingQualityReadFilter --disable-read-filter GoodCigarReadFilter --disable-read-filter NotSecondaryAlignmentReadFilter --disable-read-filter MappedReadFilter --disable-read-filter MappingQualityAvailableReadFilter --disable-read-filter NonZeroReferenceLengthAlignmentReadFilter --disable-read-filter NotDuplicateReadFilter --disable-read-filter PassesVendorQualityCheckReadFilter --disable-read-filter WellformedReadFilter --native-pair-hmm-threads 1 --dbsnp ref/common_all_20180418_edit.vcf'

		print(cmd)
		#print(' ')
