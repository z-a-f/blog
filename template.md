# Title

This is some description of the problem. Or anything else :)

## Template Subtitle -> you can have some titles probably

You can put your question somewhere here and some codes:

```Python
def question():
    print "Any codes might come in here"
```

To create a "hide button", use

``` html
<button class="section" target="solution" show="Show solution" hide="Hide solution"></button>
```

<button class="section" target="solution" show="Show solution" hide="Hide solution"></button>

The section that you want to be hidden, should be inside the following tag-pair:

``` html
<!--sec data-title="Solution" data-id="solution" data-show=false ces-->
...
<!--endsec-->
```
**Note** that you cannot have titles higher than `####` in the hidden block - Use `####`, `#####`, etc...
<!--sec data-title="Solution" data-id="solution" data-show=false ces-->

Any solution codes would come here.

```Python
def question():
    print "This is an answer!"
```

<!--endsec-->

