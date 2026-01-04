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

    def number_of_notes( self ) -> int:
        return len( self.data[ 'notes' ] )

    def add_note( self, title: str, text: str ) -> None:
        if title.replace( ' ', '' ) == '':
            title = f"Untitled #{ len( self.data[ 'notes' ] ) }"

        new_note: dict = { 
            'id': len( self.data[ 'notes' ] ),
            'title': title,
            'text': text
        }

        self.data[ 'notes' ].append( new_note )

        self.rewrite_json( self.data )

        return

    def remove_note( self, id: int ) -> None:
        for i in range( len( self.data[ 'notes' ] ) ):
            if self.data[ 'notes' ][ i ][ 'id' ] == id:
                self.data[ 'notes' ].pop( i )

                self.rewrite_json( self.data )

                break

        for i in range( len( self.data[ 'notes' ] ) ):
            self.data[ 'notes' ][ i ][ 'id' ] = i
            self.rewrite_json( self.data )

        return

    def show_all_notes( self ) -> str:
        notes: str = ''
        for i in range( len( self.data[ 'notes' ] ) ):
            notes += f'{ i + 1 }. { self.data[ 'notes' ][ i ][ 'title' ] }\n'

        return notes

    def read_note( self, id: int ) -> dict:
        note: dict = {}
        for i in range( len( self.data[ 'notes' ] ) ):
            if self.data[ 'notes' ][ i ][ 'id' ] == id:
                note = self.data[ 'notes' ][ i ]

        return note

    def update_note( self, id: int, new_title: str, new_text: str ) -> None:
        for i in range( len( self.data[ 'notes' ] ) ):
            if self.data[ 'notes' ][ i ][ 'id' ] == id:
                self.data[ 'notes' ][ i ][ 'title' ] = new_title
                self.data[ 'notes' ][ i ][ 'text' ] = new_text

        self.rewrite_json( self.data )
