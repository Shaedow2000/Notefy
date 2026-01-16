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
    window.geometry( '1000x700' )
    window.minsize( 1000, 700 )

    top_label: Label = Label( window, text='Notefy', font=( 'Impact', 26, 'bold' ), fg='black', bg='skyblue', relief=FLAT, bd=14 )
    top_label.pack( fill='x' )

    window.mainloop()
