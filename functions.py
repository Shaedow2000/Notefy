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

    def add_note( self, title: str, text: str ) -> None:
        if title.replace( ' ', '' ) == '':
            title = f"Untitled #{ len( self.data[ 'notes' ] ) }"

        new_note: dict = { 
            'id': len( self.data[ 'notes' ] ),
            'title': title,
            'text': text
        }

        self.data[ 'notes' ].append( new_note )

        return

    def remove_note( self, id: int ) -> None:
        for i in range( len( self.data[ 'notes' ] ) ):
            if self.data[ 'notes' ][ i ][ 'id' ] == id:
                self.data[ 'notes' ].pop( i )

        return

    def show_all_notes( self ) -> None:
        pass

    def read_note( self ) -> None:
        pass

    def update_note( self ) -> None:
        pass
