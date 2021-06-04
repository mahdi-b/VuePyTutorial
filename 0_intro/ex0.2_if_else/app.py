from vue import *

class App(VueComponent):
    seen = False
    template = """
        <div>
            <span v-if="seen">Now you see me</span>
            <span else="seen">Now you don't</span>
        </div>
    """
    


App("#app")
