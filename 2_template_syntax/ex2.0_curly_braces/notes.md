* Most basic form of data binding is text interpolation using the “Mustache” syntax

* Var updated whenever the data object’s msg property changes.


* Curly braces interpret the data as plain text, not HTML. In order to output real HTML, you will need to use the v-html directive
```<span v-html="rawHtml"></span>```

* The contents of the span will be replaced with the value of the rawHtml property, interpreted as plain HTML
  * data bindings are ignored 

