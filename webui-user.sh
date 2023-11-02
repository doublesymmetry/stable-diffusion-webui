#!/bin/bash
#########################################################
# Uncomment and change the variables below to your need:#
#########################################################

# Install directory without trailing slash
#install_dir="/home/$(whoami)"

# Name of the subdirectory
#clone_dir="stable-diffusion-webui"

# Commandline arguments for webui.py, for example: export COMMANDLINE_ARGS="--medvram --opt-split-attention"
#export COMMANDLINE_ARGS=""

# check if macos, if so set commandline args
if [[ "$OSTYPE" == "darwin"* ]]; then
    export COMMANDLINE_ARGS="--skip-torch-cuda-test --upcast-sampling --opt-sub-quad-attention --use-cpu interrogate --listen --nowebui --port=7860 --cors-allow-origins=*"
else
    export COMMANDLINE_ARGS="--listen --nowebui --port=7860 --cors-allow-origins=*"
fi

# python3 executable
#python_cmd="python3"

# git executable
#export GIT="git"

# python3 venv without trailing slash (defaults to ${install_dir}/${clone_dir}/venv)
#venv_dir="venv"
venv_dir="venv-torch-nightly"

# script to launch to start the app
#export LAUNCH_SCRIPT="launch.py"

# install command for torch
#export TORCH_COMMAND="pip install torch==1.12.1+cu113 --extra-index-url https://download.pytorch.org/whl/cu113"
if [[ "$OSTYPE" == "darwin"* ]]; then
    export TORCH_COMMAND="pip install --pre torch torchvision -f https://download.pytorch.org/whl/nightly/cpu/torch_nightly.html"
else
    export TORCH_COMMAND="pip install --pre torch torchvision -f https://download.pytorch.org/whl/nightly/cu113/torch_nightly.html"
fi

# Requirements file to use for stable-diffusion-webui
#export REQS_FILE="requirements_versions.txt"

# Fixed git repos
#export K_DIFFUSION_PACKAGE=""
#export GFPGAN_PACKAGE=""

# Fixed git commits
#export STABLE_DIFFUSION_COMMIT_HASH=""
#export CODEFORMER_COMMIT_HASH=""
#export BLIP_COMMIT_HASH=""

# Uncomment to enable accelerated launch
#export ACCELERATE="True"

# Uncomment to disable TCMalloc
#export NO_TCMALLOC="True"

###########################################
