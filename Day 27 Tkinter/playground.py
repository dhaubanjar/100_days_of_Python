import tkinter as tk

def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)

window = tk.Tk()
window.title("My First GUI Program")
window.minsize(500, 500)
window.config(padx=20, pady=20)

""" Label """
my_label = tk.Label(text= "I am a Legend", font=("Helvetica", 20, "bold") )
my_label.config(text="New Text")
my_label.grid(column=0, row=0)


""" Button """
button = tk.Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

new_button = tk.Button(text="New Button" )
new_button.grid(column=2, row=0)

""" Entry """
input = tk.Entry(width=10)
print(input.get())
input.grid(column=1, row=2)






window.mainloop()