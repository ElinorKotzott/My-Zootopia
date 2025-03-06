import requests
import os
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv('API_KEY')

def fetch_data():
    """fetches data from animal API depending on user_input"""
    animal = input("Enter an animal name! ")
    url = f"https://api.api-ninjas.com/v1/animals?&name={animal}"
    try:
        animals_data = requests.get(url, headers={"X-Api-Key": API_KEY}).json()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching the data: {e}")
        return None

    if not animals_data:
        error_string = f"{animal} doesn't exist!"
        # reads animals_template
        try:
            with open("animals_template.html", "r") as handle:
                template_data = handle.read()
        except FileNotFoundError:
            print("The file was not found.")
            return None
        # replaces old string with error message
        new_data = template_data.replace("__REPLACE_ANIMALS_INFO__", error_string)
        # creates new file with HTML and animal info
        with open("animals.html", "w") as handle:
            handle.write(new_data)
        return None
    else:
        return animals_data