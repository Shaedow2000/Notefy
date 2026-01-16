import sys
from ui import ui

# call the ui function
def main() -> None:
    ui()

# start execution
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit( 'Exiting...' )
