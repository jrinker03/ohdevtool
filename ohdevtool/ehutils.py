import os
import sys
from esphome.__main__ import run_esphome
from esphome.core import CORE
from esphome.config import read_config

def getCoreFromConfig(configPath):
    if not CORE.config_path:
        if not os.path.isfile(configPath):
            configPath = os.path.join(os.path.dirname(__file__), configPath)
        if not os.path.isfile(configPath):
            print(f"Error: config file '{configPath}' not found")
            sys.exit(1)

        CORE.config_path = configPath
        read_config({})
    return CORE

def getBuildPathFromConfig(configPath):
    return getCoreFromConfig(configPath).build_path

def runEsphomeGenerate(configPath):
    args = ["esphome", "compile", "--only-generate", configPath]
    return run_esphome(args)