from tabulate import tabulate
import argparse
import csv
import os
import sys


def main():
    # parsing the comand-line-arguments
    parsed = parse_comline()

    # creating selected_file, messag and modus for the further operations
    selected_file, phrase, modus = prepare_options(parsed.read, parsed.write)

    # creating actual dir with directory, and check if pycolino.csv allready exists
    # if not, create it
    actual_dr = os.listdir()
    if not "pycolino.csv" in actual_dr:
        create_csv(actual_dr)

    # creating old_dr as a list from the pycolino.csv
    old_dr = read_csv()

    # creating a temp-list to work with, updating csv with actual directory
    temp_dr = create_temp(actual_dr, old_dr)

    # Selects the status, in which the programm shall run
    temp_ops = select_operate(modus, temp_dr, selected_file, phrase)

    # clear terminal
    if os.name in ["nt", "dos"]:
        os.system("cls")
    else:
        os.system("clear")

    # print output
    print(tabulate(temp_ops, headers="keys", tablefmt="rounded_outline"))

    # final saving of modified csv
    save_list(temp_dr)


def parse_comline():
    """
    Parsing the comand-line-arguments.

    :return: A tuple of the parsed arguments
    :rtype: tuple
    """
    parser = argparse.ArgumentParser(
        description="A simple comand-line-tool for adding notes to your files and read them. By default without arguments pycolino will show the complete directory."
    )
    parser.add_argument(
        "-r",
        "--read",
        help="Readmode: The name of the file whose notes you want to read. For reading -w must not be selected.",
        type=str,
        default="",
    )
    parser.add_argument(
        "-w",
        "--write",
        help="Additional writemode: Write a note in quotes about the file you selected with -r.",
        type=str,
        default="",
    )
    return parser.parse_args()


def prepare_options(reading: str, writing: str) -> tuple:
    """
    Checking the status in which pycolino shall run

    :param reading: the choosen file
    :type reading: str
    :param writing: the message to save
    :type writing: str
    :param modus: the running modus for pycolino
    :type modus: str
    :return: A tuple of reading, writing, status
    :rtype: tuple
    """
    modus = "default"
    if reading != "" and writing != "":
        modus = "write"
    if reading != "" and writing == "":
        modus = "read"

    return (reading, writing, modus)


def read_csv() -> list:
    """
    reads the pycolino.csv and generates a list

    :return: A list of dicts with the data of the pycolino.csv
    :rtype: list
    """
    csv_drs = []
    with open("pycolino.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            csv_drs.append({"name": row["name"], "message": row["message"]})

    return csv_drs


def create_csv(actual_dir):
    """
    creates an csv without messages but with the actual directory
    """
    with open("pycolino.csv", "w") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "message"])
        writer.writeheader()
        for act in actual_dir:
            writer.writerow({"name": act, "message": ""})


def create_temp(actual_dr: list, old_dr: list) -> list:
    """
    creates a list of dicts with actual directory and comments as tempfile

    :param actual_dr: a list of the actual directory from system
    :type actual_dr: list
    :param old_dr: a list of dicts out of the csv-file
    :type old_dr: list
    :return: an updated list, combining actual directory with comments from csv
    :rtype: list
    """
    temp_dr = []
    for actual in actual_dr:
        found = 0
        for old in old_dr:
            if old["name"] == actual:
                temp_dr.append({"name": actual, "message": old["message"]})
                found = 1
        if found == 0:
            temp_dr.append({"name": actual, "message": ""})

    return temp_dr


def create_read(temp_dr, selected_file) -> list:
    """
    Returning a list with a single dict, depending on selected_file

    :param temp_dr: a list of the updated directory
    :type actual_dr: list
    :param selected_file: a str with the file to search for
    :type seletcted_file: str
    :return: a list with a singe dict of the searched file
    :rtype: list
    """
    for temp in temp_dr:
        if selected_file == temp["name"]:
            return [{"name": temp["name"], "message": temp["message"]}]

    sys.exit("Something went wrong.")


def create_write(temp_dr, selected_file, phrase) -> list:
    """
    Writing the phrase into the row with the selected file and returns

    :param temp_dr: a list of the updated directory
    :type actual_dr: list
    :param selected_file: a str with the file to search for
    :type seletcted_file: str
    :param phrase: a str with the phrase to write
    :type phrase: str

    :return: a list with a singe dict of the file written in
    :rtype: list
    """
    for temp in temp_dr:
        if selected_file == temp["name"]:
            temp["message"] = phrase
            return [{"name": temp["name"], "message": temp["message"]}]

    sys.exit("Something went wrong.")


def save_list(temp_dr):
    """
    Saving the modified list into the pycolino.csv

    :param temp_dr: a list of the updated directory
    :type actual_dr: list
    """
    with open("pycolino.csv", "w") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "message"])
        writer.writeheader()
        for temp in temp_dr:
            writer.writerow({"name": temp["name"], "message": temp["message"]})


def select_operate(modus, temp_dr, selected_file, phrase) -> list:
    """
    Selecting the modus to work

    :param modus: a str with the choosen modus
    :type modus: str
    :param temp_dr: a list of the updated directory
    :type actual_dr: list
    :param selected_file: a str with the file to search for
    :type seletcted_file: str
    :param phrase: a str with the phrase to write
    :type phrase: str

    :return: a list with the content to print out in main
    :rtype: list
    """
    match modus:
        case "read":
            return create_read(temp_dr, selected_file)
        case "write":
            return create_write(temp_dr, selected_file, phrase)
        case "default":
            return temp_dr
        case _:
            sys.exit("Something went wrong")


if __name__ == "__main__":
    main()
