def Merge(Dictionary1, Dictionary2, Dictionary3):
    Dictionary3.update(Dictionary2)
    Dictionary3.update(Dictionary1)
    return Dictionary3

#Creating a dictionary
exampleDictionary = {
    "FirstName" : "Luffy",
    "MiddleName" : "D",
    "LastName" : "Monkey"
}
print(exampleDictionary)

#Using update() function:
exampleDictionary.update({"FirstName": "Dragon"})
print(f"After using update() function: {exampleDictionary}")

#Using del function:
del exampleDictionary["FirstName"]
print(f"After del: {exampleDictionary}")

#Using clear() function:
exampleDictionary.clear()
print(f"After using clear() function: {exampleDictionary}\n")

#Creating a dictionary
exampleDictionary = {
    "FirstName" : "Luffy",
    "MiddleName" : "D",
    "LastName" : "Monkey",
    "Address" : "Dawn",
    "Pincode" : "12345"
}
print(exampleDictionary)

#Using popitem() function:
exampleDictionary.popitem()
print(f"After using popitem() function: {exampleDictionary}")

#Using pop() function:
exampleDictionary.pop("Address")
print(f"After using pop() function: {exampleDictionary}")

#Using get() function:
example = exampleDictionary.get("FirstName")
print(f"Using get() function: {example}")


#Using key() function:
example = exampleDictionary.keys()
print(f"Using get() function: {example}")


#Using values() function:
example = exampleDictionary.values()
print(f"Using get() function: {example}")

#Creating 3 dictionary
Dictionary1 = {
    "FirstName": "Levi",
    "LastName": "Ackerman"
}
Dictionary2 = {
    "FirstName1": "Mikasa",
    "LastName3": "Ackerman"
}
Dictionary3 = {
    "FirstName2": "Eren",
    "LastName2": "Yeagar"
}

#Merging 3 dictionaries using Merge() funcion:
print(f"Merged Dictionary: {Merge(Dictionary1, Dictionary2, Dictionary3)}")
#END of program
print("21DCE052")
