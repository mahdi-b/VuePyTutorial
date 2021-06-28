from vue import *
from my_utils import debounce
from browser import timer
import random 

class App(VueComponent):
    question=""
    answer= 'I cannot give you an answer until you ask a question!'
    template = """
    <div id="watch-example">
      <p>
        Ask a yes/no question:
        <input v-model="question">
      </p>
      <p>{{ answer }}</p>
    </div>
    """
    debouncedGetAnswer = None

    def created(self):
        # Wait for at least 500 MS after typing to call getAnswer
        # Every typing event resets the type fo 500 MS
        self.debouncedGetAnswer = debounce(self.getAnswer, 500)
        print(f"Finished Creating debounceGetAnswer. its value is {self.debouncedGetAnswer}")

    @watch("question")
    def question_updated(self, new, old):
        print("question was updated")
        self.answer = 'Waiting for you to stop typing...'
        self.debouncedGetAnswer()


    def getAnswer(self):
         if "?" not in self.question:
             self.answer = 'Questions usually contain a question mark. ;-)'
         else:
             # do some long running process and anser the question
             timer.set_timeout(self.update_answer, 3000)

    def update_answer(self):
        self.answer = random.sample(["Yes", "No", "Maybe", "Not sure"], 1)[0]
        
        
App("#app")
