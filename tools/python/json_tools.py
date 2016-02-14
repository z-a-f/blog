
import json

"""
Convert the input variables to JSON format

Usage:
> a = 12
> b = 42
> import json_tools
> json_tools.vars2json('test.json', a=a, b=b)

@param fName File name to be saved
@param **kwargs dictionary type of input
"""
def vars2json(fName, **kwargs):
    with open(fName, 'w') as f:
        json.dump(kwargs, f)

        
"""
Convert the input JSON filename to variables

Usage:
> import json_tools
> vars = json_tools.json2vars('test.json')
> print vars['a'], vars['b']  # These are the variables stored in 'test.json'

@param fName File name to be opened
@returns Dictionary with all variables :)
"""
def json2vars(fName):
    out = None
    with open(fName, 'r') as f:
        out = json.load(f)
    return out
