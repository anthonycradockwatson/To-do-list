import customtkinter as ctk
if __name__ == '__main__':
    # Initialize the main window
    top = ctk.CTk()
    top.geometry("250x600")
    button = "#1e231e"
    background = "#23283c"
    checkbox = "#C4DAD2"
    button_hover = "#2d3028"
    top.configure(fg_color = background)
    # Add a label
    label = ctk.CTkLabel(top, text="To do list", width=150,height=35, corner_radius=5, fg_color= "#192328")
    label.pack(pady=10, padx=10)
    # Function to add a new checkbox
    def add_checkbox():
        def hide_checkbox():
            if check_var.get() == 1:
                new_checkbox.pack_forget()
        def close_and_get_text():
            nonlocal checkbox_text
            checkbox_text = goal.get()
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
        new_checkbox = ctk.CTkCheckBox(top, text=checkbox_text, variable=check_var, command=hide_checkbox, hover_color=checkbox, border_color="#959eab")
        new_checkbox.pack(pady=5, padx = 1)
    # Add button to trigger checkbox creation
    add_button = ctk.CTkButton(top, text="Add a point", command=add_checkbox, fg_color= button, hover_color=button_hover)
    add_button.pack(pady=10)
    # Start the main loop
    top.mainloop()
