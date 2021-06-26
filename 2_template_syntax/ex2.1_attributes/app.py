from vue import *

class App(VueComponent):
    someMessage = "Hello world from VuePy"
    rawHtml = "<p>Some <b>HTML</b> text</p>"
    template = """
    <div>
        {{someMessage}}
        <p>Using mustaches: {{ rawHtml }}</p>
        <p>Using v-html directive: <span v-html="rawHtml"></span></p>
    </div>
    """

    
    
App("#app")
