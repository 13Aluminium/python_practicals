def reverse_words(string):
    words = string.split()
    reversed_words = words[::-1]
    return " ".join(reversed_words)

string = input("Enter a long string containing multiple words: ")
reversed_string = reverse_words(string)

print(reversed_string)

print("21DCE052")