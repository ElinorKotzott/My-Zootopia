import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)

animals_data = load_data('animals_data.json')
print(animals_data)


for animal in animals_data:
    print()
    name = animal.get('name')
    if name is not None:
        print("Name: ", name)

    diet = animal.get('characteristics').get('diet')
    if diet is not None:
        print("Diet: ", diet)

    locations = animal.get('locations')
    if locations is not None and len(locations) != 0:
        location = locations[0]
        print("Location: ", location)

    animal_type = animal.get('characteristics').get('type')
    if animal_type is not None:
        print("Type: ", animal_type)





