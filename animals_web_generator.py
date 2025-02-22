import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)

animals_data = load_data('animals_data.json')
#print(animals_data)

output = ""
for animal in animals_data:
    name = animal.get('name')
    if name is not None:
        output = output + f"Name: {name}\n"

    diet = animal.get('characteristics').get('diet')
    if diet is not None:
        output = output + f"Diet: {diet}\n"

    locations = animal.get('locations')
    if locations is not None and len(locations) != 0:
        location = locations[0]
        output = output + f"Location: {location}\n"

    animal_type = animal.get('characteristics').get('type')
    if animal_type is not None:
        output = output + f"Type: {animal_type}\n"

print(output)



try:
    with open("animals_template.html", "r") as handle:
        template_data = handle.read()
except FileNotFoundError:
    print("The file was not found.")


new_data = template_data.replace("__REPLACE_ANIMALS_INFO__", output)

print(new_data)

with open("animals.html", "w") as handle:
    handle.write(new_data)


