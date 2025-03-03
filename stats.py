def word_count(path_to_file):
	count_string = ""
	count_string = path_to_file.split()
	words = len(count_string)
	return words

def character_count(path_to_file):
	lowercase = ""
	letters = {}
	count_string = ""
	count_string = path_to_file.split()
	for word in count_string:
		lowercase += word.lower()
	for letter in lowercase:
		if letter not in letters:
			letters[letter] = 0
		letters[letter] += 1
	return letters

def dict_sort(dict_input):
	char_list = []
	for char, count in dict_input.items():
		char_list.append({"char": char, "count": count})

	def sort_on(dict_item):
		return dict_item["count"]

	char_list.sort(reverse=True, key=sort_on)
	return char_list
