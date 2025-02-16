import sys
import argparse
from ohdevtool.build import build

def parse_args(argv):
    parser = argparse.ArgumentParser(description='OpenHouse Development Tool')

    subparsers = parser.add_subparsers(help="Command to run:", dest="command", metavar="command")
    subparsers.required = True

    parser_compile = subparsers.add_parser("build", help="Invoke the build as indicated by the configuration file.")
    parser_compile.add_argument("configuration", help="The YAML file for the project.")

    parser_upload = subparsers.add_parser("upload", help="Upload the latest binary as indicated by the configuration file.")
    parser_upload.add_argument("configuration", help="The YAML file for the project.")

    parser_monitor = subparsers.add_parser("monitor", help="Connect to the device indicated by the configuration file and begin serial monitoring.")
    parser_monitor.add_argument("configuration", help="The YAML file for the project.")

    parser_run = subparsers.add_parser("run", help="Build, upload and monitor the project as indicated by the configuration file.")
    parser_run.add_argument("configuration", help="The YAML file for the project.")

    parser_test = subparsers.add_parser("test", help="Run the unit tests for the project.")
    parser_test.add_argument("configuration", help="The YAML file for the project.")

    return parser.parse_args(argv)

def main(argv=None):
    args = parse_args(argv)

    if args.command == "build":
        return build(args)
    else:
        print(f"Command '{args.command}' not implemented.")

    return 0


if __name__ == "__main__":
    sys.exit(main())