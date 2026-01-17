from tkinter import *
from tkinter import messagebox
from backend import NotesApp

notesapp: NotesApp = NotesApp()

window: Tk = Tk()

add_menu: Frame = Frame( window )
remove_menu: Frame = Frame( window )
update_menu: Frame = Frame( window )
read_menu: Frame = Frame( window )
show_all_menu: Frame = Frame( window )

def hide_menus() -> None:
    add_menu.pack_forget()
    remove_menu.pack_forget()
    update_menu.pack_forget()
    read_menu.pack_forget()
    show_all_menu.pack_forget()

    return

def is_int( n: str ) -> bool:
    try:
        int( n )
        return True
    except ValueError:
        return False

colors: dict = {
    'light': {
        'bg': 'lightgrey',
        'fg': 'black',
        'logo': 'skyblue',
        'buttons': 'lightgrey'
    },
    'dark': {
        'bg': 'black',
        'fg': 'white',
        'logo': 'darkblue',
        'buttons': '#0D1A45'
    },
    'nature': {
        'bg': '#36FF2B',
        'fg': 'black',
        'logo': 'darkgreen',
        'buttons': '#41CC44'
    },
    'sky': {
        'bg': '#32CDE6',
        'fg': 'black',
        'logo': '#2957FF',
        'buttons': '#456FFF'
    }
}

bg: StringVar = StringVar( value='' )
fg: StringVar = StringVar( value='' )
logo: StringVar = StringVar( value='' )
buttons: StringVar = StringVar( value='' )

def set_color() -> None:
    color: str = notesapp.get_color()

    bg.set( value=colors[ color ][ 'bg' ] )
    fg.set( value=colors[ color ][ 'fg' ] )
    logo.set( value=colors[ color ][ 'logo' ] )
    buttons.set( value=colors[ color ][ 'buttons' ] )

    return
    
def ui() -> None:
    set_color()

    # GLOBAL VARS
    fonts: tuple = ( 'Impact', 18 )
    default_title: StringVar = StringVar( value=f'Untitled #{ notesapp.get_notes_num() }' )
    error: list = [ 'Invalid ID', ( *fonts, 'bold italic underline' ), 'red' ]
    note: StringVar = StringVar( value='' )
    notes: StringVar = StringVar( value=notesapp.show_all() )

    global window
    global add_menu, remove_menu, update_menu, read_menu, show_all_menu

    window.configure( bg=bg.get() )
    add_menu.configure( bg=bg.get() )
    remove_menu.configure( bg=bg.get() )
    update_menu.configure( bg=bg.get() )
    read_menu.configure( bg=bg.get() )
    show_all_menu.configure( bg=bg.get() )

    # WINdOW SETUP
    window.geometry( '1000x700' )
    window.minsize( 1000, 700 )

    # TOP LOGO
    top_label: Label = Label( window, text='Notefy', font=( 'Impact', 26, 'bold' ), fg=fg.get(), bg=logo.get(), relief=FLAT, bd=14 )
    top_label.pack( fill='x' )

    # FRAME THAT HOLDS ALL THE BUTTONS TO OPEN THE MENUS
    buttons_side: Frame = Frame( window, bg=bg.get() )

    add_button: Button = Button( buttons_side, text='Add Note', fg=fg.get(), bg=buttons.get(), font=fonts, width=25, command=lambda: ( hide_menus(), add_menu.pack() ) )
    remove_button: Button = Button( buttons_side, text='Remove Note', fg=fg.get(), bg=buttons.get(), font=fonts, width=25, command=lambda: ( hide_menus(), remove_menu.pack() ) )
    update_button: Button = Button( buttons_side, text='Update Note', fg=fg.get(), bg=buttons.get(), font=fonts, width=25, command=lambda: ( hide_menus(), update_menu.pack() ) )
    read_button: Button = Button( buttons_side, text='Read Note', fg=fg.get(), bg=buttons.get(), font=fonts, width=25, command=lambda: ( hide_menus(), read_menu.pack() ) )
    show_all_button: Button = Button( buttons_side, text='Show All Note', fg=fg.get(), bg=buttons.get(), font=fonts, width=25, command=lambda: ( hide_menus(), show_all_menu.pack() ) )

    add_button.pack( pady=5 )
    remove_button.pack( pady=5 )
    update_button.pack( pady=5 )
    read_button.pack( pady=5 )
    show_all_button.pack( pady=5 )

    buttons_side.pack( side='left', fill='y' )

    # -------------------------------------------------------------------- # 
    # ADD MENU 
    title_entry: Entry = Entry( add_menu, font=fonts, width=35, textvariable=default_title )
    text_entry : Entry = Entry( add_menu, font=fonts, width=35 )

    text_entry.insert( 0, 'Text' )

    submit: Button = Button( add_menu, text='Add', fg=fg.get(), bg=buttons.get(), font=fonts, command=lambda: (
        notesapp.add( title_entry.get().strip() if title_entry.get().replace( ' ', '' ) != '' else f'Untitled #{ notesapp.get_notes_num() }', text_entry.get().strip() ),
        title_entry.delete( 0, END ),
        text_entry.delete(  0, END ),
        default_title.set( value=f'Untitled #{ notesapp.get_notes_num() }' ),
        text_entry.insert( 0, 'Text' ),
        notes.set( value=notesapp.show_all() )
    ) )

    title_entry.pack()
    text_entry.pack()
    submit.pack( pady=5 )

    # REMOVE MENU
    remove_error: Label = Label( remove_menu, text=error[ 0 ], font=error[ 1 ], fg=error[ 2 ], bg=bg.get() )

    remove_id_entry: Entry = Entry( remove_menu, font=fonts, width=35 )
    remove_id_entry.insert( 0, 'Id' )

    remove: Button = Button( remove_menu, text='Remove', fg=fg.get(), bg=buttons.get(), font=fonts, command=lambda: (
        remove_error.pack_forget(),
        notesapp.remove( int( remove_id_entry.get().replace( ' ', '' ) ) ) if is_int( remove_id_entry.get().replace( ' ', '' ) ) and int( remove_id_entry.get().replace( ' ', '' ) ) <= notesapp.get_notes_num() else remove_error.pack(),
        remove_id_entry.delete( 0, END ),
        remove_id_entry.insert( 0, 'Id' ),
        default_title.set( value=f'Untitled #{ notesapp.get_notes_num() }' ),
        notes.set( notesapp.show_all() )
    ) )

    remove_all: Button = Button( remove_menu, text='Remove All', fg=fg.get(), bg=buttons.get(), font=fonts, command=lambda: (
        notesapp.remove_all() if messagebox.askyesno( title='Remove all notes', message='Do you really want to remove all the existing notes?', icon='warning' ) else ...,
        notes.set( value=notesapp.show_all() )
    ) )

    remove_id_entry.pack()
    remove.pack( pady=5 )
    remove_all.pack( pady=15 )

    # UPDATE MENU
    update_error: Label = Label( update_menu, text=error[ 0 ], font=error[ 1 ], fg=error[ 2 ], bg=bg.get() )

    update_id_entry: Entry = Entry( update_menu, font=fonts, width=35 )
    update_title_entry: Entry = Entry( update_menu, font=fonts, width=35 )
    update_text_entry : Entry = Entry( update_menu, font=fonts, width=35 )

    update_id_entry.insert( 0, 'Id' )
    update_title_entry.insert( 0, '(leave empty to not change)' )

    update: Button = Button( update_menu, text='Update', fg=fg.get(), bg=buttons.get(), font=fonts, command=lambda: (
        update_error.pack_forget(),
        notesapp.update( int( update_id_entry.get().replace( ' ', '' ) ), update_title_entry.get().strip() if update_title_entry.get().replace( ' ', '' ) != '' else None, update_text_entry.get().strip() ) if is_int( update_id_entry.get().replace( ' ', '' ) ) and int( update_id_entry.get().replace( ' ', '' ) ) <= notesapp.get_notes_num() else update_error.pack(),
        update_id_entry.delete( 0, END ),
        update_title_entry.delete( 0, END ),
        update_text_entry.delete(  0, END ),
        update_id_entry.insert( 0, 'Id' ),
        update_title_entry.insert( 0, '(leave empty to not change)' ),
        notes.set( value=notesapp.show_all() )
    ) )

    update_id_entry.pack()
    update_title_entry.pack()
    update_text_entry.pack()
    update.pack( pady=5 )

    # READ MENU
    read_error: Label = Label( read_menu, text=error[ 0 ], font=error[ 1 ], fg=error[ 2 ], bg=bg.get() )

    note_label: Label = Label( read_menu, textvariable=note, font=fonts, wraplength=600, fg=fg.get(), bg=bg.get() )

    read_id_entry: Entry = Entry( read_menu, font=fonts, width=35 )
    read_id_entry.insert( 0, 'Id' )

    read: Button = Button( read_menu, text='Read', fg=fg.get(), bg=buttons.get(), font=fonts, command=lambda: (
        read_error.pack_forget(),
        ( note.set( notesapp.read( int( read_id_entry.get().replace( ' ', '' ) ) ) ), note_label.pack() ) if is_int( read_id_entry.get().replace( ' ', '' ) ) and int( read_id_entry.get().replace( ' ', '' ) ) <= notesapp.get_notes_num() else ( read_error.pack(), note_label.pack_forget() ),
        read_id_entry.delete( 0, END ),
        read_id_entry.insert( 0, 'Id' )
    ) )

    read_id_entry.pack()
    read.pack( pady=5 )
    note_label.pack()

    # SHOW ALL MENU
    notes_label: Label = Label( show_all_menu, textvariable=notes, font=fonts, fg=fg.get(), bg=bg.get() )

    notes_label.pack()

    # START WINDOW
    window.mainloop()
