def get_word_count(text):
    return (len(text.split()))

def get_characters(text):
    characters = {}
    for char in text:
        lowered = char.lower()
        if lowered in characters:
            characters[lowered] += 1
        else:
            characters[lowered] = 1
    return characters

def sort_on(d):
    return d["num"]

def sort_characters(characters):
    sorted = []
    for ch in characters:
        sorted.append({"char": ch, "num": characters[ch]})
    sorted.sort(reverse=True, key=sort_on)
    return sorted