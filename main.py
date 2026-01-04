import sys
from gui import ui

def main() -> None:
    ui() 

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit( 1 )
