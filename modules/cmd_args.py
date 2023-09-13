import argparse
import json
import os
from modules.paths_internal import models_path, script_path, data_path, extensions_dir, extensions_builtin_dir, sd_default_config, sd_model_file  # noqa: F401

parser = argparse.ArgumentParser()

parser.add_argument("-f", action='store_true', help=argparse.SUPPRESS)  # allows running as root; implemented outside of webui
parser.add_argument("--update-all-extensions", action='store_true', help="launch.py argument: download updates for all extensions when starting the program")
parser.add_argument("--skip-python-version-check", action='store_true', help="launch.py argument: do not check python version")
parser.add_argument("--skip-torch-cuda-test", action='store_true', help="launch.py argument: do not check if CUDA is able to work properly")
parser.add_argument("--reinstall-xformers", action='store_true', help="launch.py argument: install the appropriate version of xformers even if you have some version already installed")
parser.add_argument("--reinstall-torch", action='store_true', help="launch.py argument: install the appropriate version of torch even if you have some version already installed")
parser.add_argument("--update-check", action='store_true', help="launch.py argument: check for updates at startup")
parser.add_argument("--test-server", action='store_true', help="launch.py argument: configure server for testing")
parser.add_argument("--log-startup", action='store_true', help="launch.py argument: print a detailed log of what's happening at startup")
parser.add_argument("--skip-prepare-environment", action='store_true', help="launch.py argument: skip all environment preparation")
parser.add_argument("--skip-install", action='store_true', help="launch.py argument: skip installation of packages")
parser.add_argument("--dump-sysinfo", action='store_true', help="launch.py argument: dump limited sysinfo file (without information about extensions, options) to disk and quit")
parser.add_argument("--loglevel", type=str, help="log level; one of: CRITICAL, ERROR, WARNING, INFO, DEBUG", default=None)
parser.add_argument("--do-not-download-clip", action='store_true', help="do not download CLIP model even if it's not included in the checkpoint")
parser.add_argument("--data-dir", type=str, default=os.path.dirname(os.path.dirname(os.path.realpath(__file__))), help="base path where all user data is stored")
parser.add_argument("--config", type=str, default=sd_default_config, help="path to config which constructs model",)
parser.add_argument("--ckpt", type=str, default=sd_model_file, help="path to checkpoint of stable diffusion model; if specified, this checkpoint will be added to the list of checkpoints and loaded",)
parser.add_argument("--ckpt-dir", type=str, default=None, help="Path to directory with stable diffusion checkpoints")
parser.add_argument("--vae-dir", type=str, default=None, help="Path to directory with VAE files")
parser.add_argument("--gfpgan-dir", type=str, help="GFPGAN directory", default=('./src/gfpgan' if os.path.exists('./src/gfpgan') else './GFPGAN'))
parser.add_argument("--gfpgan-model", type=str, help="GFPGAN model file name", default=None)
parser.add_argument("--no-half", action='store_true', help="do not switch the model to 16-bit floats")
parser.add_argument("--no-half-vae", action='store_true', help="do not switch the VAE model to 16-bit floats")
parser.add_argument("--no-progressbar-hiding", action='store_true', help="do not hide progressbar in gradio UI (we hide it because it slows down ML if you have hardware acceleration in browser)")
parser.add_argument("--max-batch-count", type=int, default=16, help="maximum batch count value for the UI")
parser.add_argument("--embeddings-dir", type=str, default=os.path.join(data_path, 'embeddings'), help="embeddings directory for textual inversion (default: embeddings)")
parser.add_argument("--textual-inversion-templates-dir", type=str, default=os.path.join(script_path, 'textual_inversion_templates'), help="directory with textual inversion templates")
parser.add_argument("--hypernetwork-dir", type=str, default=os.path.join(models_path, 'hypernetworks'), help="hypernetwork directory")
parser.add_argument("--localizations-dir", type=str, default=os.path.join(script_path, 'localizations'), help="localizations directory")
parser.add_argument("--allow-code", action='store_true', help="allow custom script execution from webui")
parser.add_argument("--medvram", action='store_true', help="enable stable diffusion model optimizations for sacrificing a little speed for low VRM usage")
parser.add_argument("--medvram-sdxl", action='store_true', help="enable --medvram optimization just for SDXL models")
parser.add_argument("--lowvram", action='store_true', help="enable stable diffusion model optimizations for sacrificing a lot of speed for very low VRM usage")
parser.add_argument("--lowram", action='store_true', help="load stable diffusion checkpoint weights to VRAM instead of RAM")
parser.add_argument("--always-batch-cond-uncond", action='store_true', help="does not do anything")
parser.add_argument("--unload-gfpgan", action='store_true', help="does not do anything.")
parser.add_argument("--precision", type=str, help="evaluate at this precision", choices=["full", "autocast"], default="autocast")
parser.add_argument("--upcast-sampling", action='store_true', help="upcast sampling. No effect with --no-half. Usually produces similar results to --no-half with better performance while using less memory.")
parser.add_argument("--share", action='store_true', help="use share=True for gradio and make the UI accessible through their site")
parser.add_argument("--ngrok", type=str, help="ngrok authtoken, alternative to gradio --share", default=None)
parser.add_argument("--ngrok-region", type=str, help="does not do anything.", default="")
parser.add_argument("--ngrok-options", type=json.loads, help='The options to pass to ngrok in JSON format, e.g.: \'{"authtoken_from_env":true, "basic_auth":"user:password", "oauth_provider":"google", "oauth_allow_emails":"user@asdf.com"}\'', default=dict())
parser.add_argument("--enable-insecure-extension-access", action='store_true', help="enable extensions tab regardless of other options")
parser.add_argument("--codeformer-models-path", type=str, help="Path to directory with codeformer model file(s).", default=os.path.join(models_path, 'Codeformer'))
parser.add_argument("--gfpgan-models-path", type=str, help="Path to directory with GFPGAN model file(s).", default=os.path.join(models_path, 'GFPGAN'))
parser.add_argument("--esrgan-models-path", type=str, help="Path to directory with ESRGAN model file(s).", default=os.path.join(models_path, 'ESRGAN'))
parser.add_argument("--bsrgan-models-path", type=str, help="Path to directory with BSRGAN model file(s).", default=os.path.join(models_path, 'BSRGAN'))
parser.add_argument("--realesrgan-models-path", type=str, help="Path to directory with RealESRGAN model file(s).", default=os.path.join(models_path, 'RealESRGAN'))
parser.add_argument("--clip-models-path", type=str, help="Path to directory with CLIP model file(s).", default=None)
parser.add_argument("--xformers", action='store_true', help="enable xformers for cross attention layers")
parser.add_argument("--force-enable-xformers", action='store_true', help="enable xformers for cross attention layers regardless of whether the checking code thinks you can run it; do not make bug reports if this fails to work")
parser.add_argument("--xformers-flash-attention", action='store_true', help="enable xformers with Flash Attention to improve reproducibility (supported for SD2.x or variant only)")
parser.add_argument("--deepdanbooru", action='store_true', help="does not do anything")
parser.add_argument("--opt-split-attention", action='store_true', help="prefer Doggettx's cross-attention layer optimization for automatic choice of optimization")
parser.add_argument("--opt-sub-quad-attention", action='store_true', help="prefer memory efficient sub-quadratic cross-attention layer optimization for automatic choice of optimization")
parser.add_argument("--sub-quad-q-chunk-size", type=int, help="query chunk size for the sub-quadratic cross-attention layer optimization to use", default=1024)
parser.add_argument("--sub-quad-kv-chunk-size", type=int, help="kv chunk size for the sub-quadratic cross-attention layer optimization to use", default=None)
parser.add_argument("--sub-quad-chunk-threshold", type=int, help="the percentage of VRAM threshold for the sub-quadratic cross-attention layer optimization to use chunking", default=None)
parser.add_argument("--opt-split-attention-invokeai", action='store_true', help="prefer InvokeAI's cross-attention layer optimization for automatic choice of optimization")
parser.add_argument("--opt-split-attention-v1", action='store_true', help="prefer older version of split attention optimization for automatic choice of optimization")
parser.add_argument("--opt-sdp-attention", action='store_true', help="prefer scaled dot product cross-attention layer optimization for automatic choice of optimization; requires PyTorch 2.*")
parser.add_argument("--opt-sdp-no-mem-attention", action='store_true', help="prefer scaled dot product cross-attention layer optimization without memory efficient attention for automatic choice of optimization, makes image generation deterministic; requires PyTorch 2.*")
parser.add_argument("--disable-opt-split-attention", action='store_true', help="prefer no cross-attention layer optimization for automatic choice of optimization")
parser.add_argument("--disable-nan-check", action='store_true', help="do not check if produced images/latent spaces have nans; useful for running without a checkpoint in CI")
parser.add_argument("--use-cpu", nargs='+', help="use CPU as torch device for specified modules", default=[], type=str.lower)
parser.add_argument("--disable-model-loading-ram-optimization", action='store_true', help="disable an optimization that reduces RAM use when loading a model")
parser.add_argument("--listen", action='store_true', help="launch gradio with 0.0.0.0 as server name, allowing to respond to network requests")
parser.add_argument("--port", type=int, help="launch gradio with given server port, you need root/admin rights for ports < 1024, defaults to 7860 if available", default=None)
parser.add_argument("--show-negative-prompt", action='store_true', help="does not do anything", default=False)
parser.add_argument("--ui-config-file", type=str, help="filename to use for ui configuration", default=os.path.join(data_path, 'ui-config.json'))
parser.add_argument("--hide-ui-dir-config", action='store_true', help="hide directory configuration from webui", default=False)
parser.add_argument("--freeze-settings", action='store_true', help="disable editing settings", default=False)
parser.add_argument("--ui-settings-file", type=str, help="filename to use for ui settings", default=os.path.join(data_path, 'config.json'))
parser.add_argument("--gradio-debug",  action='store_true', help="launch gradio with --debug option")
parser.add_argument("--gradio-auth", type=str, help='set gradio authentication like "username:password"; or comma-delimit multiple like "u1:p1,u2:p2,u3:p3"', default=None)
parser.add_argument("--gradio-auth-path", type=str, help='set gradio authentication file path ex. "/path/to/auth/file" same auth format as --gradio-auth', default=None)
parser.add_argument("--gradio-img2img-tool", type=str, help='does not do anything')
parser.add_argument("--gradio-inpaint-tool", type=str, help="does not do anything")
parser.add_argument("--gradio-allowed-path", action='append', help="add path to gradio's allowed_paths, make it possible to serve files from it", default=[data_path])
parser.add_argument("--opt-channelslast", action='store_true', help="change memory type for stable diffusion to channels last")
parser.add_argument("--styles-file", type=str, help="filename to use for styles", default=os.path.join(data_path, 'styles.csv'))
parser.add_argument("--autolaunch", action='store_true', help="open the webui URL in the system's default browser upon launch", default=False)
parser.add_argument("--electron", action='store_true', help="when --autolaunch is provided, open the webui URL as a standalone Electron app instead.", default=False)
parser.add_argument("--theme", type=str, help="launches the UI with light or dark theme", default=None)
parser.add_argument("--use-textbox-seed", action='store_true', help="use textbox for seeds in UI (no up/down, but possible to input long seeds)", default=False)
parser.add_argument("--disable-console-progressbars", action='store_true', help="do not output progressbars to console", default=False)
parser.add_argument("--enable-console-prompts", action='store_true', help="does not do anything", default=False)  # Legacy compatibility, use as default value shared.opts.enable_console_prompts
parser.add_argument('--vae-path', type=str, help='Checkpoint to use as VAE; setting this argument disables all settings related to VAE', default=None)
parser.add_argument("--disable-safe-unpickle", action='store_true', help="disable checking pytorch models for malicious code", default=False)
parser.add_argument("--api", action='store_true', help="use api=True to launch the API together with the webui (use --nowebui instead for only the API)")
parser.add_argument("--api-auth", type=str, help='Set authentication for API like "username:password"; or comma-delimit multiple like "u1:p1,u2:p2,u3:p3"', default=None)
parser.add_argument("--api-log", action='store_true', help="use api-log=True to enable logging of all API requests")
parser.add_argument("--nowebui", action='store_true', help="use api=True to launch the API instead of the webui")
parser.add_argument("--ui-debug-mode", action='store_true', help="Don't load model to quickly launch UI")
parser.add_argument("--device-id", type=str, help="Select the default CUDA device to use (export CUDA_VISIBLE_DEVICES=0,1,etc might be needed before)", default=None)
parser.add_argument("--administrator", action='store_true', help="Administrator rights", default=False)
parser.add_argument("--cors-allow-origins", type=str, help="Allowed CORS origin(s) in the form of a comma-separated list (no spaces)", default=None)
parser.add_argument("--cors-allow-origins-regex", type=str, help="Allowed CORS origin(s) in the form of a single regular expression", default=None)
parser.add_argument("--tls-keyfile", type=str, help="Partially enables TLS, requires --tls-certfile to fully function", default=None)
parser.add_argument("--tls-certfile", type=str, help="Partially enables TLS, requires --tls-keyfile to fully function", default=None)
parser.add_argument("--disable-tls-verify", action="store_false", help="When passed, enables the use of self-signed certificates.", default=None)
parser.add_argument("--server-name", type=str, help="Sets hostname of server", default=None)
parser.add_argument("--gradio-queue", action='store_true', help="does not do anything", default=True)
parser.add_argument("--no-gradio-queue", action='store_true', help="Disables gradio queue; causes the webpage to use http requests instead of websockets; was the defaul in earlier versions")
parser.add_argument("--skip-version-check", action='store_true', help="Do not check versions of torch and xformers")
parser.add_argument("--no-hashing", action='store_true', help="disable sha256 hashing of checkpoints to help loading performance", default=False)
parser.add_argument("--no-download-sd-model", action='store_true', help="don't download SD1.5 model even if no model is found in --ckpt-dir", default=False)
parser.add_argument('--subpath', type=str, help='customize the subpath for gradio, use with reverse proxy')
parser.add_argument('--add-stop-route', action='store_true', help='does not do anything')
parser.add_argument('--api-server-stop', action='store_true', help='enable server stop/restart/kill via api')
parser.add_argument('--timeout-keep-alive', type=int, default=30, help='set timeout_keep_alive for uvicorn')
parser.add_argument("--disable-all-extensions", action='store_true', help="prevent all extensions from running regardless of any other settings", default=False)
parser.add_argument("--disable-extra-extensions", action='store_true', help="prevent all extensions except built-in from running regardless of any other settings", default=False)
