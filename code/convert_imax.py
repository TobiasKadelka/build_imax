#!/usr/bin/env python
# coding: utf8
import os

# this function gets an input-path as a string, iterates over all folders in there 
# and prints commands, that can be copied and be run as a shell script.
# The script is directly created for IMAX (Susannes dataset, that she got from china)
# and does not work for other datasets.
def convert_bids( input_path ):
	folder_list = os.listdir( input_path )
	for folder in folder_list:
		# I just need to iterate over the folders with data, not the files.
		# The test for "." in folder is as good as every other solution
		if "." in folder:
			continue

		# The subject-folders are named like IMAX01-3, where the "IMAX01" is the subject name
		# and the numbers after the - are the session-numbers.
		subject_key = folder.split("-")[0]
		session_key = folder.split("-")[1]

		# I construct the complete file-path for every nii.gz that we want, instant of iterating over
		# all the IMAX-files, because some datasets might contain "random files for just one subject
		# without additional explanations", that I can skip that way.
		# example file path: IMAX01-1/Circus/IMAX01-1_Circus_data.nii.gz

		# for every subject there should be a "..../Circus/IMAX01-1_Circus_data.nii.gz" file.
		source_circus = input_path + folder + "/Circus/" + folder + "_Circus_data.nii.gz"
		destination_circus = output_path + "sub-" + subject_key + "/ses-" + session_key + "/func/sub-" + subject_key + "_ses-" + session_key + "_task-circus.nii.gz"
		if os.path.isfile( source_circus ):
			# create every folder that is necassary for that file. If folders already exist
			# nothing bad should happen.
			print ("mkdir -p " + destination_circus[ 0 : destination_circus.rfind("/") ] )
			print ("cp " + source_circus + " " + destination_circus + "\n")


		# example for inscape: /data/BnB1/DATA/download_data/Zhou/IMAX/IMAX01-1/Inscape/IMAX01-1_Inscape_data.nii.gz
		source_inscape = input_path + folder + "/Inscape/" + folder + "_Inscape_data.nii.gz"
		destination_inscape = output_path + "sub-" + subject_key + "/ses-" + session_key + "/func/sub-" + subject_key + "_ses-" + session_key + "_task-inscape.nii.gz"
		if os.path.isfile( source_inscape ):
			# create every folder that is necassary for that file
                        print ("mkdir -p " + destination_inscape[ 0 : destination_inscape.rfind("/") ] )
                        print ("cp " + source_inscape + " " + destination_inscape + "\n")


		# same same for task-movies:
		source_movie = input_path + folder + "/Movie/" + folder + "_Movie_data.nii.gz"
		destination_movie = output_path + "sub-" + subject_key + "/ses-" + session_key + "/func/sub-" + subject_key + "_ses-" + session_key + "_task-movie.nii.gz"
		if os.path.isfile( source_movie ):
			# create every folder that is necassary for that file
			print ("mkdir -p " + destination_movie[ 0 : destination_movie.rfind("/") ] )
			print ("cp " + source_movie + " " + destination_movie + "\n")


		# next: 2 files IMAX01-1/MPR/IMAX01-1_defacedMPR_data.nii.gz, and the same but with .log instead of .nii.gz.
		# This files aren't in bids right now, but I think, they should be stored with the other files (not just for
		# for converting it to bids later, but also so that susanne can use the files already).
		source_defacedMPR = input_path + folder + "/MPR/" + folder + "_defacedMPR_data.nii.gz"
		destination_defacedMPR = output_path + "sub-" + subject_key + "/ses-" + session_key + "/anat/sub-" + subject_key + "_ses-" + session_key + "_task-defacedMPR.nii.gz"
		if os.path.isfile( source_defacedMPR ):
			# create every folder that is necassary for that file
			print ("mkdir -p " + destination_defacedMPR[ 0 : destination_defacedMPR.rfind("/") ] )
			print ("cp " + source_defacedMPR + " " + destination_defacedMPR + "\n")
			print ("cp " + source_defacedMPR.replace("nii.gz", "nii.log") + " " + destination_defacedMPR.replace("nii.gz", "log") + "\n")


		# last two files: IMAX01-1/Rest-fMRI-Multi/Run1/IMAX01-1_RSfMRIMultiRun1_data.nii.gz
		# that one and the same but with run5. We don't change the number 5 to 2, because of 
		# possible new mri-images for the sessions after some time.
		# It is also possible, that websites, that describe the data, are giving additional
		# information for each session. If we would change the 5, that would not match our file-names.
		source_rest = input_path + folder + "/Rest-fMRI-Multi/Run1/" + folder + "_RSfMRIMultiRun1_data.nii.gz"                   
		destination_rest = output_path + "sub-" + subject_key + "/ses-" + session_key + "/func/sub-" + subject_key + "_ses-" + session_key + "_run-1_task-rest.nii.gz"    
		if os.path.isfile( source_rest ):  
			# create every folder that is necassary for that file
			print ("mkdir -p " + destination_rest[ 0 : destination_rest.rfind("/") ] )
			print ("cp " + source_rest + " " + destination_rest + "\n")
			print ("cp " + source_rest.replace("Run1", "Run5") + " " + destination_rest.replace("Run1", "Run5").replace("_run-1_", "_run-5_") + "\n")

input_path  = "/data/BnB1/DATA/download_data/Zhou/IMAX/"
output_path = "/data/BnB1/Raw_Data/IMAX/"
convert_bids( input_path )

