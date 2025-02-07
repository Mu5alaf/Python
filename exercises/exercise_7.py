import pyjokes

def Unpacking(*args):
    jokes = [pyjokes.get_joke(), pyjokes.get_joke(), pyjokes.get_joke()]
    joke_1, *jokes = jokes
    print(jokes)
Unpacking()