import os
import sys
import re



os.chdir(sys.argv[1].replace("\"", ""))
print(os.getcwd())
ns = []
file = []
name, ext = os.path.splitext(os.listdir()[0])
name = re.sub("[\(\[].*?[\)\]]", "", name)
for n in name.split("-"):
    n = os.path.splitext(n)[0].strip()
    n = n.replace("_", "")
    file.append(n)
    ns.append(input("\""+n+"\" "+"Title, Number, Or Episode? (t, n, e): "))
filename = file[ns.index("t")].strip()+"-"+file[ns.index("n")].strip()
if "e" in ns:
    filename += "-"+file[ns.index("e")].strip()
filename += ext
print(filename)
r = input("Is this Correct? (Yes/No): ")

if r.upper().startswith("Y"):
    for f in os.listdir():
        file = []
        file = []
        name = re.sub("[\(\[].*?[\)\]]", "", f)
        for n in name.split("-"):
            n = os.path.splitext(n)[0].strip()
            n = re.sub("[\(\[].*?[\)\]]", "", n).strip()
            n = n.replace("_", "")
            file.append(n)
        filename = file[ns.index("t")].strip()+"-"+file[ns.index("n")].strip()
        if "e" in ns:
            filename += "-"+file[ns.index("e")].strip()
        filename += ext
        print(filename)
        os.rename(f, filename)
