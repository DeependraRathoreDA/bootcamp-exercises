import json
def search(usr_input):
    value = "No meaning found of given word."
    a = False
    for key, meaning in data.items():
        if usr_input.lower() == key:
            value = meaning
            a = True
        elif usr_input.title() == key:
            value = meaning
            a = True
        elif usr_input.capitalize() == key:
            value = meaning
            a = True
    return a, value
file = open('data.json',"r")
data = json.loads(file.read())
usr_input = input('Enter word to Search in Dictionary: ')
a, output = search(usr_input)
if a == True:
    for item in output:
        print( "==>> "+ item)
else:
    print(output)
