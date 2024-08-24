def main():
	book_dir = "books/frankenstein.txt"
	file_contents = retrieve_book_text(book_dir)
	words_count = word_count(file_contents)
	char_count = unique_char_count(file_contents)
	sorted_char_count = sort_char_count(char_count)
	print(f"----- begin report of {book_dir} -----")
	print()
	print(f"{words_count} words found in the document")
	print()
	for item in sorted_char_count:
		if not item["char"].isalpha():
			continue
		print(f"The '{item['char']}' character was found {item['num']} times")
	print("----- end report -----")

# retrieves the text of the book
def retrieve_book_text(book_directory):
	with open(book_directory) as f:
		return f.read()

# counts the number of words in the book
def word_count(book_text):
	words = book_text.split()
	return len(words)

# counts the number of unique letter characters in the book
def unique_char_count(book_text):
	alpha_bet = "abcdefghijklmnopqrstuvwxyz"
	lowered_frank = book_text.lower()
	counter_dict = {}
	for letter in alpha_bet:
		counter_dict[letter] = 0
	for letter in alpha_bet:
		for char in range(len(lowered_frank)):
			if letter == lowered_frank[char]:
				counter_dict[letter] += 1
	return counter_dict

# A function that takes a dictionary and returns the value of the "num" key
# This is how the `.sort()` method knows how to sort the list of dictionaries
def sort_on(char_count_list):
	return char_count_list["num"]

# sorts the unique characters into a list from most to least
def sort_char_count(character_count):
    sorted_char_list = []
    for ch in character_count:
        sorted_char_list.append({"char": ch, "num": character_count[ch]})
    sorted_char_list.sort(reverse=True, key=sort_on)
    return sorted_char_list

main()
