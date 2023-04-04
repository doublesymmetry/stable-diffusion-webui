#!/bin/bash
#########################################################
# Uncomment and change the variables below to your need:#
#########################################################

# Install directory without trailing slash
#install_dir="/home/$(whoami)"

# Name of the subdirectory
#clone_dir="stable-diffusion-webui"

# Commandline arguments for webui.py, for example: export COMMANDLINE_ARGS="--medvram --opt-split-attention"
export COMMANDLINE_ARGS="--skip-torch-cuda-test --skip-install --upcast-sampling --opt-sub-quad-attention --use-cpu interrogate"

# python3 executable
#python_cmd="python3"

# git executable
#export GIT="git"

# python3 venv without trailing slash (defaults to ${install_dir}/${clone_dir}/venv)
#venv_dir="venv"

# script to launch to start the app
#export LAUNCH_SCRIPT="launch.py"

# install command for torch
export USE_DISTRIBUTED=1
export TORCH_COMMAND="pip install --pre git+https://github.com/brkirch/pytorch@14f753fbe267eb204d52e42f1fb2c8390867cc70#egg=torch torchvision==0.15.0.dev20230302 -f https://download.pytorch.org/whl/nightly/cpu/torch_nightly.html"

# Requirements file to use for stable-diffusion-webui
#export REQS_FILE="requirements_versions.txt"

# Fixed git repos
#export K_DIFFUSION_PACKAGE=""
#export GFPGAN_PACKAGE=""

# Fixed git commits
#export STABLE_DIFFUSION_COMMIT_HASH=""
#export TAMING_TRANSFORMERS_COMMIT_HASH=""
#export CODEFORMER_COMMIT_HASH=""
#export BLIP_COMMIT_HASH=""

# Uncomment to enable accelerated launch
#export ACCELERATE="True"

# Put transformers cache with the other models
export TRANSFORMERS_CACHE="$PWD/models/transformers"

# Add git and python to PATH
export PATH="$PWD/python/3.10.10/bin:$PWD/git/bin:$PATH"
export GIT_EXEC_PATH="$PWD/git/libexec/git-core"
export GIT_TEMPLATE_DIR="$PWD/git/share/git-core/templates"

###########################################
