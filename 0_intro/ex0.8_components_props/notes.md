* We customize the component by giving it props
   * it's a way to pass components data
   
* We are biding the item.text to a new variable called todo
   * This variable will be avaible in python code for the component
   ```v-bind:todo="item"```

* Note that we need to register the component, otherwise the app doesn't know what TodoItem (todo-item) is

  ```TodoItem.register("todo-item")````


