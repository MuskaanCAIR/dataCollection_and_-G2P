ENV_NAME = "data_collect"

export CONDA_ALWAYS_YES="true"

#update conda in your system
conda update -n base -c defaults conda

#incase the environment already exists, remove it
conda remove -n $ENV_NAME --all

#create the environment
conda create -n $ENV_NAME python=3.10 -y

#configure shell for conda
conda init bash

#activate environment
conda activate $ENV_NAME

#disable yes to all
unset CONDA_ALWAYS_YES