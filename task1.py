# Write your solution to exercise 1 here
words_input = []
count = 0
while True:
    # read user input
    str_input = input("Type in a string: ")

    # check for empty string
    if str_input == "":
        break
    # add each word to list
    words_input.append(str_input)
    count += 1


all_input = ""
length = 0
for word in words_input:
    # check for longest word
    if len(word) > length:
        length = len(word)

    # joining all words
    all_input += word

common_letter = ""
counter = 0
for letter in all_input:
    each = all_input.count(letter)
    if each > counter:
        most_count = each
        common_letter = letter


if __name__ == "__main__":

      # printing result
    print(f"Total number of strings: {count}")
    print(f"The length of the longest string: {length}")
    print(f"The most common character in strings: {common_letter}")

