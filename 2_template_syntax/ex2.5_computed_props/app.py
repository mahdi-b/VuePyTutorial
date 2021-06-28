from vue import *
import time

class App(VueComponent):
    message= " "
    template = """
      <div id="example">

        <input type="text" v-model="message"><br><br>

        <p>Computed reversed message: "{{ reversedMessage }}"</p>
        <p>Computed reversed message: "{{ reversedMessage }}", computed at: {{now}}</p>

      </div>
    """
    @computed
    def reversedMessage(self):
        return " ".join(self.message.split()[::-1])

    @computed
    def now(self):
        return time.time()

    
    
App("#app")
