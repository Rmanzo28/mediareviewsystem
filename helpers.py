# the file with the main functions

# module imports
import json
import logging
from pathlib import Path
# path to file  declaration
global path_to_file
path_to_file = "Data.json"
# we should only need logging if there is an issue on user side

logging.basicConfig(level=logging.WARNING)
# secure file. writer(safe, catches null or invalid data before write)
def write_to_file(data):
    global path_to_file
    fileexists = Path(path_to_file).exists()

    if not data:
        raise ValueError("Empty or invalid data")
    
    # checks if the file exists
    if fileexists:
        try:
            # append to existing file
            with open(path_to_file, "a") as f:
                f.write(json.dumps(data) + "\n")
        # catch failures to write
        except OSError:
            print("Failure to write file")
            return False

    else:
        #logging that file isnt found and that it is being created
        logging.warning("File not found")
        logging.info("Creating File Data.txt")

        try:
            # create and write file
            with open(path_to_file, "w") as f:
                f.write(json.dumps(data + "\n"))

        except OSError:
            print("Failure to create/write file")
            return False

    return True
#secure reading of the file
def read_file():
    global path_to_file
    try:
        # gets lines of the file and returns them as dict
        with open(path_to_file, "r") as f:
            lines = f.readlines()

        entries = [json.loads(line) for line in lines]
        return entries
    #catches if the file is nto found
    except FileNotFoundError:
        print("File not found")
        return None
# creates the dictionary for each user entry
def dict_create():
    dicts = {
        "Title":None,
        "Type":None,
        "Notes":None,
        "Rating":None,
        "Status":None,

    }

    return dicts
# the main function where users would enter entries
def collect_entries():
    mediareview = dict_create()
    try:
        print("* indicates a required question")
        entry_1 = input("Enter The Title Of The Media*:").lower().strip()
        entry_2 = input("Enter The Type Of Media(Book/Video game/Anime/Manga/Movie/TV Show)*:").lower().strip()
        entry_3 = input("Enter Any Notes You Had On the Media:").lower()
        entry_4 = int(input("Enter Your Rating Of The Media*:"))
        entry_5 = input("Enter How Done You Are With The Media(In Progress,Completed,Not Started)*:").lower().strip()

        if entry_1 and entry_2 and entry_4 and entry_5:
            #checks that all required fields are filled out
            mediareview["Title"] = entry_1
            mediareview["Type"] = entry_2
            mediareview["Notes"] = entry_3
            mediareview["Rating"] = entry_4
            mediareview["Status"] = entry_5
            return mediareview
        else:
            # catches errors
            raise ValueError("One Or More Fields Not Filled Out")
        
    except ValueError as e:
        print(e)
        return None
# filter/sort function
def filter(datatype, datavalue):
    # the dict that matches input to types
    data_type_dict = {
        "rating": 1,
        "type": 2,
        "status": 3
    }

    x = data_type_dict.get(datatype)
    lines = read_file()
    
    # checks that file is not empty before sorting
    if not lines:
        return []
    # match statement to turn the user requested sort(rating/type/completion status) -> the correct sorting algorithm
    match x:
        case 1:
            try:
                # sorts by rating
                rating = int(datavalue)
                return [r for r in lines if r["Rating"] == rating]
            except ValueError:
                return []

        case 2:
            # sorts by type
            return [r for r in lines if r["Type"] == datavalue]

        case 3:
            #sorts by status
            return [r for r in lines if r["Status"] == datavalue]

        case _:
            # if nothing matches or input is invalid
            return []