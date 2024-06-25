import re

def remove_special_characters(text):
    # Define a regular expression pattern to match special characters
    # pattern = r'[^\u0C80-\u0CFF\s]'  #kannada This pattern matches anything that is not a letter, digit, or whitespace
    pattern = r'[^\u0D00-\u0D7F\s]' # malayalam
    # Use the sub() function from the re module to replace matched patterns with an empty string
    text = re.sub(pattern, '', text)
    return text

# Read the text corpus from a txt file
file_path = 'mal_testcase.txt'  # Change 'corpus.txt' to the actual file path
with open(file_path, 'r', encoding="utf-8") as file:
    text_corpus = file.readlines()

# Process each line in the text corpus
cleaned_corpus = [remove_special_characters(line) for line in text_corpus]

# Write the cleaned corpus back to the txt file
cleaned_file_path = 'cleaned_mal.txt'  # Change 'cleaned_corpus.txt' to the desired file path
with open(cleaned_file_path, 'w', encoding="utf-8") as file:
    file.writelines(cleaned_corpus)
