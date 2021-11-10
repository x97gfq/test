
word = "Hello, World!"

for x in range(len(word)):
    for y in range(x):
        print(word[x-1], end = "")
    print("\n",end="")
    
#for letter in word:
#    print(letter)   
