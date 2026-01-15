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

    def add( self ) -> None:
        pass

    def remove( self ) -> None:
        pass

    def remove_all( self ) -> None:
        pass

    def update( self ) -> None:
        pass

    def read( self ) -> None:
        pass

    def show_all( self ) -> None:
        pass
