* A Vue application consists of a root Vue instance created with new Vue
  * optionally organized into a tree of nested, reusable components.

└─ TodoList
   ├─ TodoItem
   │  ├─ TodoButtonDelete
   │  └─ TodoButtonEdit
   └─ TodoListFooter
      ├─ TodosButtonClear
      └─ TodoListStatistics


* At creation Vue instance adds all the properties found in its data object to Vue’s reactivity system.

* When the values of those properties change, the view will “react”, updating to match the new values.

* Each Vue instance goes through a series of initialization steps when it’s created
 1. Set up data observation
 2. compile the template
 3. mount the instance to the DOM
 3. update the DOM when data changes.

* Along the way, it also runs functions called lifecycle hooks, giving users the opportunity to add their own code at specific stages.

https://stefanhoelzl.github.io/vue.py/docs/vue_concepts/lifecycle_hooks.html