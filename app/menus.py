import actions

menu_history = [] # Datastructure:- Stack (Tracks the history of menus)
current_menu = None # current menu selected

menu = { # Tree Data Structure
    "1": {
        "message": "Manage Categories",
        "options":{
            "1": {
                "message":"List categories",
                "action": actions.get_categories,
            },
            "2": {
                "message":"Add a category",
                "action": actions.add_category,
                "fields":[
                    { "label": "Enter category name:-", "field": "name"},
                    { "label": "Enter description:-", "field": "description"}
                ]
            },
            "3": {
                "message":"Update Category",
                "action": actions.get_categories,
            },
            "4": {
                "message":"Delete Category",
                "action": actions.get_categories,
            },
            "Back": {
                "message":"Update Category"
            }
        }
    },
    "2": {
        "message": "View Products",
        "action": actions.get_products
    },
    "exit":{
        "message": "Exis system"
    }
}