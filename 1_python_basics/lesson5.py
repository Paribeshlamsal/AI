#file handling in python
#no copilot for this file
f=open("data.txt","r")
content=f.read()
print(content)
f.close()

f=open("a.txt","w")
f.write("Hello from file handling")
f.close()

f=open("data.txt","a")
f.write("\n New Line")
f.close()

f=open("data.txt","r")
for line in f:
    print(line.strip())
f.close()

with open("data.txt","r") as f:
    content=f.read()
    print(content)