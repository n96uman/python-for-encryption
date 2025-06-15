text=input("Enter your text :")
key=input("Enter the key word :")
hexa=""
n=0
for i in range(len(text)):
    num=ord(text[i])^ ord(key[n])
    n+=1
    if n>=len(key):
        n=0
    hexa+=hex(num)[2:]
print("the massage is encoded")
print(f"the cypher text is {hexa}")
with open("cypher","w") as cy:
    cy.write(hexa)
