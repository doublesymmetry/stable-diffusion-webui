#!/bin/bash
####################################################################
#                          macOS defaults                          #
# Please modify webui-user.sh to change these instead of this file #
####################################################################

delimiter="################################################################"

printf "\n%s\n" "${delimiter}"
printf "\e[1m\e[31m                          **WARNING**\n"
printf "\e[1m\e[31m  This is a test build of stable-diffusion-webui and PyTorch!\n"
printf "\e[1m\e[31mCrashes and bugs are expected, do not assume it will be stable!\n"
printf "\e[1m\e[31m   DO NOT report issues to the web UI or PyTorch developers!\n"
printf "\e[1m\e[33mReport issues to github.com/brkirch/stable-diffusion-webui/issues\e[0m"
printf "\n%s\n" "${delimiter}"

export install_dir="$HOME"
export COMMANDLINE_ARGS="--skip-torch-cuda-test --skip-install --precision full --no-half-vae --upcast-sampling --opt-sub-quad-attention --use-cpu interrogate"
export USE_DISTRIBUTED=1
export TORCH_COMMAND="pip install --pre git+https://github.com/brkirch/pytorch@e87e0272a4bca458574d1c38161a8982b00e89db#egg=torch torchvision==0.15.0.dev20230302 -f https://download.pytorch.org/whl/nightly/cpu/torch_nightly.html"
export K_DIFFUSION_REPO="https://github.com/brkirch/k-diffusion.git"
export K_DIFFUSION_COMMIT_HASH="3f2c40051a71eb1e5e07b2d66e17b5f0d45b96d5"
export PYTORCH_ENABLE_MPS_FALLBACK=1

# Put transformers cache with the other models
export TRANSFORMERS_CACHE="$PWD/models/transformers"

# Add git and python to PATH
export PATH="$PWD/python/3.10.10/bin:$PWD/git/bin:$PATH"
export GIT_EXEC_PATH="$PWD/git/libexec/git-core"
export GIT_TEMPLATE_DIR="$PWD/git/share/git-core/templates"

if [[ -x "$(command -v python3.10)" ]]
then
    python_cmd="python3.10"
fi

####################################################################
