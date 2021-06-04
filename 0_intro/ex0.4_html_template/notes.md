External html template

* we need declare the template name
  ```template = "#htmltemplate"```
  * the * indicates the template is an external file

* we need to have an equivalent file
```
  some_index.html
```
* we need to have the mapping in the configuration file `vuepy.yml`
```  
templates:
   htmltemplate : some_index.html
```