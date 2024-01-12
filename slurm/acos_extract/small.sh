#!/bin/bash

#SBATCH --partition=spgpu
#SBATCH --time=00-10:00:00
#SBATCH --gpus=2
#SBATCH --cpus-per-gpu=4
#SBATCH --nodes=1 
#SBATCH --mem-per-cpu=11500m
#SBATCH --account=wangluxy1
#SBATCH --mail-user=qwzhao@umich.edu
#SBATCH --mail-type=BEGIN,END,FAIL
#SBATCH --job-name=acos_extract_small

module load python cuda
pushd /home/qwzhao/src/absa/EECS595Project

source env/bin/activate

bash scripts/bash/run.sh -t acos-extract -m llama-2 -s small