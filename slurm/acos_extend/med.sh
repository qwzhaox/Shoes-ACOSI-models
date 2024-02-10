#!/bin/bash

#SBATCH --partition=spgpu
#SBATCH --time=00-08:00:00
#SBATCH --gpus=2
#SBATCH --cpus-per-gpu=2
#SBATCH --nodes=1 
#SBATCH --mem-per-cpu=4000m
#SBATCH --account=wangluxy1
#SBATCH --mail-user=qwzhao@umich.edu
#SBATCH --mail-type=BEGIN,END,FAIL
#SBATCH --job-name=acos_extend_med

module load python cuda
pushd /home/qwzhao/src/absa/LLM-acosi

source env/bin/activate

bash scripts/bash/run.sh -t acos-extend -m llama-2 -s med