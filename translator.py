def translator(phrase):
    translated_phrasee =""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            translated_phrasee = translated_phrasee + "g"
        else:
            translated_phrasee = translated_phrasee + letter
    return translated_phrasee



print(translator(input("Enterr a phrase:  ")))

