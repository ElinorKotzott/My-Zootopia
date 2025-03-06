import data_fetcher

def serialize_animal(animal_obj):
    """concatenates strings for the HTML file using the list of dictionaries in animals_data"""
    output = ""
    output = output + "<li class='cards__item'>"
    name = animal_obj.get('name')
    if name is not None:
        # ensuring the apostrophe will be depicted correctly
        if "’" in name:
            name = name.replace("’", "&rsquo;")
        output = output + f"<div class='card__title'> {name}</div>\n"

    output = output + "<div class='card__text'>\n<ul>\n"

    locations = animal_obj.get('locations')
    if locations is not None and len(locations) != 0:
        location = locations[0]
        output = output + f"<li><strong>Location:</strong> {location}</li>\n"

    if animal_obj.get('characteristics') is not None:

        diet = animal_obj.get('characteristics').get('diet')
        if diet is not None:
            output = output + f"<li><strong>Diet:</strong> {diet}</li>\n"

        animal_type = animal_obj.get('characteristics').get('type')
        if animal_type is not None:
            output = output + f"<li><strong>Type:</strong> {animal_type}</li>\n"

        lifespan = animal_obj.get('characteristics').get('lifespan')
        if lifespan is not None:
            # ensuring the hyphen will be depicted correctly
            if "–" in lifespan:
                lifespan = lifespan.replace("–", "-")
            output = output + f"<li><strong>Lifespan:</strong> {lifespan}</li>\n"

        lifestyle = animal_obj.get('characteristics').get('lifestyle')
        if lifestyle is not None:
            output = output + f"<li><strong>Lifestyle:</strong> {lifestyle}</li>\n"

    output = output + "</ul></div>\n</li>"
    return output


def main():
    animals_data = data_fetcher.fetch_data()
    if animals_data is not None:
        final_output = ""
        for animal in animals_data:
            final_output = final_output + serialize_animal(animal)
        # reads animals_template

        try:
            with open("animals_template.html", "r") as handle:
                template_data = handle.read()
        except FileNotFoundError:
            print("The file was not found.")
            return None
        # replaces old string with animal info
        new_data = template_data.replace("__REPLACE_ANIMALS_INFO__", final_output)
        print("Website was successfully generated to the file 'animals.html'.")
        # creates new file with HTML and animal info
        with open("animals.html", "w") as handle:
            handle.write(new_data)


if __name__ == "__main__":
    main()

