import sys
import pandas

if len(sys.argv) != 2:
    print("Usage: bookbot <path_to_file>")
    sys.exit(1)

filepath = sys.argv[1]

try:
    with open(filepath) as f:
        book_string = f.read().lower()

        char_count = {}
        for char in book_string:
            if char not in char_count and char.isalpha():
                char_count[char] = 1
            elif char.isalpha():
                char_count[char] += 1

        list_of_words = book_string.split()
        cleaned_list = []
        for word in list_of_words:
            word = "".join([char for char in word if char.isalpha()])
            cleaned_list.append(word)
        unique_words = set(cleaned_list)
        sorted_list = sorted(list(unique_words))

        print(f"Number of words: {len(list_of_words)}")
        print(f"Unique words: {len(sorted_list)}")

        data = {"Char": char_count.keys(), "Times": char_count.values()}
        df = pandas.DataFrame(data)
        sorted_df = df.sort_values(by="Times", ascending=False)
        sorted_df["Times"] = sorted_df["Times"].apply(lambda x: format(x, ","))
        print(sorted_df.to_string(index=False))
except FileNotFoundError:
    print("File not found. Please check filepath and try again.")
except Exception as e:
    print(f"An error occured: {e}")
