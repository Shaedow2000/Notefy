from tkinter import *

def ui() -> None:
    window: Tk = Tk()
    window.geometry( '800x500' )
    window.minsize( 800, 500 )


    top_label: Label = Label( window, text='Notefy', font=( 'Impact', 34, 'bold' ), bg='skyblue', relief=FLAT, bd=20 )
    top_label.pack( fill='x' )

    buttons_side: Frame = Frame( window )

    add_btn: Button = Button( buttons_side, width=15, text='Add Note', font=( 'Impact', 20 ) )
    remove_btn: Button = Button( buttons_side, width=15, text='Remove Note', font=( 'Impact', 20 ) )
    show_all_btn: Button = Button( buttons_side, width=15, text='Show All Notes', font=( 'Impact', 20 ) )
    read_btn: Button = Button( buttons_side, width=15, text='Read Note', font=( 'Impact', 20 ) )
    update_btn: Button = Button( buttons_side, width=15, text='Update Note', font=( 'Impact', 20 ) )

    add_btn.pack( pady=5 )
    remove_btn.pack( pady=5 )
    show_all_btn.pack( pady=5 )
    read_btn.pack( pady=5 )
    update_btn.pack( pady=5 )
    
    buttons_side.pack( side='left', fill='y' )

    window.mainloop()
