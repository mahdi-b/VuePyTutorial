from vue import *

class TodoItem(VueComponent):
    todo: str
    template = "<li>{{ todo }}</li>"
    def created(self):
        print("Todo-item was created")
    



    
class App(VueComponent):

    template = "#htmltemplate"

    groceryList = [{ "id": 0, "text": 'Vegetables' },
                   { "id": 1, "text": 'Cheese' },
                   { "id": 2, "text": 'Whatever else humans are supposed to eat' }
                ]
    def created(self):
        print("App was created")

TodoItem.register("todo-item")
App("#app")
