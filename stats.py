file_path = input("Enter the path to the text file: ")

try:
    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()

    lines = text.splitlines()
    words = text.split()

    number_of_lines = len(lines)
    total_words = len(words)

    characters_without_spaces = sum(
        1 for char in text
        if not char.isspace()
    )

    if lines:
        longest_line = max(lines, key=len)
    else:
        longest_line = ""

    print(f"Number of lines: {number_of_lines}")
    print(f"Number of words: {total_words}")
    print(f"Characters without spaces: {characters_without_spaces}")
    print(f"Longest line: {longest_line}")


except FileNotFoundError:
    print("File not found.")

input("Press Enter to continue...")