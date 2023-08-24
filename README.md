# pycolino

## Video-Demo:

https://www.youtube.com/watch?v=O9xzHHkCB4M

## Description:

This project is a command line tool that allows you to add notes to the files of a directory on the command line and read them. The program is written in Python and uses a CSV file to store the relevant data. Pycolino is an abbreviation for Python command line notes. The program has the following main functions:

- Defaultmode: Read and display the current directory structure and saved notes on the command line.
- Readmode: Reading and displaying a file called via the command line and the stored note
- Writemode: Selecting a file listed in the directory and writing a note to that same file from the command line

## Files and functions:

- pycolino.py: The main program with the main function and all other supporting functions.
    - main(): The mainfunction of the program. Controls the program flow and calls all other functions.
    - parse_comline(): Parses the command line input and returns a tuple of the parsed arguments.
    - prepare_options(): Checks the mode in which the program should run. Depending on the mode, returns a tuple with the file to be edited, the note to be added and the status in which the program should run.
    - read_csv(): Reads the pycolino.csv and generates a list which is then transferred.
    - create_csv(actual_dir): Creates a CSV without comments, but with the current directory structure.
    - create_temp(actual_dr, old_dr): Creates and returns a list of dictonarys containing the current directory and notes.
    - create_read(temp_dr, selected_file): Based on the selected file, creates a list with a single dictonary that contains the selected file and a possibly stored note.
    - create_write(temp_dr, selected_file, phrase): Writes the entered note to the corresponding file and creates a list with a single dictonary based on the selected file, which contains the selected file and the stored note.
    - save_list(temp_dr): Overwrites the csv-file with the temporarily created and edited list.
    - select_operate(modus, temp_dr, selected_file, phrase): Evaluates from the parsed input in which mode the program should run and returns a list with the corresponding output.
- pycolino.csv: In this CSV the directory structure and optional notes are stored. The first time the program is used in a new directory, the file is created automatically.
- test_project.py: Contains test functions to test the following functions from project.py: prepare_options, create_read and create_write
- requirements.txt: Contains the libraries that need to be installed via pip install. These are argparse, pytest and tabulate


## Design descisions

In developing this command line application, certain design decisions were made to improve usability and performance. Some of these decisions were:

- use of python: Python was used as the language because it is easy and efficient to use for developing this program and has a very good library for output with tabulate.
- use of csv: csv was used as the storage format because it is absolutely sufficient and easy to use for the purpose employed.
- use of paradigm: The program is not complex enough for object-oriented programming, instead the code has a high proportion of functions and is slightly oriented towards functional programming here.

## Contributing

I welcome contributions to improve this project. If you want to improve something, please create a pull request with a detailed description of the changes.

## Author

- Author: epicwinzer

## Contact

If you have any questions, problems or suggestions, you can contact me by e-mail: webmaster@midlifestudent.de
