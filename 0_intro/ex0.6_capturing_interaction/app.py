from vue import *

class App(VueComponent):
    template = "#htmltemplate"

    message ="Hello World"
    def reverseMessage(self, event):
        print(f"The message was clicked {event}")
        self.message = self.message[::-1]

App("#app")
