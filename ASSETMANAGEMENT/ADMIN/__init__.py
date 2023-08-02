from tkinter import Tk
import signadmin

if __name__ == '__main__':
    # Create a root window for your application
    root = Tk()

    # Execute the code from the signadmin.py module
    signadmin.run(root)

    # Start the Tkinter event loop
    root.mainloop()
