from vue import *

class App(VueComponent):
    todos = ["Get 4 lbs", "Email party invitations", "Return books to libraray"]

    template = """
      <div>
        <ol>
          <li v-for="todo in todos">
            {{ todo}}
          </li>
        </ol>
      </div>
    """
    


App("#app")
