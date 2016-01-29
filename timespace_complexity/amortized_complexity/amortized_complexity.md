# Amortized Complexity

As explained in [Wikipedia](https://en.wikipedia.org/wiki/Amortized_analysis) 
and [StackOverflow](http://stackoverflow.com/a/15079679):

> Amortized complexity is the total ex expense per operation, evaluated
> over a sequence of operations. The idea is to guarantee the total
> expense of the entire sequence, while permitting individual operations
> to be much more expensive than the average.


One simple example would be an implementation of `Queue` in Ruby:

``` ruby
class Queue
    def initialize
        @input = []
        @output = []
    end
            
    def enqueue(element)
        @input << element
    end
                    
    def dequeue
        if @output.empty?
            while @input.any?
                @output << @input.pop
            end
        end
            
        @output.pop
    end
end
```

Note that `enqueue` has a complexity of $$O(1)$$, while `dequeue` is $$O(n)$$.

> ..., we can charge the cost of copying any item from the input array to the output 
> array to the earlier enqueue operation for that item. This charging scheme 
> doubles the amortized time for enqueue, but reduces the amortized time for 
> dequeue to O(1).
