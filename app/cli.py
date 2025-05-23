#!/usr/bin/env python

from menus import menu, current_menu, menu_history

# user to be able to see all categories and products
# user to be able to add/update/delete categories and products
# user to be able to generate and export a report (csv)


# click
if __name__ == "__main__":
    print("Welcome to the invetory application!!!")
    
    while True:
        # we need to be able to get the current menu as a working menu 
        # otherwise use the base menu in the menus.py module
        working_menu = current_menu if current_menu != None else menu

        # We loop through the menu dictionary and
        # display the options that a user should pick
        for k, v in working_menu.items():
            print(f"{k}. {v["message"]}")
        
        # We request a user to select an option based on the listed options
        option = input("Select an option:- ")

        # if the user enters an exit command, we break out of the loop
        if option == "exit":
            break
        
        # if the user enters a back option, we go to the previous menu
        if option == "back":
            menu_history.pop()
            current_menu = None if len(menu_history) == 0 else menu_history[-1]
            continue
        
        # Check if the selected option has an action
        if option in menu:            
            if "action" in working_menu[option]:

                # Check if there is some data that the user needs to enter
                # and collect that data
                if "fields" in working_menu[option]:
                    obj = {} # this variable stores all the information need to execute the action
                    for field in working_menu[option]["fields"]:
                        obj[field["field"]] = input(field["label"])
                    # Execute the action here passing in all the data we collected from user
                    working_menu[option]["action"](obj)
                
                else:
                    # Execute the action without any arguments if there is no data to collect
                    working_menu[option]["action"]()
            
            # if there are other options in the selected menu,
            # proceed to the next menu options and repeat the same process
            if "options" in working_menu[option]:
                current_menu = working_menu[option]["options"]
                menu_history.append(current_menu)

        else:
            print("Please select an option")

        print("""
--------------------------
              """)


# manage a resource(categories, products)
# add / delete / update
# go back