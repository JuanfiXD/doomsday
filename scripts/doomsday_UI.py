import tkinter as tk

window = tk.Tk()
window.geometry("400x300")

menu_frame = tk.Frame(window)      # screen 1
trainer_frame = tk.Frame(window)   # screen 2

def show_frame(frame):
    frame.tkraise()                # bring this frame to the front

# put both frames in the same grid cell so they stack on top of each other
for frame in (menu_frame, trainer_frame):
    frame.grid(row=0, column=0, sticky="nsew")

# --- widgets go INTO the frames, note the first argument is the frame, not window ---
tk.Label(menu_frame, text="Welcome").pack()
tk.Button(menu_frame, text="Start", command=lambda: show_frame(trainer_frame)).pack()

tk.Label(trainer_frame, text="What day?").pack()
tk.Button(trainer_frame, text="Exit", command=lambda: show_frame(menu_frame)).pack()

show_frame(menu_frame)             # start on the menu
window.mainloop()