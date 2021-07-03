from vue import *

class App(VueComponent):
    isValid = True
    items =[{"id": 1, "message":"Test 1"}, {"id": 2, "message":"Test 2"}, {"id": 3, "message":"Test 3"},]
    someObject = {"A":1, "B":2, "C":3}
    template = """
    <div>

    <ul id="example-1">
    <li v-for="item in items" :key="item.id">
    {{ item.message }}
    </li>
    </ul>

    <hr/>

    <ul id="example-2">
    <li v-for="(item, index) in items">
    {{ index }} - {{ item.message }}
    </li>
    </ul>

    <hr/>

    <ul id="v-for-object" class="demo">
    <li v-for="(value, key, index) in someObject">
   {{ index }}: {{ key }} --> {{ value }}
    </li>
    </ul>


    </div>
    """

    
        
        
App("#app")
