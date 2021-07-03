from vue import *

class App(VueComponent):
    isActive = False
    isError = True
    activeClass = "A"
    errorClass = "C"
    activeColor = "blue"
    fontSize = 40
    
    template = """


    <div>
        <p v-bind:class="{ active: isActive, error: isError}">Active is set </p>
        <p v-bind:class="{ active: !isActive }">Active is not set </p>
        <button v-on:click="isError = !isError;">Set Error</button>

        <hr/>

        <!-- Binding activeClass and hardcoding B-->
        <p v-bind:class="[isActive ? activeClass : 'B', errorClass]">Using arrays</p>

        <hr/>
        <p v-bind:style="{ color: activeColor, fontSize: fontSize + 'px' }">Style works the same way as class</p>

    </div>


    """

    
        
        
App("#app")
