s=input("Enter a string\n")
vowels=set("aeiouAEIOU")
#print(vowels)
l=[]
for i in s:
    if i in vowels:
        l.append(i)
print("vowels in given string are",l)

    
