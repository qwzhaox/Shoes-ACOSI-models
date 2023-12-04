#!/bin/bash

#SBATCH --partition=spgpu
#SBATCH --time=00-64:00:00
#SBATCH --gpus=8
#SBATCH --cpus-per-gpu=4
#SBATCH --nodes=1 
#SBATCH --mem-per-cpu=11500m
#SBATCH --account=wangluxy1
#SBATCH --mail-user=qwzhao@umich.edu
#SBATCH --mail-type=BEGIN,END,FAIL
#SBATCH --job-name=acosi_extract_big

module load python cuda
pushd /home/qwzhao/src/absa/EECS595Project

source env/bin/activate

bash scripts/bash/acosi_extract/big.sh