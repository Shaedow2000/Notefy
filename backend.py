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

    def update( self, id: int, new_title: str, new_text: str ) -> None:
        for i in range( self.data[ 'notes' ] ):
            if self.data[ 'notes' ][ i ][ 'id' ] == id:
                if new_title != None:
                    self.data[ 'notes' ][ i ][ 'title' ] = new_title

                if new_text != None:
                    self.data[ 'notes' ][ i ][ 'text' ] = new_text

                break

        self.rewrite_json( self.data )
        return

    def read( self, id: int ) -> str:
        note: dict = {}
        for i in range( self.data[ 'notes' ] ):
            if self.data[ 'notes' ][ i ][ 'id' ] == id:
                note = self.data[ 'notes' ][ i ]

        return f'================ Note { note[ "id" ] } ================\n\nTitle: { note[ "title" ] }\n\nText: { note[ "text" ] }'

    def show_all( self ) -> str:
        notes_titles: str = ''
        for i in range( self.data[ 'notes' ] ):
            if i % 2:
                notes_titles += f'{ i }. { self.data[ "notes" ][ i ][ "title" ] }\n'
            else:
                notes_titles += f'{ i }. { self.data[ "notes" ][ i ][ "title" ] }\t|\t'

        return notes_titles if notes_titles.replace( ' ', '' ) != '' else 'No notes found\n\n:('
