def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1

    sorted_chars = dict(sorted(chars.items()))
    return sorted_chars

def sort_dict(unsorted_dict):
    sorted_pairs = sorted(unsorted_dict.items(), key=lambda p: p[1], reverse = True)
    new_pairs = []
    for i in range(0, len(sorted_pairs)):
        if sorted_pairs[i][0].isalpha():
            new_pairs.append({"char" : sorted_pairs[i][0], "num" : sorted_pairs[i][1]})
    return new_pairs

# Proposed better version by Boots.Bot:
#def sort_dict(unsorted_dict):
#    sorted_pairs = sorted(
#        unsorted_dict.items(),
#        key=lambda p: p[1],
#        reverse=True,
#    )
#
#    return [
#        {"char": char, "num": count}
#        for char, count in sorted_pairs
#        if char.isalpha()
#    ]