import json
import logging as log
from pathlib import Path

global path_to_file
path_to_file:str = "Data.json"

log.basicConfig(level=log.WARNING)

def write_to_file(data):
    global path_to_file
    fileexists = Path(path_to_file).exists()

    if not data:
        raise ValueError("Empty or invalid data")

    try:
        with open(path_to_file, "a") as f:
            f.write(json.dumps(data) + "\n")  # FIXED
        log.info("Data Written To File")
        return True

    except OSError:
        log.error("Failure To Write File")
        return False
    
def read_file():
    global path_to_file
    try:
        with open(path_to_file, "r") as f:
            lines = f.readlines()
        
        log.info("File Read Successful")


        entries = [json.loads(line) for line in lines]
        return entries

    except FileNotFoundError:
        log.error("File Not Found")
        return None

def dict_create():
    dicts:dict = {
        "Title":None,
        "Type":None,
        "Notes":None,
        "Rating":None,
        "Status":None,

    }

    return dicts

def collect_entries():
    mediareview:dict = dict_create()
    try:
        print("* indicates a required question")
        entry_1:str = input("Enter The Title Of The Media*").lower().strip()
        entry_2:str = input("Enter The Type Of Media(Book/Video game/Anime/Manga/Movie/TV Show)*").lower().strip()
        entry_3:str = input("Enter Any Notes You Had On the Media").lower()
        entry_4:int = int(input("Enter Your Rating Of The Media*"))
        entry_5:str = input("Enter How Done You Are With The Media(In Progress,Completed,Not Started)*").lower().strip()

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
        log.error(e)
        return None
    



def user_prompt(prompt):
    try:
        if not prompt:
            raise ValueError("Empty Or Invalid Prompt")
        else:
            userinput = input(prompt)
            if not userinput:
                raise ValueError("Empty Or Invalid Input")
            else:
                return userinput
    except ValueError as e:
        log.error(e)
        return None
    

def filter(datatype, datavalue):
    data_type_dict = {
        "rating": 1,
        "type": 2,
        "status": 3
    }

    x = data_type_dict.get(datatype)
    lines = read_file()

    match x:
            case 1:
           
                entries = [r for r in lines if r["Rating"] == int(datavalue)]
                return entries

            case 2:
            
                entries = [r for r in lines if r["Type"] == datavalue]
                return entries

            case 3:
            
                entries = [r for r in lines if r["Status"] == datavalue]
                return entries

            case _:
                return []
