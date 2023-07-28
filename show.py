import os
import subprocess

def show_link(links=[],destroy=False):
    if destroy:
        subprocess.call("TASKKILL /F /IM links.txt", shell=True)
    else:
        try:
            subprocess.call("TASKKILL /F /IM links.txt")
        except:
            pass
        n = 1
        with open("links.txt",mode="w") as file:
            for i in links:
                file.write(f"{n}: {i} \n")
                n += 1
            file.close()
        os.system("open links.txt")