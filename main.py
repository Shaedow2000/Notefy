import sys, os
from ui import ui

if not os.path.exists( 'notes.json' ):
    with open( 'notes.json', 'w' ) as file:
        json.dump( { 'notes': [] }, file )

def main() -> None:
    pass

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit( 'Exiting...' )
