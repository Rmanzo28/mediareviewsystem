# package imports
import helpers as helpers
import logging as log
import json



#main function
def main():
    # welcome screen
    print("=" * 40)
    print(" Welcome to the Media Review System ")
    print("Rate, review, and explore your favorite media!")
    print("=" * 40)
    # main loop
    while True:
        # asks the user what they want to do
        userchoice = input("What Would You Like To Do? (Enter/View/Sort/Quit): ").lower().strip()
        # match statement(python equivalent of switch) to map user response -> action
        match userchoice:

            case "enter":
                # handles data entry and writing
                data_dict = helpers.collect_entries()
                if data_dict:
                    success = helpers.write_to_file(data_dict)
                    if not success:
                        print("File Write Failed")

            case "view":
                # handles viewing all entries
                lines = helpers.read_file()
                if lines:
                    print(json.dumps(lines, indent=4))
                if not lines:
                    log.error("File Not Found/Created")

            case "sort":
                #sort by userinput
                sort_choice = input("Sort by (type/rating/status): ").lower().strip()
                value = input("Enter value to filter by: ")
                results = helpers.filter(sort_choice, value)
                # print the dictionary neatly
                print(json.dumps(results, indent=4))

            case "quit":
                # end program
                print("Goodbye!")
                break

            case _:
                # if input is invalid handler
                print("Invalid option")
# prevents recursive calling of main() by ensuring caller is the main thread
if __name__ == "__main__":
    main()
                        
                

             

   
                     
                     
                     

                









        
    

    
