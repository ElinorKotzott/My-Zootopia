import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)

animals_data = load_data('animals_data.json')


output = ""
for animal in animals_data:
    output = output + "<li class='cards__item'>"
    name = animal.get('name')
    if name is not None:
        #ensuring the apostrophe will be depicted correctly
        if "’" in name:
            name = name.replace("’", "'&rsquo;'")
        output = output + f"<div class='card__title'> {name}<div/>\n"

    output = output + "<p class='card__text'>\n"

    diet = animal.get('characteristics').get('diet')
    if diet is not None:
        output = output + f"<strong>Diet:</strong> {diet}<br/>\n"

    locations = animal.get('locations')
    if locations is not None and len(locations) != 0:
        location = locations[0]
        output = output + f"<strong>Location:</strong> {location}<br/>\n"

    animal_type = animal.get('characteristics').get('type')
    if animal_type is not None:
        output = output + f"<strong>Type:</strong> {animal_type}<br/>\n"

    output = output + "</p>\n</li>"

print(output)


#reads animals_template
try:
    with open("animals_template.html", "r") as handle:
        template_data = handle.read()
except FileNotFoundError:
    print("The file was not found.")

#replaces old string with animal info
new_data = template_data.replace("__REPLACE_ANIMALS_INFO__", output)

print(new_data)

#creates new file with HTML and animal info
with open("animals.html", "w") as handle:
    handle.write(new_data)


