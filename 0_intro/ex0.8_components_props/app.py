from vue import *

class TodoItem(VueComponent):
    todo: str
    template = "<li>{{ todo }}</li>"

TodoItem.register("todo-item")

    
class App(VueComponent):

    template = "#htmltemplate"

    groceryList = [{ "id": 0, "text": 'Vegetables' },
                   { "id": 1, "text": 'Cheese' },
                   { "id": 2, "text": 'Whatever else humans are supposed to eat' }
                ]


App("#app")
