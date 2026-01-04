from tkinter import *
from functions import NotesApp
import os

window: Tk = Tk()
notesapp: NotesApp = NotesApp( f'{ os.getcwd() }/notes.json' )

add_menu: Frame = Frame( window )
remove_menu: Frame = Frame( window )
show_all_menu: Frame = Frame( window )
read_menu: Frame = Frame( window )
update_menu: Frame = Frame( window )

def hide_menus() -> None:
    add_menu.pack_forget()
    remove_menu.pack_forget()
    show_all_menu.pack_forget()
    read_menu.pack_forget()
    update_menu.pack_forget()

    return

def check_is_int( n: str ) -> bool:
    try:
        if '-' not in str( n ):
            int( n )

            return True
        else:
            raise ValueError()
    except ValueError:
        return False

def ui() -> None:
    global window
    window.geometry( '800x500' )
    window.minsize( 800, 500 )

    notes_list: StringVar = StringVar( value=notesapp.show_all_notes() )

    # ADD NOTE MENU
    title_entry: Entry = Entry( add_menu, width=25, font=( 'Impact', 22 ) )
    text_entry: Entry = Entry( add_menu, width=25, font=( 'Impact', 22 ) )

    title_entry.insert( 0, f'Untitled #{ notesapp.number_of_notes() + 1 }' )
    text_entry.insert( 0, 'Text' )

    submit: Button = Button( add_menu, text='submit', font=( 'Impact', 12 ), command=lambda: ( notesapp.add_note( title_entry.get(), text_entry.get() ), title_entry.delete( 0, END ), text_entry.delete( 0, END ), title_entry.insert( 0, f'Untitled #{ notesapp.number_of_notes() + 1 }' ), text_entry.insert( 0, 'Text' ), notes_list.set( value=notesapp.show_all_notes() ) ) )
    
    title_entry.pack()
    text_entry.pack()
    submit.pack( pady=5 )

    # REMOVE NOTE MENU
    error: Label = Label( remove_menu, text='Incorrect ID.', fg='red', font=( 'Impact', 20, 'bold italic underline' ) )
    all_notes_remove: Label = Label( remove_menu, textvariable=notes_list, font=( 'Impact', 20 ) )
    
    id_entry: Entry = Entry( remove_menu, width=25, font=( 'Impact', 22 ) )
    id_entry.insert( 0, 'Id' )
    
    delete: Button = Button( remove_menu, text='Remove', font=( 'Impact', 12 ), command=lambda: ( error.pack_forget(), notesapp.remove_note( int( id_entry.get() ) - 1 ) if check_is_int( id_entry.get() ) else error.pack(), id_entry.delete( 0, END ), id_entry.insert( 0, 'Id' ), notes_list.set( value=notesapp.show_all_notes() ) ) )

    all_notes_remove.pack()
    id_entry.pack()
    delete.pack( pady=5 )

    # SHOW ALL NOTES MENU
    all_notes_show: Label = Label( show_all_menu, textvariable=notes_list, font=( 'Impact', 20 ) )
    all_notes_show.pack()

    # READ NOTE MENU
    error2: Label = Label( read_menu, text='Incorrect ID.', fg='red', font=( 'Impact', 20, 'bold italic underline' ) )
    all_notes_read: Label = Label( read_menu, textvariable=notes_list, font=( 'Impact', 20 ) )

    id_entry2: Entry = Entry( read_menu, width=25, font=( 'Impact', 22 ) )
    id_entry2.insert( 0, 'Id' )

    note: Label = Label( read_menu, font=( 'Impact', 20 ) )

    read: Button = Button( read_menu, text='Read', font=( 'Impact', 12 ), command=lambda: ( error2.pack_forget(), note.config( text=notesapp.read_note( int( id_entry2.get() ) - 1 ) ) if check_is_int( id_entry2.get() ) else error2.pack(), id_entry2.delete( 0, END ), id_entry2.insert( 0, 'Id' ), notes_list.set( value=notesapp.show_all_notes() ) ) )

    all_notes_read.pack()
    id_entry2.pack()
    read.pack( pady=5 )
    note.pack()

    ###########################
    # MAIN

    top_label: Label = Label( window, text='Notefy', font=( 'Impact', 34, 'bold' ), bg='skyblue', relief=FLAT, bd=20 )
    top_label.pack( fill='x' )

    buttons_side: Frame = Frame( window )

    add_btn: Button = Button( buttons_side, width=15, text='Add Note', font=( 'Impact', 20 ), command=lambda: ( hide_menus(), add_menu.pack() ) )
    remove_btn: Button = Button( buttons_side, width=15, text='Remove Note', font=( 'Impact', 20 ), command=lambda: ( hide_menus(), remove_menu.pack() ) )
    show_all_btn: Button = Button( buttons_side, width=15, text='Show All Notes', font=( 'Impact', 20 ), command=lambda: ( hide_menus(), show_all_menu.pack() ) )
    read_btn: Button = Button( buttons_side, width=15, text='Read Note', font=( 'Impact', 20 ), command=lambda: ( hide_menus(), read_menu.pack() ) )
    update_btn: Button = Button( buttons_side, width=15, text='Update Note', font=( 'Impact', 20 ), command=lambda: ( hide_menus(), update_menu.pack() ) )

    add_btn.pack( pady=5 )
    remove_btn.pack( pady=5 )
    show_all_btn.pack( pady=5 )
    read_btn.pack( pady=5 )
    update_btn.pack( pady=5 )
    
    buttons_side.pack( side='left', fill='y' )

    window.mainloop()
