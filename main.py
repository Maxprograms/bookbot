def read_file(book_file):
    with open(book_file) as f:
        file_contents = f.read()
        return(file_contents)

def count_words(text):
    count = 0
    words = text.split()
    for word in words:
        count += 1
    return count

def count_characters(text):
    characters = list(text.lower())
    count_map = {}
    for character in characters:
        if character not in count_map:
            count_map[character] = 1
        else:
            count_map[character] += 1
    return dict(sorted(count_map.items(), key=lambda item: item[1], reverse=True))


def main():
    book = "books/frankenstein.txt"
    print(f'--- Begin report of {book} ---')
    print(count_words(read_file(book)))
    character_dictionary = count_characters(read_file(book))
    for character in character_dictionary:
        print(f'The {character} character was found {character_dictionary[character]} times.')

if __name__ == "__main__":
    main()