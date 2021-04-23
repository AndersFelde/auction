import os
import sys

arguments = sys.argv

if len(arguments) <= 2 or arguments[1].lower() == "h" or arguments[1].lower(
) == "help":
    print("rename.py 'original name' 'new name'")
    exit()

old = arguments[1].lower()
new = arguments[2].lower()

files = ["manage.py", f"{old}/wsgi.py", f"{old}/asgi.py", f"{old}/settings.py"]

for file in files:
    try:
        with open(f"./{old}/{file}", "r") as openFile:
            data = openFile.read()
    except:
        print("The old app-name was not found")
        exit()

    data = data.replace(old, new)

    with open(f"./{old}/{file}", "w") as openFile:
        openFile.write(data)
        print(f"Replaced in {file}")

os.rename(f"./{old}/{old}", f"./{old}/{new}")
os.rename(f"./{old}", f"./{new}")
print("Renamed directories")
