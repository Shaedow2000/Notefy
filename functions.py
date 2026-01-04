import json

class NotesApp:
    def __init__( self, dir: str ) -> None:
        self.dir: str = dir

        self.data: dict = {}
        with open( self.dir, 'r' ) as file:
            self.data = json.load( file )

    def rewrite_json( self, new_data: dict ) -> None:
        with open( self.dir, 'w' ) as file:
            json.dump( new_data, file, indent=4 )

        return

    def add_note( self ) -> None:
        pass

    def remove_note( self ) -> None:
        pass

    def show_all_notes( self ) -> None:
        pass

    def read_note( self ) -> None:
        pass

    def update_note( self ) -> None:
        pass
