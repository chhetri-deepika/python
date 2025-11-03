import pyjokes
jokes = pyjokes.get_jokes()
for joke in jokes:
    print(joke)
    # pyjokes is a internal module that provides programming jokes.