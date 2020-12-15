#!/bin/bash
#
#SBATCH --partition=debug
#SBATCH --ntasks=1
#SBATCH --mem=1024
#SBATCH --output=jobname_%J_stdout.txt
#SBATCH --error=jobname_%J_stderr.txt
#SBATCH --time=00:10:00
#SBATCH --job-name=
#SBATCH --mail-user=
#SBATCH --mail-type=ALL
#SBATCH --chdir=
#
#################################################

module load Biopython

python3 tbl.py
