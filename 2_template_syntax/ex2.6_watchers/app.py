from vue import *
import time

class App(VueComponent):
    message= "A"
    template = """
      <div id="example">

        <input type="text" v-model="message"><br><br>

      </div>
    """
    @watch("message")
    def log_change(self, new, old):
        print(f"message changed from '{old}' to new {new}")
    
App("#app")
