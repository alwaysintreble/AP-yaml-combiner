from tkinter import Tk, filedialog, messagebox
from yaml import dump, safe_load


root = Tk()
root.withdraw()

messagebox.showinfo(title="Main File Selection", message="Select primary file for other yaml files to be appended to.")
origin = filedialog.askopenfilename()

messagebox.showinfo(title="Additional File Selection", message="Select all files that you would like to append to the "
                                                               "main file. pressing ctrl while clicking will allow "
                                                               "multiple selections.")
other_files = filedialog.askopenfilenames(title="Files to add to main file")

with open(origin, 'a') as main_data:
    for filename in other_files:
        main_data.write('\n---\n\n')
        with open(filename) as w:
            other_data = safe_load(w)
            dump(other_data, main_data)

messagebox.showinfo(title="Complete", message=f"Process complete. All yaml files have been compiled into {origin}.")
