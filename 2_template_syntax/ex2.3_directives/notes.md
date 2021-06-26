* Directives are special attributes with the v- prefix.
* A directive’s job is to reactively apply side effects to the DOM when the value of its expression changes.


* Some directives can take an “argument”, denoted by a colon after the directive name.
    * v-bind directive is used to reactively update an HTML attribute:

    ```<a v-bind:href="url"> ... </a>```

* Another example is the v-on directive, which listens to DOM events:

```<a v-on:click="doSomething"> ... </a>```



* Can also use an expression in a directive argument by wrapping it with square brackets:


```<a v-bind:[attributeName]="url"> ... </a>```

* Similarly, you can use dynamic arguments to bind a handler to a dynamic event name:
  * below, this means on click -> do something

```	   eventName = "click"

	   <a v-on:[eventName]="doSomething"> ... </a>
```


* Modifiers are special postfixes denoted by a dot, which indicate that a directive should be bound in some special way.

  * example, the .prevent modifier tells the v-on directive to call event.preventDefault() on the triggered event:

  ```<form v-on:submit.prevent="onSubmit"> ... </form>```

