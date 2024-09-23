import customtkinter as ctk
import sqlite3
con=sqlite3.connect("to_do_list.db")
sql=con.cursor()
    # Initialize the main window
top = ctk.CTk()
top.geometry("250x600")
button = "#1e231e"
background = "#23283c"
checkbox = "#C4DAD2"
button_hover = "#2d3028"
rowid=1
check_num=1
new_checkbox={}
top.configure(fg_color = background)
    # Add a label
label = ctk.CTkLabel(top, text="To do list", width=150,height=35, corner_radius=5, fg_color= "#192328")
label.pack(pady=10, padx=10)
    # Function to add a new checkbox
sql.execute("CREATE TABLE IF NOT EXISTS to_do_list( Task text)")
def hide_checkbox(task_text, checkbox, check_var):
        # This function is used for handling checkbox click events
    if check_var.get() == 1:
        sql.execute("SELECT rowid FROM to_do_list WHERE task = ?", (task_text,))
        thing=sql.fetchone()
        thing=int(thing[0])
        print(thing)
        sql.execute("DELETE FROM to_do_list WHERE Task = ?", (task_text,))
        checkbox[f"{thing}"].forget()
        con.commit()
def add_checkbox():
    def close_and_get_text():
        nonlocal checkbox_text
        checkbox_text = goal.get()
            # Function to save to sql database
        sql.execute("INSERT INTO to_do_list (Task) VALUES(?)", (checkbox_text,))
        con.commit()
        title.destroy()
        # Create a temporary window for user input
    title = ctk.CTkToplevel(top)
    title.geometry("300x100")
    title.configure(fg_color = background)
    checkbox_text = "New Task"
    goal = ctk.CTkEntry(title, placeholder_text="What would you like the checkbox to say?", width= 250, fg_color="#141829")
    goal.pack(pady=15)
        # Button to close the window and use the entered text
    clear = ctk.CTkButton(title, text="Finish", command=close_and_get_text,
                     corner_radius=16, fg_color= button, hover_color=button_hover)
    clear.pack(pady=0)
    title.wait_window(title)
    # Create the checkbox with the user-provided text
    check_var = ctk.IntVar()
    new_checkbox[f"{rowid}"] = ctk.CTkCheckBox(top, text=checkbox_text, variable=check_var, onvalue=1, offvalue=0,
                                                command=lambda t=checkbox_text, v=check_var: hide_checkbox(t, new_checkbox, v),
                                                hover_color=checkbox, border_color="#959eab")
    new_checkbox[f"{rowid}"].pack(pady=5, padx=1)
    # Add button to trigger checkbox creation
add_button = ctk.CTkButton(top, text="Add a point", command=add_checkbox, fg_color= button, hover_color=button_hover)
add_button.pack(pady=10)
def kill():
    con.close()
    top.destroy()
end = ctk.CTkButton(top, text="All done", command = kill, fg_color= button, hover_color=button_hover)
end.pack(pady=10)
sql.execute("SELECT rowid, task FROM to_do_list")
rows = sql.fetchall()
    # Print existing tasks
if rows:
    for row in rows:
        rowid, task = row
        check_var = ctk.IntVar()
        new_checkbox[f"{rowid}"] = ctk.CTkCheckBox(top, text=task, variable=check_var,onvalue=1,offvalue=0,
                                        command=lambda t=task, v=check_var: hide_checkbox(t, new_checkbox, v),
                                        hover_color=checkbox, border_color="#959eab")
        new_checkbox[f"{rowid}"].pack(pady=5, padx=1)
  # Start the main loop
con.commit()
top.mainloop()
