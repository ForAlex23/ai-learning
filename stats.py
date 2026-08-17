def count_stats(text):
    lines = text.splitlines()
    words = text.split()
    characters_without_spaces = sum(1 for char in text if not char.isspace())
    longest_line = max(lines, key=len) if lines else ""
    return {
        "number_of_lines": len(lines),
        "total_words": len(words),
        "characters_without_spaces": characters_without_spaces,
        "longest_line": longest_line,
    }
def main():
    file_path = input("Enter the path to the text file: ")
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            text = file.read()
    except FileNotFoundError:
        print("File not found.")
        return
    result = count_stats(text)
    print(f"Number of lines: {result['number_of_lines']}")
    print(f"Number of words: {result['total_words']}")
    print(f"Characters without spaces: {result['characters_without_spaces']}")
    print(f"Longest line: {result['longest_line']}")
if __name__ == "__main__":
    main()
