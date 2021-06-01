from vue import *

class App(VueComponent):
    someMessage = "Hello world from VuePy" 
    template = "<div>{{someMessage}}</b></div>"
App("#app")
