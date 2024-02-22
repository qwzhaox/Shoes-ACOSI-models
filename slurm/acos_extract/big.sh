#!/bin/bash

#SBATCH --partition=spgpu
#SBATCH --time=06-00:00:00
#SBATCH --gpus=16
#SBATCH --cpus-per-gpu=4
#SBATCH --nodes=2 
#SBATCH --mem-per-cpu=11500m
#SBATCH --account=wangluxy1
#SBATCH --mail-user=qwzhao@umich.edu
#SBATCH --mail-type=BEGIN,END,FAIL
#SBATCH --job-name=ae_big

# conda
module load python3.10-anaconda/2023.03
pushd /home/qwzhao/src/absa/LLM-acosi

source /sw/pkgs/arc/python3.10-anaconda/2023.03/bin/activate
conda activate llm_acosi


bash scripts/bash/run.sh -t acos-extract -m llama-2 -s big