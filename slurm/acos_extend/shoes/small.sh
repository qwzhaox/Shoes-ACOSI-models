#!/bin/bash

#SBATCH --partition=spgpu
#SBATCH --time=00-06:00:00
#SBATCH --gpus=1
#SBATCH --cpus-per-gpu=1
#SBATCH --nodes=1 
#SBATCH --mem-per-cpu=1000m
#SBATCH --account=wangluxy1
#SBATCH --mail-user=qwzhao@umich.edu
#SBATCH --mail-type=BEGIN,END,FAIL
#SBATCH --job-name=ax_small

# conda
module load python3.10-anaconda/2023.03
pushd /home/qwzhao/src/absa/LLM-acosi

source /sw/pkgs/arc/python3.10-anaconda/2023.03/bin/activate
conda activate llm_acosi


bash scripts/bash/run.sh -t acos-extend -m llama-2 -s small -d shoes