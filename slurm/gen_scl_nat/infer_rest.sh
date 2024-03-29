#!/bin/bash

#SBATCH --partition=spgpu
#SBATCH --time=00-00:30:00
#SBATCH --gpus=1
#SBATCH --cpus-per-gpu=1
#SBATCH --nodes=1 
#SBATCH --mem-per-cpu=11500m
#SBATCH --account=wangluxy1
#SBATCH --mail-user=qwzhao@umich.edu
#SBATCH --mail-type=BEGIN,END,FAIL
#SBATCH --job-name=infer_r_gsn

# conda
module load python3.10-anaconda/2023.03
pushd /home/qwzhao/src/absa/GEN_SCL_NAT_acosi

source /sw/pkgs/arc/python3.10-anaconda/2023.03/bin/activate
conda activate gen_scl_nat_env

# run job
bash configs/infer_restaurant.sh