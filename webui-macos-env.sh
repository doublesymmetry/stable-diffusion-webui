#!/bin/bash
####################################################################
#                          macOS defaults                          #
# Please modify webui-user.sh to change these instead of this file #
####################################################################

export install_dir="$HOME"
export COMMANDLINE_ARGS="--skip-torch-cuda-test --skip-install --no-download-sd-model --no-half-vae --upcast-sampling --use-cpu interrogate"
export TORCH_COMMAND="pip install --pre torch torchvision -f https://download.pytorch.org/whl/nightly/cpu/torch_nightly.html"
export PYTORCH_ENABLE_MPS_FALLBACK=1

# Put transformers cache with the other models
export TRANSFORMERS_CACHE="$PWD/models/transformers"

# Add git, python, and node.js to PATH
export PATH="$PWD/bin-deps/python/3.10.13/bin:$PWD/bin-deps/git/bin:$PWD/bin-deps/node/bin:$PATH"
export GIT_EXEC_PATH="$PWD/bin-deps/git/libexec/git-core"
export GIT_TEMPLATE_DIR="$PWD/bin-deps/git/share/git-core/templates"
export NODE_PATH=$(npm root --quiet -g)

if [[ -x "$(command -v python3.10)" ]]
then
    python_cmd="python3.10"
fi

####################################################################
