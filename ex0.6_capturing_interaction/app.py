from vue import *

class App(VueComponent):
    template = "#htmltemplate"

    message ="Hello World"
    def reverseMessage(self, event):
        print(f"The message was clicked {event}")
        self.message = " ".join(self.message.split()[::-1])

App("#app")
