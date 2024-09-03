option={}
f=open(r'c:\windows\win.ini')
for line in f:
    if line.startswith(';'):
        continue
    if line.startswith('['):
        iterm=[]
        name=line[1:line.rfind(']')]
        option.setdefault(name,iterm)
        continue
    if '='in line:
        option[name].append(line.strip())
print(option)