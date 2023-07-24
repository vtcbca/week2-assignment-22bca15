n=input("Enter string :")
new=""
for i in range(len(n)):
    if i%2!=0:
        new+=n[i]
    else:
        new+=str(i)
print(new)
