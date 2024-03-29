#!/bin/bash

#SBATCH --partition=spgpu
#SBATCH --time=00-01:00:00
#SBATCH --gpus=1
#SBATCH --cpus-per-gpu=1
#SBATCH --nodes=1 
#SBATCH --mem-per-cpu=11500m
#SBATCH --account=wangluxy
#SBATCH --mail-user=qwzhao@umich.edu
#SBATCH --mail-type=BEGIN,END,FAIL
#SBATCH --job-name=eval_unified_mvp

# conda
module load python3.10-anaconda/2023.03
pushd /home/qwzhao/src/absa/multi-view-prompting-acosi

source /sw/pkgs/arc/python3.10-anaconda/2023.03/bin/activate
conda activate mvp

# run job
bash scripts/eval_unified.sh