import ipywidgets as widgets
from ipywidgets import HBox, VBox
from IPython.display import display, clear_output

user_input = widgets.Text(placeholder = 'Full Name', description = "User:")
load_button = widgets.Button(description="Enter", button_style="success")
date = widgets.DatePicker(description = 'Pick a Date')
tasks = widgets.SelectMultiple(description = 'Tasks', options = [])
add_button = widgets.Button(description="Add Task")
edit_button = widgets.Button(description="Edit Task")
delete_button = widgets.Button(description="Remove Task")

structured_ui = widgets.VBox([
        widgets.HBox([user_input, load_button]),
        date, tasks,
        widgets.HBox([add_button, edit_button, delete_button])
    ])

display(structured_ui)