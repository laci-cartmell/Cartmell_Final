#!/usr/bin/env python

######################################################################################################
# PARTS OF THE SCRIPT
# Load needed modules
# Create the destination directory
# Unzip a .gz file and convert from fq to fa
# Copy files to the destination directory
# Rename files by removing .fq.gz

######################################################################################################
## Load needed modules

import gzip
import os
import shutil
from Bio import SeqIO

######################################################################################################
## Create a new directory for the unzipped files

# Give name of the new directory
new_directory = '/scratch/tubiol786304/Project/UnzippedSequences'

# Parent Directory - give name of cwd
parent_dir = '/scratch/tubiol786304/Project'

# Join paths
path = os.path.join(parent_dir, new_directory)

# Make the new directory
os.mkdir(path)

# print to output if directory is successfully created
print("Directory '%s' created" %new_directory)

######################################################################################################
## Unzip .gz and convert from fastq to fasta

# The directory with the files to be modified
directory = 'Files'

# Create list of zipped files name
Zipped_files = []

# Iterate through all files in directory to unzip and convert files from fq to fa
for zipped in os.scandir(directory):
    if zipped.path.endswith(".gz"):
       file_name = os.path.abspath(zipped)
       Zipped_files.append(os.path.basename(zipped))
       gzip.open(file_name, 'rt+')
       SeqIO.convert(file_name, "fastq-illumina", zipped, "fasta")
    else:
       print(zipped, "Files are already unzipped OR there are no .gz files in this directory.")

# Print the name of the zipped files
print("Files that are zipped", Zipped_files)

######################################################################################################
## Copy files to the destination directory

# name the source of the files
source_files = os.listdir(directory)

# create an abs.path for all files in directory, & copy to new_directory
for file in source_files:
    full_name = os.path.join(directory, file)
    shutil.copy(full_name, new_directory)

# Print the new_directory path way
print("\nThe destination path is:", new_directory)

######################################################################################################
## Rename files so that the .fq.gz is dropped

# Create a new variable that contains the new_directory name
destination = 'UnzippedSequences'

# For printing the newly formated names
print_unzipped_names = []

# Rename the files already in the destination directory
for file in os.scandir(destination):
    zipped_path = os.path.abspath(file)
    unzipped_name = os.path.basename(file).rsplit('.', 2)[0]
    print_unzipped_names.append(unzipped_name)
    os.rename(os.path.join(destination, zipped_path), os.path.join(destination, unzipped_name))

# Print the new names
print("\n These are the new file names\n\t", print_unzipped_names) 

######################################################################################################
## Compare number of original files to number of new files created

# Use len to count the number of files
num_original = len(Zipped_files)
num_new = len(print_unzipped_names)

# Print the number of original and new files
print(f"\nIf code ran properly, there should be the same number of original and new files: \n\tThere are {num_original} original files and {num_new} new files")

