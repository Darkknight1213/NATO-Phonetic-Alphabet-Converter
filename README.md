
# NATO Phonetic Alphabet Converter

## 📋 Overview  
The **NATO Phonetic Alphabet Converter** is a simple Python program that converts a user-inputted word into its corresponding NATO phonetic alphabet representation. This project is both educational and functional, demonstrating the use of Python data manipulation techniques like dictionary and list comprehensions.

---

## 🚀 Features  
- Converts any word into NATO phonetic alphabet codes.  
- Uses a CSV file to map letters to their phonetic equivalents.  
- Ensures uppercase transformation for consistency with the NATO standard.  
- Easy to use and highly educational for Python learners.

---

## 📂 Files Required  
1. **Python Script (`main.py`)**: The primary script to run the application.  
2. **NATO Phonetic Alphabet CSV (`nato_phonetic_alphabet.csv`)**: A CSV file containing letters and their corresponding phonetic words.  
   - Example format:  
     ```csv
     letter,code
     A,Alfa
     B,Bravo
     ```

---

## 🖥️ How to Run  

### Prerequisites  
1. **Python Installed**: Ensure Python 3.7+ is installed on your system.  

### Steps to Run  
1. Place both `main.py` and `nato_phonetic_alphabet.csv` in the same directory.  
2. Open a terminal/command prompt in the directory.  
3. Run the script:  
   ```bash
   python main.py
   ```
4. Enter a word when prompted, and the program will output the phonetic alphabet for each letter in the word.  

---

## 📈 Example Output  
### Input:  
```text
Enter a Word: Python
```

### Output:  
```text
['Papa', 'Yankee', 'Tango', 'Hotel', 'Oscar', 'November']
```

---

## 🎓 Benefits for Students  
- **Learn Python Concepts**:  
  - Understand dictionary and list comprehensions.  
  - Learn to work with CSV files using the Pandas library.  

- **Practical Usage**:  
  - Understand the NATO phonetic alphabet, commonly used in aviation and military communication.  
  - Learn how to process user input and map it to structured data.  

- **Simple and Modular**:  
  - Encourages the separation of data (CSV) and logic (Python script), a best practice in software development.  

---

## 📜 License  
This project is free to use for educational purposes. Feel free to modify and enhance!  

**Happy Coding! 🚀**
