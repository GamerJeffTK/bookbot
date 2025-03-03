import sys
def get_book_text(path_to_file):
	file_contents = ""
	char_dict = {}
	with open(path_to_file) as f:
		file_contents = f.read()
		num_words = word_count(file_contents)
		char_dict = character_count(file_contents)
		sorted_dict = dict_sort(char_dict)
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {path_to_file}...")
	print("----------- Word Count ----------")
	print(f"Found {num_words} total words")
	print("--------- Character Count -------")

	# Print each character and its count on a separate line
	for item in sorted_dict:
		if item["char"].isalpha():
			print(f"{item['char']}: {item['count']}")
	print("============= END ===============")

from stats import word_count
from stats import character_count
from stats import dict_sort

def main():
	if len(sys.argv) != 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	book_path = sys.argv[1]
	get_book_text(book_path)


main()
