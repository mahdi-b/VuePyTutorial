
* Instead of using complex logic in {{}}, you should use a computed property. E.g.:

```
    # instead of 
    <p>Reversed message is {{" ".join(self.message.split()[::-1])}} </p>
    # do
    <p>Reversed message is {{reversedMessage}} </p>
    # with
    @computed
    def reversedMessage(self):
        return " ".join(self.message.split()[::-1])
```



* Vue is aware that reversedMessage depends on message, so it will update any bindings that depend on reversedMessage when message changes. 

And the best part is that we’ve created this dependency relationship declaratively: the computed getter function has no side effects, which makes it easier to test and understand.




* The following computed property will never update, because Date.now() is not a reactive dependency:
```
    @computed
    def now(self):
        return time.time()
```