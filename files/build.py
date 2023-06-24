import os
import sys
from jinja2 import Environment, FileSystemLoader

SUCCESS = 0
ERROR = 84
OUTPUT_FOLDER = "./output"
INPUT_FOLDER = "./files/templates"


def get_output_folder(args: list, output_folder: str = OUTPUT_FOLDER) -> str:
    """ Get the output folder if provided """
    if len(args) > 1:
        return args[1]
    return output_folder


def get_input_folder(args: list, input_folder: str = INPUT_FOLDER) -> str:
    """ Get the input folder if provided """
    if len(args) > 2:
        return args[2]
    return input_folder


def create_paths_if_not_exist(path: str = OUTPUT_FOLDER) -> None:
    """ Create the output path if it does not exist """
    if os.path.exists(path) == False:
        os.makedirs(path, exist_ok=True)


def get_all_folders_for_the_environement(src: str) -> list[str]:
    """ Get all the folders for the environment """
    folders = [src]
    content = os.listdir(src)
    for item in content:
        my_path = os.path.join(src, item)
        if os.path.isdir(my_path):
            folders.append(my_path)
            folders.extend(get_all_folders_for_the_environement(my_path))
    return folders


def get_all_pages(src: str, rule: str) -> list[str]:
    """ Get all the Jinja webpages to be converted """
    pages = []
    content = os.listdir(src)
    for item in content:
        my_path = os.path.join(src, item)
        if os.path.isfile(my_path) and rule in item:
            pages.append(to_linux(my_path))
        if os.path.isdir(my_path):
            pages.extend(get_all_pages(my_path, rule))
    return pages


def render_page(file_name: str, render_env: Environment, output_name: str) -> int:
    """ Render a jinja page """
    # try:
    render_template = render_env.get_template(file_name)
    rendered_output = render_template.render()
    create_paths_if_not_exist(os.path.dirname(output_name))
    file = open(output_name, "w", encoding="utf-8")
    file.write(rendered_output)
    file.close()
    print(f"Conversion = {rendered_output}")
    return SUCCESS
    # except Exception as err:
    #     print(f"Error: {err}", end=" ")
    # return ERROR


def create_folders_of_directory(my_pages: list[str]) -> None:
    """ Create the folders of the directory """
    for page in my_pages:
        output = page.split('/')
        output[0] = output[0].replace(INPUT_FOLDER, "")
        res = OUTPUT_FOLDER
        for i in output:
            if len(i) > 0:
                res += f"/{i}"
        create_paths_if_not_exist(res)


def to_linux(path: str) -> str:
    """ Convert the path to a linux path """
    return path.replace("\\", "/")


def main(input_folder, output_folder):
    """ The main function of the program """
    # Get the output and input folder
    output_folder = to_linux(get_output_folder(sys.argv))
    input_folder = to_linux(get_input_folder(sys.argv))
    print(f"INPUT_FOLDER = {input_folder}\nOUTPUT_FOLDER = {output_folder}")
    print("Gathering folders for the environement")
    folds = get_all_folders_for_the_environement(input_folder)
    print(f"Found folders = {folds}")
    env = Environment(
        loader=FileSystemLoader(
            folds,
            encoding="utf-8",
            followlinks=True
        )
    )
    # Create the output folder if it does not exist
    print(f"Checking folder presence = '{output_folder}'")
    create_paths_if_not_exist(output_folder)

    # get all the website pages
    pages = get_all_pages(input_folder, "index.j")
    print(f"Found pages = {pages}")

    # Render all the pages
    print("Rendering pages")
    for page in pages:
        output = page
        if '\\' in page:
            output = output.replace("\\", "/")
        output = output.split('/')
        output[0] = output[0].replace(input_folder, "")
        res = output_folder
        for i in output:
            if len(i) > 0:
                res += f"/{i}"
        print(f"Rendering page {page} to {res}...", end="")
        status = render_page(page, env, res)
        if status == SUCCESS:
            print("[OK]")
        else:
            print("[KO]")


if __name__ == "__main__":
    main(INPUT_FOLDER, OUTPUT_FOLDER)
