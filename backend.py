import json, os

# Backend code of the app
class NotesApp:
    def __init__( self ) -> None:
        # Name of the file
        self.file: str = 'notes.json'
        # Data that is inside the file
        self.data: dict = {}

        # Check if the file exists
        self.create_json_file()

        # retrieve data from file
        with open( self.file, 'r' ) as file:
            self.data = json.load( file )

    # Create file if not found
    def create_json_file( self ) -> None:
        if not os.path.exists( self.file ):
            with open( self.file, 'w' ) as file:
                json.dump( { 'notes': [] }, file )

    # Reweites all the file with new data ( overwriting )
    def rewrite_json( self, data: dict ) -> None:
        with open( self.file, 'w' ) as file:
            json.dump( data, file )

        return

    # Rewrite the ids in in order, from 0 to the index of the last note 
    def rewrite_ids( self ) -> None:
        for i in range( self.data[ 'notes' ] ):
            self.data[ 'notes' ][ i ][ 'id' ] = i

        return

    # Get the number of notes 
    def get_notes_num( self ) -> int:
        return len( self.data[ 'notes' ] ) 

    # Create a new note
    def add( self, title: str, text: str ) -> None:
        note: dict = {
            'id': self.get_notes_num(),
            'title': title,
            'text': text
        }

        self.data[ 'notes' ].append( note )
        self.rewrite_json( self.data )

        return

    # Remove a note by its id
    def remove( self, id: int ) -> None:
        for i in range( self.data[ 'notes' ] ):
            if self.data[ 'notes' ][ i ][ 'id' ] == id:
                self.data[ 'notes' ].pop( i )
                break
        
        self.rewrite_json( self.data )
        self.rewrite_ids()

        return

    # Remove all the notes
    def remove_all( self ) -> None:
        self.data[ 'notes' ] = []

        self.rewrite_json( self.data )

        return

    # Update note title and/or text by id
    def update( self, id: int, new_title: str | None, new_text: str | None ) -> None:
        for i in range( self.data[ 'notes' ] ):
            if self.data[ 'notes' ][ i ][ 'id' ] == id:
                if new_title != None:
                    self.data[ 'notes' ][ i ][ 'title' ] = new_title

                if new_text != None:
                    self.data[ 'notes' ][ i ][ 'text' ] = new_text

                break

        self.rewrite_json( self.data )
        return

    # Read the title and text of a note by its id
    def read( self, id: int ) -> str:
        note: dict = {}
        for i in range( self.data[ 'notes' ] ):
            if self.data[ 'notes' ][ i ][ 'id' ] == id:
                note = self.data[ 'notes' ][ i ]

        return f'================ Note { note[ "id" ] } ================\n\nTitle: { note[ "title" ] }\n\nText: { note[ "text" ] }'

    # Show all the existing notes titles 
    def show_all( self ) -> str:
        notes_titles: str = ''
        for i in range( self.data[ 'notes' ] ):
            if i % 2:
                notes_titles += f'{ i }. { self.data[ "notes" ][ i ][ "title" ] }\n'
            else:
                notes_titles += f'{ i }. { self.data[ "notes" ][ i ][ "title" ] }\t|\t'

        return notes_titles if notes_titles.replace( ' ', '' ) != '' else 'No notes found\n\n:('
