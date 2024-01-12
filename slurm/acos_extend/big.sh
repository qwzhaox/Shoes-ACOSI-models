#!/bin/bash

#SBATCH --partition=spgpu
#SBATCH --time=00-36:00:00
#SBATCH --gpus=8
#SBATCH --cpus-per-gpu=4
#SBATCH --nodes=1 
#SBATCH --mem-per-cpu=11500m
#SBATCH --account=wangluxy1
#SBATCH --mail-user=qwzhao@umich.edu
#SBATCH --mail-type=BEGIN,END,FAIL
#SBATCH --job-name=acos_extend_big

module load python cuda
pushd /home/qwzhao/src/absa/EECS595Project

source env/bin/activate

bash scripts/bash/run.sh -t acos-extend -m llama-2 -s big