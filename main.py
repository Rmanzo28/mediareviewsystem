import helpers as helpers
import logging as log
import json



def main():
    print("=" * 40)
    print(" Welcome to the Media Review System ")
    print("Rate, review, and explore your favorite media!")
    print("=" * 40)

    while True:
        userchoice = input("What Would You Like To Do? (Enter/View/Sort/Quit): ").lower().strip()

        match userchoice:

            case "enter":
                data_dict = helpers.collect_entries()
                if data_dict:
                    success = helpers.write_to_file(data_dict)
                    if not success:
                        print("File Write Failed")

            case "view":
                lines = helpers.read_file()
                if lines:
                    print(lines)
                if not lines:
                    log.error("File Not Found/Created")

            case "sort":
                sort_choice = input("Sort by (type/rating/status): ").lower().strip()
                value = input("Enter value to filter by: ")
                results = dict(helpers.filter(sort_choice, value))

                print(json.dumps(results, indent=4))

            case "quit":
                print("Goodbye!")
                break

            case _:
                print("Invalid option")

main()
                        
                

             

   
                     
                     
                     

                









        
    

    
