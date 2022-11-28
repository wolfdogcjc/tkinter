import tkinter as tk

counter = 0 


def counter_label(label):
  counter = 0
  def count():
    global counter
    counter += 1
    label.config(text=str(counter))
    label.after(1000, count)
  count()
 
 
root = tk.Tk()

root.geometry("200x200")
 
# set minimum window size value
root.minsize(200, 200)
 
# set maximum window size value
root.maxsize(200, 200)

root.title("Stopwatch")
#changed title
label = tk.Label(root, fg="black")
#changed to black
label.config(font=("Courier", 44))
#made text bigger and changed font
label.pack()
counter_label(label)
button = tk.Button(root, fg="red",text='Stop', width=25, command=root.destroy)
#changed to red text (for stop)
button.pack()


root.mainloop()