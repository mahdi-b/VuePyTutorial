
* Using v-if and v-for together is not recommended. See the style guide for further information.

* v-for directive renders a list of items based on an input array.
  * The v-for directive requires a special syntax in the form of `item in items`,
    * `items` is the source data array and `item` is an alias for the array element being iterated on


* v-for also supports an optional second argument for the index of the current item.
<ul id="example-2">
  <li v-for="(item, index) in items">
    {{ index }} - {{ item.message }}
  </li>
</ul>

* V-for can also work on to iterate over the properties of a dictionary


* To give Vue a hint so that it can track each node’s identity, and thus reuse and reorder existing elements, you need to provide a unique key attribute for each item:

