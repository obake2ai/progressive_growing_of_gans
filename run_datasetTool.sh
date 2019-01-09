#!/bin/sh
#PBS -q h-regular
#PBS -l select=1:mpiprocs=1:ompthreads=32
#PBS -W group_list=gj16
#PBS -l walltime=20:00:00
cd $PBS_O_WORKDIR
. /etc/profile.d/modules.sh
module load cuda9/9.1.85
module load tensorflow/1.8.0
export PYENV_ROOT="/lustre/gj16/j16002/.pyenv/"
export PATH=$PYENV_ROOT/bin:$PATH
if command -v pyenv 1>/dev/null 2>&1; then
  eval "$(pyenv init -)"
fi
python dataset_tool.py create_from_images datasets/maico2kiku maico2kiku
