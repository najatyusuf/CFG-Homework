from collections import Counter

def generate_phrase(characters, phrase):
    characters_counter = Counter(characters)
    phrase_counter = Counter(phrase)

    if len(characters) < len(phrase):  # characters length less than phrase length
        return False
    else:  # character length greater or equal to phrase length
        if characters_counter == phrase_counter:  # character == phrase
            return True
        elif characters_counter > phrase_counter:
            return True
        else:
            return False  # character length is greater than phrase but does not match


# Example inputs
print('Test True:')
print(generate_phrase("", ""))
print(generate_phrase(" ", " "))
print(generate_phrase("A", ""))
print(generate_phrase("aBc? ", "aBc? "))
print(generate_phrase("abc", "abc"))
print(generate_phrase("ABC", "ABC"))
print(generate_phrase("aabbcc", "abc"))

print('\nTest False:')
print(generate_phrase("cbacba", "aabbccc"))
print(generate_phrase("ABC", "abc"))
print(generate_phrase("abc", "ABC"))