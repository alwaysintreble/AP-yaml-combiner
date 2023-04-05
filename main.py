from tkinter import Tk, filedialog, messagebox


root = Tk()
root.withdraw()

messagebox.showinfo(title="File Selection", message="Select all files that you would like to combine. "
                                                    "Pressing ctrl while clicking will allow multiple selections.")
files = filedialog.askopenfilenames(title="File Selection", filetypes=(("yaml files", "*.yaml"),), defaultextension="yaml")

messagebox.showinfo(title="Output Selection", message="Select file to save this as.")
output = filedialog.asksaveasfilename(confirmoverwrite=True, defaultextension="yaml", title="Output File", filetypes=(("yaml files", "*.yaml"),))

with open(output, 'wt') as main_data:
    main_data.write('\n---\n\n'.join(open(file, 'rt').read() for file in files))

messagebox.showinfo(title="Complete", message=f"Process complete. All yaml files have been compiled into {output}.")
