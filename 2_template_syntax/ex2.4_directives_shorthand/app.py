from vue import *

class App(VueComponent):
    url = "/a/b/c"
    key = "href"
    event="click"
    template = """
    <div>
         <h2>Biniding</h2>
         <p><a v-bind:href="url"> Method 1 </a></p>
         <p><a :href="url"> Method 2 </a></p>
         <p><a :[key]="url"> Method 3 </a></p>

         <h2>Click</h2>
         <p><a v-on:click="clicked"> Method 1 </a></p>
         <p><a @click="clicked"> Method 2 </a></p>
         <p><a @[event]="clicked"> Method 3 </a></p>



    </div>
    """

    def clicked(self, evt):
        print(f"Clicked: {evt}")

    
    
    
App("#app")
