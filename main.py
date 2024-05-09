def letter_count(s):
    result = dict()
    for l in s.lower():
        if l not in result:
            result[l] = 0
        result[l] = result[l] + 1
    return result

def sort_char(char):
    return char["count"]

def sort_alpha(char_dict):
    base_arr = []
    for k in char_dict:
        if k.isalpha():
            base_arr.append({'char': k, 'count': char_dict[k]})
    base_arr.sort(reverse=True, key=sort_char)   
    return base_arr

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
        counts = sort_alpha(letter_count(file_contents))

        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{len(words)} found in the document\n")
        for c in counts:
            print(f"The '{c['char']}' character was found {c['count']} times")
        print("--- End report ---")

main()
