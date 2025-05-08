# Persian Text Preprocessing

## Overview
This script reshapes and processes Persian text, performs tokenization, removes unwanted symbols, and applies specific word transformations. It also handles bidirectional text display for accurate representation of Persian text in environments that don't naturally support right-to-left languages.

## Requirements
- Python 3.x
- **Libraries**:
  - `arabic_reshaper`: for reshaping Arabic/Persian text
  - `bidi.algorithm`: for handling bidirectional text
  - `re`: for regular expression operations

To install the required libraries, use:

```bash
pip install arabic-reshaper python-bidi

## Functionality
Text Reshaping:

The input Persian text is reshaped using the arabic_reshaper library, which is necessary for displaying Persian text correctly in environments like consoles or certain IDEs.

Bidirectional Text Display:

The reshaped text is processed with get_display() from bidi.algorithm to ensure correct display for right-to-left languages.

Word Extraction and Tokenization:

The script extracts words and symbols from the reshaped text using regular expressions.

It handles punctuation, special characters, and spaces to ensure that only relevant text remains for further processing.

Stemming:

The script applies a series of regular expressions to remove common Persian word suffixes, such as those for tense or pluralization.

Custom patterns are used for stemming specific Persian words, removing non-informative parts of the words.

Text Cleaning:

Unwanted symbols, such as punctuation and certain Persian stop words, are removed from the text.

The script also converts certain terms, such as "bps" to "bit per second" for clarity.

Final Output:

The cleaned, reshaped, and tokenized text is printed to the console for inspection.
