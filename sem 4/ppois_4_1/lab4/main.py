import sys
from controller import Controller

if __name__ == "__main__":
    ct = Controller()
    if (len(sys.argv) <= 1):
        ct.run_web()

    if sys.argv[1] == "cli":
        ct.run_cli()
    else:
        ct.run_web()
