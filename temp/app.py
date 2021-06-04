from vue import *

class MainTableView(VueComponent):
    # do something to get the data form mahdi@receiptstogo.com from firebase
    # store the data in a variable called data
    data = [{"vendor": "Apple", "total": 100.01}, {"vendor": "Best Buy", "total": 250.20}]
    
    template = """
    <div>
      <div v-for="receipt in data">
        <p>vendor: {{receipt.vendor}} </p>
        <p>total: {{receipt.total}}   </p>
        <hr>
      </div>
    </div>
    """

MainTableView.register("transaction-table")


class App(VueComponent):

    template = "<transaction-table></transaction-table>"



App("#app")
