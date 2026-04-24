import helpers as helpers
import logging as log


def main():
       
        print("=" * 40)
        print(" Welcome to the Media Review System ")
        print("Rate, review, and explore your favorite media!")
        print("=" * 40)
        userchoice = input("What Would You Like To Do?(Enter/View/Sort)").lower()
       

        match userchoice:
                case "enter":
                         while (True):
                                try:

                                    data_dict:dict = helpers.collect_entries()
                                    success:bool = helpers.write_to_file(data_dict)
                                    if success:
                                           break
                                    elif not success:
                                           print("File Write Failed")
                case "view":
                        
                case "sort":
                        
                

             

       # while (True):
           # try:

             #   data_dict:dict = helpers.collect_entries()
              #  success:bool = helpers.write_to_file(data_dict)
              # if success:
                     
                     
                     
                     

                









        
    

    
