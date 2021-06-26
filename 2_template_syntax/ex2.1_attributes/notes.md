* Mustaches cannot be used inside HTML attributes ->

  * Use v-bind directive instead

```<div v-bind:id="dynamicId"></div>```



```<button v-bind:disabled="isButtonDisabled">Button</button>```

If isButtonDisabled has the value of null, undefined, or false, the disabled attribute will not even be included in the rendered <button> element.

Also use v-html in a span to include HTML content.



