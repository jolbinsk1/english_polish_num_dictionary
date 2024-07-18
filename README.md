# English/Polish Number Translation and Pronunciation

This repository provides functions for translating the numbers 0 and 1,000,000 in English and Polish, along with their pronunciation in both languages. It includes a simple interface to input a number and output its English and Polish words, English pronunciation of the Polish words, and IPA pronunciation.

## Features

- Convert numbers (0 to 1,000,000) to their English and Polish words.
- Write out the English pronunciations for Polish numbers.
- Provide IPA (International Phonetic Alphabet) pronunciations for Polish numbers.

## How to Use 

1) Clone this repository:
```bash
Copy code
git clone https://github.com/yourusername/number-translation.git
cd number-translation
```

2) Run the main script:

``` bash
Copy code
python main.py
Follow the prompts to input an integer between 0 and 1,000,000.

```

## Functions

- `return_IPA(num)`: Returns the IPA pronunciation of a Polish number.
- `IPA_format(num)`: Formats the IPA pronunciation correctly.
- `return_words(num)`: Returns the English words for numbers 0 to 1,000,000.
- `return_words_PL(num)`: Returns the Polish words for numbers 0 to 1,000,000.
- `ENG_pro(num)`: Returns the English pronunciation of a Polish number.
- `answer(num)`: Prints the English and Polish words for the given number, along with their pronunciations.
- `number_translate()`: Prompts the user to input a number between 0 and 1,000,000 and prints the translations and pronunciations.

## Structure

-`english_polish_dictionaries.py`: Contains dictionaries for number words and pronunciations in English and Polish.
-`english_return_function.py`: Contains the return_words function.
-`polish_return_function.py`: Contains the return_words_PL function.
-`polish_eng_pronunciation.py`: Contains the ENG_pro function.
-`IPA_and_format_func.py`: Contains return_IPA and IPA_format functions.
-`final_funcs.py`: Contains answer and number_translate functions.
-`main.py`: Main script that ties everything together.

## Example

```bash 
After running main.py, you will be prompted to enter a number:

Please enter an integer from 0 to 1,000,000 (do not include commas or periods): 123
The output will display the English and Polish words for the number, along with their pronunciations:

English: one hundred twenty-three

Polish: sto dwadzieścia trzy
   * English pronunciation: stoh dvah-DZYEH-shchah tshih
   * IPA pronunciation: / stɔ dvaˈd͡ʑɛɕ.tɕa tʂɨ /
```
