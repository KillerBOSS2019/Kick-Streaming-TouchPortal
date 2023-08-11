from TouchPortalAPI import tppbuild

PLUGIN_MAIN = "main.py"

PLUGIN_EXE_NAME = "tp_kick"

PLUGIN_EXE_ICON = r"kick.png"

PLUGIN_ENTRY = PLUGIN_MAIN

PLUGIN_ENTRY_INDENT = 4

PLUGIN_ROOT = "kick"

PLUGIN_ICON = r"kick.png"

OUTPUT_PATH = r"./"

PLUGIN_VERSION = "1.1.2"

ADDITIONAL_FILES = []

ADDITIONAL_PYINSTALLER_ARGS = [
    "--log-level=WARN",
    "--hidden-import=_cffi_backend",
    "--collect-all=curl_cffi"
]

ADDITIONAL_TPPSDK_ARGS = []

if __name__ == "__main__":
    tppbuild.runBuild()