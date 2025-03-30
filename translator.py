def translator(phrase):
    translated_phrasee =""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translated_phrasee = translated_phrasee + "G"
            else:
                translated_phrasee = translated_phrasee + "g"

        else:
            translated_phrasee = translated_phrasee + letter
    return translated_phrasee



print(translator(input("Enterr a phrase:  ")))

