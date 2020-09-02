import os

for f in os.scandir('packman/gui/ui'):
    basename = f.name.strip('.ui')
    os.system(f"pyuic5 packman/gui/ui/{f.name} -o packman/gui/{basename}.py")
