import os
import subprocess

def get_gedit_pid():
    try:
        ps_output = subprocess.check_output(['ps', 'aux'], universal_newlines=True)
        grep_output = subprocess.check_output(['grep', 'gedit'], input=ps_output, universal_newlines=True)

        lines = grep_output.strip().split('\n')
        if lines:
            first_line = lines[0].split()
            gedit_pid = int(first_line[1])
            return gedit_pid
        else:
            return None
    except subprocess.CalledProcessError:
        return None

def show_link(links=[],destroy=False):
    if destroy:
        pid = get_gedit_pid()
        os.system(f"kill -9 {pid}")
    else:
        pid = get_gedit_pid()
        try:
            os.system(f"kill -9 {pid}")
        except:
            pass
        n = 1
        with open("links.txt",mode="w") as file:
            for i in links:
                file.write(f"{n}: {i} \n")
                n += 1
            file.close()
        os.system("open links.txt")