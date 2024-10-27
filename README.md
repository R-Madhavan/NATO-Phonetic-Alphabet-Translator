# NATO Phonetic Alphabet Translator

This project is a simple Python program that converts any user-provided word into its NATO phonetic alphabet equivalent. For example, if the user inputs "hello," the program will output `["Hotel", "Echo", "Lima", "Lima", "Oscar"]`.

## Project Structure

- `main.py`: The main script that prompts the user for input, reads from a CSV file containing the NATO phonetic alphabet, and translates the input into the corresponding phonetic code words.
- `nato_phonetic_alphabet.csv`: A CSV file with each letter of the alphabet and its corresponding NATO phonetic code.

## Setup

1. **Clone or Download the Project**:
   - Clone the repository or download it as a zip file and extract it.

2. **Install Requirements**:
   - This project requires `pandas` for reading and processing the CSV file.
   - To install `pandas`, run:
     ```bash
     pip install pandas
     ```

3. **Run the Program**:
   - In your terminal, navigate to the project directory and run:
     ```bash
     python main.py
     ```

## Usage

1. The program will prompt you to enter a word.
2. Enter any word using letters only (e.g., "Python").
3. The program will output a list of the phonetic code words for each letter in the word, based on the NATO phonetic alphabet.

### Example
eg:1
```
Enter the name?: python
['Papa', 'Yankee', 'Tango', 'Hotel', 'Oscar', 'November']

eg:2
Enter the name?: hello
['Hotel', 'Echo', 'Lima', 'Lima', 'Oscar']
```



