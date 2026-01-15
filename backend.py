import json

class NotesApp:
    def __init__( self ) -> None:
        self.file: str = 'notes.json'
        self.data: dict = {}

        with open( self.file, 'r' ) as file:
            self.data = json.load( file )

    def rewrite_json( self, data: dict ) -> None:
        with open( self.file, 'w' ) as file:
            json.dump( data, file )

        return

    def rewrite_ids( self ) -> None:
        for i in range( self.data[ 'notes' ] ):
            self.data[ 'notes' ][ i ][ 'id' ] = i

        return

    def get_notes_num( self ) -> int:
        return len( self.data[ 'notes' ] ) 

    def add( self, title: str, text: str ) -> None:
        note: dict = {
            'id': self.get_notes_num(),
            'title': title,
            'text': text
        }

        self.data[ 'notes' ].append( note )
        self.rewrite_json( self.data )

        return

    def remove( self, id: int ) -> None:
        for i in range( self.data[ 'notes' ] ):
            if self.data[ 'notes' ][ i ][ 'id' ] == id:
                self.data[ 'notes' ].pop( i )
                break
        
        self.rewrite_json( self.data )
        self.rewrite_ids()

        return

    def remove_all( self ) -> None:
        self.data[ 'notes' ] = []

        self.rewrite_json( self.data )

        return

    def update( self ) -> None:
        pass

    def read( self ) -> None:
        pass

    def show_all( self ) -> None:
        pass
