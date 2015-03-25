from random import randint

def remix(ingredients):
    alcohols = []
    mixers = []
    for pair in ingredients:
        alcohols.append(pair[0])
        mixers.append(pair[1])
    drinks = []
    for alc in alcohols:
        mixer = mixers.pop(randint(0, len(mixers) - 1))
        drinks.append([alc, mixer])
    return drinks

print(remix([
  ["rum", "coke"],
  ["gin", "tonic"],
  ["scotch", "soda"]
]))
