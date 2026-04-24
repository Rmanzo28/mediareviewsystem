import json
import logging
from pathlib import Path

global path_to_file
path_to_file = "Data.txt"

logging.basicConfig(level=logging.INFO)

def write_to_file(data):
    global path_to_file
    fileexists = Path(path_to_file).exists()

    if not data:
        raise ValueError("Empty or invalid data")
    

    if fileexists:
        try:
            with open(path_to_file, "a") as f:
                f.write(json.dumps(data + "\n"))

        except OSError:
            print("Failure to write file")
            return False

    else:
        logging.warning("File not found")
        logging.info("Creating File Data.txt")

        try:
            with open(path_to_file, "w") as f:
                f.write(json.dumps(data + "\n"))

        except OSError:
            print("Failure to create/write file")
            return False

    return True

def read_file():
    global path_to_file
    try:
        with open(path_to_file, "r") as f:
            lines = f.readlines()

        entries = [json.loads(line) for line in lines]
        return entries

    except FileNotFoundError:
        print("File not found")
        return None

def dict_create():
    dicts = {
        "Title":None,
        "Type":None,
        "Notes":None,
        "Rating":None,
        "Status":None,

    }

    return dicts

def collect_entries():
    mediareview = helpers.dict_create()
    try:
        print("* indicates a required question")
        entry_1 = input("Enter The Title Of The Media*").lower().strip()
        entry_2 = input("Enter The Type Of Media(Book/Video game/Anime/Manga/Movie/TV Show)*").lower().strip()
        entry_3 = input("Enter Any Notes You Had On the Media").lower()
        entry_4 = int(input("Enter Your Rating Of The Media*"))
        entry_5 = input("Enter How Done You Are With The Media(In Progress,Completed,Not Started)*").lower().strip()

        if entry_1 and entry_2 and entry_4 and entry_5:
            mediareview["Title"] = entry_1
            mediareview["Type"] = entry_2
            mediareview["Notes"] = entry_3
            mediareview["Rating"] = entry_4
            mediareview["Status"] = entry_5
            return mediareview
        else:
            raise ValueError("One Or More Fields Not Filled Out")
        
    except ValueError as e:
        print(e)
        return None