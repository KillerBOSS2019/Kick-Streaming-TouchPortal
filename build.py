from TouchPortalAPI import tppbuild

PLUGIN_MAIN = "src/main.py"

PLUGIN_EXE_NAME = "tp_kick"

PLUGIN_EXE_ICON = r""

PLUGIN_ENTRY = PLUGIN_MAIN

PLUGIN_ENTRY_INDENT = 4

PLUGIN_ROOT = "kick"

PLUGIN_ICON = r""

OUTPUT_PATH = r"./"

PLUGIN_VERSION = "0.7.0"

ADDITIONAL_FILES = []

ADDITIONAL_PYINSTALLER_ARGS = [
    "--log-level=WARN",
    "--hidden-import=_cffi_backend",
    "--collect-all=curl_cffi"
]

ADDITIONAL_TPPSDK_ARGS = []

if __name__ == "__main__":
    tppbuild.runBuild()