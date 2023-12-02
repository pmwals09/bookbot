def main():
    path = "./books/frankenstein.txt"
    report(path)


def report(path):
    contents = get_contents(path)
    words = count_words(contents)
    character_list = get_character_list(contents)
    print(f"--- Begin report for {path} ---")
    print(f"{words} found in the document")
    print()
    for c in character_list:
        print(f"The '{c['character']}' character was found {c['count']} times")
    print("--- End report ---")


def get_contents(path):
    with open(path) as f:
        return f.read()


def count_words(text):
    words = text.split()
    return len(words)


def get_character_list(text):
    character_counts = count_characters(text)
    character_list = []
    for c in character_counts:
        if c.isalpha():
            character_list.append({
                "character": c,
                "count": character_counts[c]
            })
    character_list.sort(key=lambda x: x["count"], reverse=True)
    return character_list


def count_characters(text):
    counts = {}
    for c in text:
        if c.lower() in counts:
            counts[c.lower()] += 1
        else:
            counts[c.lower()] = 1
    return counts


main()
