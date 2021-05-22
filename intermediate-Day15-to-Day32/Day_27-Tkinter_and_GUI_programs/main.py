
import tkinter


window = tkinter.Tk()
window.minsize(500, 300)
window.title("My first GUI program")


my_label = tkinter.Label(text="I am a Label")
my_label.pack()


"""
    Change on screen text using button - Challenge
"""
def button_clicked():
    user_input = tk_input.get()
    my_label["text"] = user_input


button = tkinter.Button(text="Click Me", command=button_clicked)
button.pack()


tk_input = tkinter.Entry()
tk_input.pack()








window.mainloop()