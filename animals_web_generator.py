import data_fetcher


def load_data_from_html(file_path):
    """ Loads an HTML file """
    with open(file_path, "r") as original_html:
        return original_html.read()


def write_new_html_file(file_path, content):
    """Writes new HTML file"""
    with open(file_path, "w") as new_html:
        return new_html.write(content)


def serialize_animal(animal):
    """ returns an HTML-formatted string with specific data about a single animal"""
    output = ""
    output += '<li class="cards__item">'
    output += f'\t<div class="card__title">{animal["name"]}</div>\n'
    output += '\t<div class="card__text">'
    output += '\t\t<ul>'
    output += f'\t\t\t<li><strong>Diet:</strong> {animal["characteristics"]["diet"]}</li>\n'
    output += f'\t\t\t<li><strong>Location:</strong> {animal["locations"][0]}</li>\n'
    if "type" in animal["characteristics"]:
        output += f'\t\t\t<li><strong>Type:</strong> {animal["characteristics"]["type"]}</li>\n'
    output += '\t\t</ul>'
    output += '\t</div>'
    output += '</li>'
    return output


def generate_html_code(overall_data):
    """ iterates through all animals """
    output = ""
    if '<h4>The animal' in overall_data[0] and "doesn't exist.</h4>" in overall_data[0]:
        output = f'<li class="cards__item">	<div class="card__title">{overall_data[0]}</div></li>'
        return output
    for animal in overall_data:
        output += serialize_animal(animal)
    return output


def main():
    animal_name = input("Enter a name of an animal: ").lower()
    animals_data = data_fetcher.fetch_data(animal_name)
    desired_output = generate_html_code(animals_data)
    original_html_content = load_data_from_html('animals_template.html')
    updated_html_content = original_html_content.replace("__REPLACE_ANIMALS_INFO__", desired_output)
    updated_html_content = updated_html_content.replace('<style>', '<meta charset="UTF-8" /> \n\t<style>')
    write_new_html_file('animals.html', updated_html_content)
    print("Website was successfully generated to the file animals.html")


if __name__ == "__main__":
    main()
