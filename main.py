import sys
from ui import ui

def main() -> None:
    ui()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit( 'Exiting...' )
