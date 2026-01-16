from tkinter import *
from backend import NotesApp

notesapp: NotesApp = NotesApp()

window: Tk = Tk()

add_menu: Frame = Frame( window )
remove_menu: Frame = Frame( window )
update_menu: Frame = Frame( window )
read_menu: Frame = Frame( window )
show_all_menu: Frame = Frame( window )

def ui() -> None:
    # GLOBAL VARS
    fonts: tuple = ( 'Impact', 18 )

    window.geometry( '1000x700' )
    window.minsize( 1000, 700 )

    top_label: Label = Label( window, text='Notefy', font=( 'Impact', 26, 'bold' ), fg='black', bg='skyblue', relief=FLAT, bd=14 )
    top_label.pack( fill='x' )

    buttons_side: Frame = Frame( window )

    add_button: Button = Button( buttons_side, text='Add Note', font=fonts, width=25, command=lambda: ( add_menu.pack() ) )
    remove_button: Button = Button( buttons_side, text='Remove Note', font=fonts, width=25, command=lambda: ( remove_menu.pack() ) )
    update_button: Button = Button( buttons_side, text='Update Note', font=fonts, width=25, command=lambda: ( update_menu.pack() ) )
    read_button: Button = Button( buttons_side, text='Read Note', font=fonts, width=25, command=lambda: ( read_menu.pack() ) )
    show_all_button: Button = Button( buttons_side, text='Show All Note', font=fonts, width=25, command=lambda: ( show_all_menu.pack() ) )

    add_button.pack( pady=5 )
    remove_button.pack( pady=5 )
    update_button.pack( pady=5 )
    read_button.pack( pady=5 )
    show_all_button.pack( pady=5 )

    buttons_side.pack( side='left', fill='y' )

    window.mainloop()
