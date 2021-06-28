* Vue does provide a more generic way to observe and react by  watching properties

# it is often a better idea to use a computed property rather than an imperative watch callback. 

```
@watch("firstName")
def update_full_fname(self, new, old):
    self.full_name = new + self.lastName

@watch("lastName")
def update_full_lname(self, new, old):
    self.full_name = self.fname +  new
```

The above can be easily updated to be

```
@computed
def update_full_name():
    return self.fName = self.lName
```


* While computed properties are more appropriate in most cases, there are times when a custom watcher is necessary. 
 * This is most useful when you want to perform asynchronous or expensive operations in response to changing data.
 * See exmaple in code






