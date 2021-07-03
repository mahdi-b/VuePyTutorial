from vue import *

class App(VueComponent):
    isValid = True
    template = """
    <div>
      <div v-if="isValid">
        <p>Yes Valid  0</p>
        <p>Yes Valid  1</p>
      </div>
      <hr>

      <template v-if="isValid">
	<p>Yes Valid  2</p>
	<p>Yes Valid  3</p>
      </template>

      <hr/>

      <div v-if="Math.random() > 0.75">
        A
      </div>
      <div v-else>
        B
      </div>
    </div>
    """

    
        
        
App("#app")
