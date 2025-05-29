# Convert-Persian-numbers-to-English
This Python script defines a function Convert_Persian_numbers_to_English that replaces Persian digits in a given text with their English equivalents.

Function Breakdown:

Mapping Dictionary: A dictionary persian_engilsh maps Persian numerals ('۰' to '۹') to English numerals ('0' to '9').

Character Iteration: The function iterates through each character in the input text:

If the character is a Persian digit, it replaces it with the corresponding English digit.

If the character is not a Persian digit, it remains unchanged.

Output: The converted characters are printed consecutively without line breaks.

Execution Flow:

The execution function prompts the user to input text.

It then calls Convert_Persian_numbers_to_English to process and display the converted text.

Use Cases:

Processing user input that may contain Persian numerals.

Standardizing numerical data for systems that require English digits.

Preprocessing text data for applications like data analysis or machine learning.
