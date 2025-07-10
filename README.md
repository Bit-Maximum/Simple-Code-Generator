# 🧠 Simple Code Generator

[![en](https://img.shields.io/badge/lang-en-red.svg)](https://github.com/Bit-Maximum/Simple-Code-Generator/blob/master/README.md)
[![ru](https://img.shields.io/badge/lang-ru-blue.svg)](https://github.com/Bit-Maximum/Simple-Code-Generator/blob/master/Translation/README.ru.md)

> **Lab work for the course “Modern Programming Languages”**

A simple tool that generates code in **Python** or **C++** based on natural language requests.
Demonstrates the use of the **Levenshtein distance algorithm** for matching user queries to predefined templates.

---

## 📌 Project Goal

To demonstrate the ability to match user input in natural language to predefined templates and generate corresponding source code in the selected programming language (Python or C++).

---

## 🧩 How It Works

1. The user enters a request in natural language
   Example: `Напапечатай все строки длины 20 из нулей и единиц скриптом на языке C++`

2. The program compares the request to a set of templates using **Levenshtein distance**  
   It selects the closest matching template

3. The appropriate code is generated
   The target language (**Python** or **C++**) is determined by keywords (e.g., "Python", "C++")

4. The result is saved in `output.txt`

---

## 🔧 Example Usage

```bash
Введите ваш запрос:
Выведи через пробел все простые числа от 5 до 100 на языке Python
```

Output in `generated_code.txt`:

```bash
[print(x, end=' ') for x in range(2, 100) if all(x % i != 0 for i in range(2, int(x**0.5) + 1)) and x > 5]
```

## 🛠️ How to Run
1. Clone the repository:
```bash
git clone https://github.com/Bit-Maximum/Simple-Code-Generator.git
cd Simple-Code-Generator
```
2. Install dependencies (if needed):
```bash
pip install -r requirements.txt
```
3. Run the program:
```bash
python main.py
```

## © Author
_Maksim Merkurev, 2024_
_Laboratory work. Further development as a small-scale project with extended functionality is possible._
