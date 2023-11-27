#!/bin/bash

#SBATCH --partition=spgpu
#SBATCH --time=00-02:00:00
#SBATCH --gpus=1
#SBATCH --cpus-per-gpu=1
#SBATCH --nodes=1 
#SBATCH --mem-per-cpu=2800m
#SBATCH --account=eecs595f23_class
#SBATCH --mail-user=qwzhao@umich.edu
#SBATCH --mail-type=BEGIN,END,FAIL
#SBATCH --job-name=acos_extend_small

module load python cuda
pushd /home/qwzhao/src/absa/EECS595Project

source env/bin/activate

bash scripts/bash/acos_extend/small.sh