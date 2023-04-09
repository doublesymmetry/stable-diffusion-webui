#!/bin/bash
####################################################################
#                          macOS defaults                          #
# Please modify webui-user.sh to change these instead of this file #
####################################################################

if [[ -x "$(command -v python3.10)" ]]
then
    python_cmd="python3.10"
fi

export install_dir="$HOME"
export COMMANDLINE_ARGS="--skip-torch-cuda-test --skip-install --precision full --no-half-vae --upcast-sampling --opt-sub-quad-attention --use-cpu interrogate"
export USE_DISTRIBUTED=1
export TORCH_COMMAND="pip install --pre git+https://github.com/brkirch/pytorch@e87e0272a4bca458574d1c38161a8982b00e89db#egg=torch torchvision==0.15.0.dev20230302 -f https://download.pytorch.org/whl/nightly/cpu/torch_nightly.html"
export K_DIFFUSION_REPO="https://github.com/brkirch/k-diffusion.git"
export K_DIFFUSION_COMMIT_HASH="51c9778f269cedb55a4d88c79c0246d35bdadb71"
export PYTORCH_ENABLE_MPS_FALLBACK=1

# Put transformers cache with the other models
export TRANSFORMERS_CACHE="$PWD/models/transformers"

# Add git and python to PATH
export PATH="$PWD/python/3.10.10/bin:$PWD/git/bin:$PATH"
export GIT_EXEC_PATH="$PWD/git/libexec/git-core"
export GIT_TEMPLATE_DIR="$PWD/git/share/git-core/templates"

####################################################################
