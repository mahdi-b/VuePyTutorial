
* The directive v-if is used to conditionally render a block.
  * The block will only be rendered if the directive’s expression returns a truthy value.
```
<h1 v-if="awesome">Vue is awesome!</h1>
```

* v-if can be used with template to create an invisible wrapper
```
    <div v-if="isValid">
        <p>Yes Valid  1</p>
        <p>Yes Valid  2</p>
    </div>
```
versus
```
    <template v-if="isValid">
	<p>Yes Valid  1</p>
	<p>Yes Valid  2</p>
    </template>
```

* You can use the v-else directive to indicate an “else block” for v-if
  *  can also v-else-if


```
<div v-if="Math.random() > 0.75">
  A
</div>
<div v-else-if="Math.random() > 0.25">
  B
</div>
<div v-else>
  C
</div>
```

* Can also use v-show doesn’t support the <template> element, nor does it work with v-else.
  