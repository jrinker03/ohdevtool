import os
import sys
from ohdevtool.ehutils import getCoreFromConfig, runEsphomeGenerate

def modify_platformio_ini(build_path):
    print(f"Updating platformio.ini in {build_path}.")
    file = os.path.join(build_path, "platformio.ini")
    try:
        with open(file, 'r') as f:
            data = f.read()
    except FileNotFoundError:
        print(f"Error: file '{file}' not found")
        sys.exit(1)

    # Replace the platform and platform_packages lines with the latest platform package version
    substring_to_remove = "platform = https://github.com/pioarduino/platform-espressif32.git#51.03.07\nplatform_packages =\n    pioarduino/framework-espidf@https://github.com/pioarduino/esp-idf/releases/download/v5.1.5/esp-idf-v5.1.5.zip\n    espressif/toolchain-esp32ulp@2.35.0-20220830"

    # See https://registry.platformio.org/platforms/platformio/espressif32 for the latest platform package version
    data = data.replace(substring_to_remove, "platform = platformio/espressif32@^6.10.0")

    with open(file, 'w') as f:
        f.write(data)


def modify_helpers_cpp(build_path):
    print(f"Updating helpers.cpp in {build_path}.")
    file = os.path.join(build_path, "src/esphome/core/helpers.cpp")
    try:
        with open(file, 'r') as f:
            data = f.read()
    except FileNotFoundError:
        print(f"Error: file '{file}' not found")
        sys.exit(1)
    
    data = data.replace("#include \"esp32/rom/crc.h\"", "#include \"esp32s3/rom/crc.h\"")
    with open(file, 'w') as f:
        f.write(data)


def build(args):
    print(f"Building {args.configuration}")

    # Step 1: Run esphome to generate source files
    if(runEsphomeGenerate(args.configuration)!=0):
        exit(1)
    
    # Step 2: Modify the platformio.ini file to use the latest platformio/espressif32 platform library
    CORE = getCoreFromConfig(args.configuration)
    modify_platformio_ini(CORE.build_path)

    # Step 3: Modify the helpers.cpp file to use the correct crc.h file
    if CORE.data['esp32']['variant'] == 'ESP32S3':
        modify_helpers_cpp(CORE.build_path)

    # Step 4: Run platformio to build the project
    os.chdir(CORE.build_path)
    os.system("platformio run --environment " + CORE.name)
