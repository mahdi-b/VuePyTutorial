from vue import *

class App(VueComponent):
    seen = False
    someUrl="/a/b/c"
    eventName = "click"
    
    template = """
    <div>
        <p v-if="seen">Now you see me</p>
        <p v-else>or not</p>
        
        <p> <a v-bind:href="someUrl"> This should take me to "{{someUrl}}" </a></p>
       
        <p><a v-on:click="clicked"> Explicit argument: Click me </a></p>


         <p><a v-on:[eventName]="clicked"> Dynamic Arguments: click me </a></p>

    </div>
    """

    def clicked(self, evt):
        print(f"Clicked: {evt}")

    
    
    
App("#app")
