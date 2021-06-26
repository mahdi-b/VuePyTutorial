from vue import *

class App(VueComponent):
    someVar = 1
    message = "Hello World"
    template = """
    <div>
        <H3>Something Here</H3>
    </p>{{someVar}}</p>
    </p>{{someVar + 1 }}</p>
    </p>{{message.split('').reverse().join('')}}</p>
    </p>{{log("some message")}}</p>

    </div>
    """

    def log(self, var=None):
        print(f"in debugging: {var}")

    
    
    
App("#app")
