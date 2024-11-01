# pip install levenshtein
from xmlrpc.client import MAXINT

from Levenshtein import distance

'''
Шаблон 1: Напечатай все строки длины %ЦЕЛОЕ_ЧИСЛО% из нулей и единиц в лексографическом порядке на языке %[Python, C++]%
Шаблон 2: Отсортируй список детей [%строка%, %строка%,...] по алфавитному порядку
Шаблон 3: Используй %[Python, C++]%, чтобы сказать является ли число %ЦЕЛОЕ_ЧИСЛО% палиндромом
Шаблон 4: Напиши скрипт для одновременной генерации %ЦЕЛОЕ_ЧИСЛО% TXT файлов из %ЦЕЛОЕ_ЧИСЛО% строк случайных целых чисел от %ЦЕЛОЕ_ЧИСЛО% до %ЦЕЛОЕ_ЧИСЛО% на %ЦЕЛОЕ_ЧИСЛО% потоков на языке %[Python, C++]%
Шаблон 5: Используя %[Python, C++]% перейди по ссылке %URL% и проверь, встречается ли в HTML коде веб-страницы слово %СТРОКА%  
Шаблон 6: Выведи через пробел все простые числа от %ЦЕЛОЕ_ЧИСЛО% до %ЦЕЛОЕ_ЧИСЛО% на языке %[Python, C++]%  
'''

T1_C1 = '''
#include <iostream>
#include <string>

using namespace std;

string fanc(int x, int size);

int main()
{   
    
'''
T1_C2 = '''

    for (int i = 0; i < (1 << n); ++i)
    {
        cout << fanc(i, n) << endl;
    }
    return 0;
}


string fanc(int x, int size) {
    string ans;
    while (ans.size() < size) {
        ans.push_back(x % 2 + '0');
        x /= 2;
    }
    reverse(ans.begin(), ans.end());

    return ans;
}
'''
T1_P1 = '''
def func(x, size):
    ans = ''
    while len(ans) < size:
        ans += str(x % 2)
        x = x // 2
    return ''.join(reversed(ans))


if __name__ == '__main__':
'''
T1_P2 = '''
    for i in range(n ** 2):
        print(func(i, n))
'''

T2_C1 = '''
#include <iostream>
#include <fstream>
#include <thread>
#include <vector>
#include <string>

using namespace std;

void fanc(int i);

int main()
{

    vector<thread> threads;
'''
T2_C2 = '''
    {
        threads.emplace_back(thread(fanc, i));
    }

    for (auto& th : threads) {
        th.join();
    }
    return 0;
}


void fanc(int i) {
    srand(Time(0) + i * rand());
    string path = "file";
    path += i + '0';
    path += ".txt";

    ofstream fout;
    fout.open(path);

    if (fout.is_open())
    {
'''
T2_C3 = '''
    }

    fout.close();
}
'''
T2_P1 = '''
from random import randint
from multiprocessing import Pool


def f(counter):
'''
T2_P2 = '''
    with open(f"file{counter}.txt", "w+", encoding="UTF-8") as fout:
        for j in range(rows):
'''
T2_P3 = '''
    p.map(f, tasks)
    p.close()
'''

T3_C1 = '''
#include <iostream>
#include <vector>
#include <cmath>

using namespace std;


bool prime(int i) {
    if (i < 2) return false;
    for (int j = 2; j < sqrt(i) + 1; ++j) {
        if (i % j == 0) return false;
    }
    return true;
}

int main() {
    vector<int> primes;
'''
T3_C2 = '''
    {
        if (prime(i)) primes.emplace_back(i);
    }

    for (int prime : primes) {
        std::cout << prime << ' ';
    }
    return 0;
}
'''


def IsCpp(text):
    return text.lower().find('c++') != -1 or text.lower().find('с++') != -1


if __name__ == '__main__':
    templates = {
        'Напапечатай все строки длины %ЦЕЛОЕ_ЧИСЛО% из нулей и единиц скриптом на языке %[Python, C++]%' : 0,
        'Напиши скрипт для одновременной генерации %ЦЕЛОЕ_ЧИСЛО% TXT файлов в столько же потоков|процессов из %ЦЕЛОЕ_ЧИСЛО% строк случайных целых чисел от %ЦЕЛОЕ_ЧИСЛО% до %ЦЕЛОЕ_ЧИСЛО% на языке %[Python, C++]%': 0,
        'Выведи через пробел все простые числа от %ЦЕЛОЕ_ЧИСЛО% до %ЦЕЛОЕ_ЧИСЛО% на языке %[Python, C++]%': 0
    }

    userRequest = input()
    for T in templates.keys():
        templates[T] = distance(T, userRequest)

    m = MAXINT
    request = 0
    for i, value in enumerate(templates.values()):
        if m > value:
            m = value
            request = i

    print(request)
    with open("output.txt", "w", encoding='UTF-8') as fout:
        if request == 0:
            print("T1")
            n = int(userRequest[userRequest.find(' длин'):].split()[1])

            if IsCpp(userRequest):
                print("C++")
                fout.write(f'\tint n = {n};'.join((T1_C1, T1_C2)))
            else:
                print("Python")
                fout.write(f'    n = {n}'.join((T1_P1, T1_P2)))

        elif request == 1:
            print("T2")
            file_num = int(userRequest[userRequest.find(' генерац'):].split()[1])
            row_num = int(userRequest[:userRequest.find(' строк ')].split()[-1])
            from_num = int(userRequest[userRequest.find(' от '):].split()[1])
            to_num = int(userRequest[userRequest.find(' до '):].split()[1])
            if IsCpp(userRequest):
                print("C++")
                fout.write(T2_C1)
                fout.write(f"    for (int i = 0; i < {file_num}; ++i)\n")
                fout.write(T2_C2)
                fout.write(f"    for (int j = 0; j < {row_num}; ++j)\n")
                fout.write(f'{' ' * 8}fout << {from_num} + rand() % ({to_num} - {from_num} + 1) << endl;\n')
                fout.write(T2_C3)
            else:
                print("Python")
                fout.write(T2_P1)
                fout.write(f"    rows = {row_num}")
                fout.write(T2_P2)
                fout.write(f"{' ' * 12}fout.write(str(randint({from_num}, {to_num})) + '\\n')\n\n\n")
                fout.write('if __name__ == "__main__":\n')
                fout.write(f"    p = Pool(processes={file_num})\n")
                fout.write(f"    tasks = [i for i in range({file_num})]\n")
                fout.write(T2_P3)

        else:
            print("T3")
            from_num = int(userRequest[userRequest.find(' от '):].split()[1])
            to_num = int(userRequest[userRequest.find(' до '):].split()[1])

            if IsCpp(userRequest):
                print("C++")
                fout.write(T3_C1)
                fout.write(f"    for (int i = {from_num}; i < {to_num + 1}; ++i)\n")
                fout.write(T3_C2)
            else:
                print("Python")
                fout.write(f"[print(x, end=' ') for x in range(2, {to_num}) if all(x % i != 0 for i in range(2, int(x**0.5) + 1)) and x > {from_num}]")

