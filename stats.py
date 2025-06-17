def count_words(text):
    text = text.split()
    wc = 0
    for word in text:
        wc += 1
    return wc

def character_count(text):
    text = text.lower()
    count = {}
    for char in text:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    return count

def sort_on(dict):
    return dict["num"]

def get_report(char_count):
    report = []
    for key in char_count:
        report.append({"char": key, "num":char_count[key]})
    report.sort(reverse=True, key=sort_on)
    return report