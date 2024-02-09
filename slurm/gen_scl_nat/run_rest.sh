#!/bin/bash

#SBATCH --partition=spgpu
#SBATCH --time=00-05:00:00
#SBATCH --gpus=1
#SBATCH --cpus-per-gpu=4
#SBATCH --nodes=1 
#SBATCH --mem-per-cpu=11500m
#SBATCH --account=wangluxy1
#SBATCH --mail-user=qwzhao@umich.edu
#SBATCH --mail-type=BEGIN,END,FAIL
#SBATCH --job-name=rest_gen_scl_nat

# conda
module load python3.10-anaconda/2023.03
pushd /home/qwzhao/src/absa/GEN_SCL_NAT_acosi

source /sw/pkgs/arc/python3.10-anaconda/2023.03/bin/activate
conda activate gen_scl_nat_env

# run job
bash configs/run_restaurant.sh