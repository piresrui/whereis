from finder.cli_builder import get_parser
from finder.walker import run

if __name__ == "__main__":
    args = get_parser()
    run(src=args.path, pattern=args.pattern)
