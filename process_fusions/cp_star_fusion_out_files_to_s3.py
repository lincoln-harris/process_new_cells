import os

curr_path = os.getcwd()
s3_path = 's3://darmanis-group/lincoln_scratch/LAUD_revisions/StarFusionOut_3.16.20/'

for subdir in os.listdir(curr_path):
	if '.py' not in subdir and '.sh' not in subdir:

		fullpath = curr_path + '/' + subdir + '/'

		for f in os.listdir(fullpath):
			if f == 'star-fusion.fusion_predictions.tsv':
				star_path = fullpath + f 
				new_f_name = subdir + '_' + 'star-fusion.fusion_predictions.tsv'

				cmd = 'aws s3 cp ' + star_path + ' ' + s3_path + new_f_name
				print(cmd)