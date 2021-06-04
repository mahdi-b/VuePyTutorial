from vue import *



    
class App(VueComponent):
    template="<h1>Hi There!</h1>"
    
    def created(self):
        # should appear in the dev JS tools/console
        print("The app was created now")

App("#app")
