import pathlib, os, sys
from replace_distribution import iter
from random import seed, sample
import time
import tkinter as tk
from gui import GUI

if __name__ == "__main__":
    is_cmd = sys.argv[1] == "cmd"
    is_gui = sys.argv[1] == "gui"

    if is_cmd:
        print("CMD detected... Running command line...")
        SCRIPT_ROOT = str(pathlib.Path.home())
        try:
            if sys.frozen or sys.importers:
                SCRIPT_ROOT = os.path.dirname(sys.executable)
        except AttributeError:
            SCRIPT_ROOT = os.path.dirname(os.path.realpath(__file__))


        file_name = os.path.join("input_files", sys.argv[2])

        file_route = os.path.join(SCRIPT_ROOT, file_name)

        pcnt = float(sys.argv[3])
        output_num = int(sys.argv[4])
        
        try:
            is_lower = sys.argv[5] == "true"
        except:
            is_lower = False

        f = open(file_route, 'r')
        txt = f.read()
        f.close()

        print("Beginning text operation...")

        start = time.time()

        outputs = iter(output_num, pcnt, txt, is_lower=is_lower)

        print(f"Done text operation in {time.time() - start}")

                          
        output_path = os.path.join(sys.argv[6], f"{sys.argv[2].replace('.txt', '')}_output.txt")
        f_output = open(output_path, "w")
        f_output.write("\n".join(outputs))
        f_output.close()
        
        print(f"File saved in {output_path}")

        os.system('pause')

    elif is_gui:
        window = tk.Tk()
        
        gui = GUI(window)

        window.mainloop()
        





