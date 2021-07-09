from vue import *

class App(VueComponent):
    isValid = True
    #items =[{"id": 1, "message":"Test 1"}, {"id": 2, "message":"Test 2"}, {"id": 3, "message":"Test 3"},]
    someObject = {"A":1, "B":2, "C":3}
    template = """
    <div>

    <ul id="v-for-object" class="demo">
    <li v-for="val in 10">
       {{ val }}
    </li>
    </ul>

    <hr/>

    <template v-for=" val in 10">
      <table style="border: 1px solid black;">
      <tr>
        <th>val</th>
      </tr>
      <tr>
        <td>{{val}}</td>
      </tr>
      </table>
      <br/>
    </template>

    <hr/>

    <li v-for="val in 10" v-if="val % 2 == 0">
      {{ val}}
    </li>

    </div>
    """

    
        
        
App("#app")
