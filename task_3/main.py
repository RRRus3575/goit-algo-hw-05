import os
from pathlib import Path
import timeit

# Функції алгоритмів пошуку
def knuth_morris_pratt(text, pattern):
    def kmp_table(pattern):
        table = [0] * len(pattern)
        j = 0
        for i in range(1, len(pattern)):
            if pattern[i] == pattern[j]:
                j += 1
                table[i] = j
            else:
                if j != 0:
                    j = table[j - 1]
                    i -= 1
                else:
                    table[i] = 0
        return table

    table = kmp_table(pattern)
    i = j = 0
    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == len(pattern):
            return i - j
        elif i < len(text) and pattern[j] != text[i]:
            if j != 0:
                j = table[j - 1]
            else:
                i += 1
    return -1

def boyer_moore(text, pattern):
    def bad_character_table(pattern):
        table = {}
        for i in range(len(pattern) - 1):
            table[pattern[i]] = len(pattern) - 1 - i
        return table

    bad_char_table = bad_character_table(pattern)
    i = 0
    while i <= len(text) - len(pattern):
        j = len(pattern) - 1
        while j >= 0 and pattern[j] == text[i + j]:
            j -= 1
        if j < 0:
            return i
        else:
            i += bad_char_table.get(text[i + len(pattern) - 1], len(pattern))
    return -1

def rabin_karp(text, pattern):
    d = 256
    q = 101
    n = len(text)
    m = len(pattern)
    p = 0
    t = 0
    h = 1
    for _ in range(m - 1):
        h = (h * d) % q
    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q
    for i in range(n - m + 1):
        if p == t:
            for j in range(m):
                if text[i + j] != pattern[j]:
                    break
            else:
                return i
        if i < n - m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q
            if t < 0:
                t += q
    return -1

# Функція для читання файлів з різними кодуваннями
def read_file_with_encoding(filepath, encodings):
    for encoding in encodings:
        try:
            with open(filepath, 'r', encoding=encoding) as file:
                return file.read()
        except UnicodeDecodeError:
            continue
    raise ValueError(f"Could not read the file with the provided encodings: {encodings}")

# Список кодувань для спроби
encodings = ['utf-8', 'cp1251', 'utf-16']

# Отримання шляху до поточного каталогу скрипту
current_dir = Path(__file__).resolve().parent


text1_path = current_dir / 'стаття_1.txt'
text2_path = current_dir / 'стаття_2.txt'


text1 = read_file_with_encoding(text1_path, encodings)
text2 = read_file_with_encoding(text2_path, encodings)

# Підрядки для пошуку
existing_substring = "алгоритм"  
non_existing_substring = "Вигаданий підрядок"  

# Вимірювання часу для існуючого підрядка в тексті 1
kmp_time_existing_text1 = timeit.timeit(lambda: knuth_morris_pratt(text1, existing_substring), number=10)
bm_time_existing_text1 = timeit.timeit(lambda: boyer_moore(text1, existing_substring), number=10)
rk_time_existing_text1 = timeit.timeit(lambda: rabin_karp(text1, existing_substring), number=10)

# Вимірювання часу для вигаданого підрядка в тексті 1
kmp_time_non_existing_text1 = timeit.timeit(lambda: knuth_morris_pratt(text1, non_existing_substring), number=10)
bm_time_non_existing_text1 = timeit.timeit(lambda: boyer_moore(text1, non_existing_substring), number=10)
rk_time_non_existing_text1 = timeit.timeit(lambda: rabin_karp(text1, non_existing_substring), number=10)

# Вимірювання часу для існуючого підрядка в тексті 2
kmp_time_existing_text2 = timeit.timeit(lambda: knuth_morris_pratt(text2, existing_substring), number=10)
bm_time_existing_text2 = timeit.timeit(lambda: boyer_moore(text2, existing_substring), number=10)
rk_time_existing_text2 = timeit.timeit(lambda: rabin_karp(text2, existing_substring), number=10)

# Вимірювання часу для вигаданого підрядка в тексті 2
kmp_time_non_existing_text2 = timeit.timeit(lambda: knuth_morris_pratt(text2, non_existing_substring), number=10)
bm_time_non_existing_text2 = timeit.timeit(lambda: boyer_moore(text2, non_existing_substring), number=10)
rk_time_non_existing_text2 = timeit.timeit(lambda: rabin_karp(text2, non_existing_substring), number=10)

# Результати
print("Стаття 1 - Існуючий підрядок:")
print(f"KMP: {kmp_time_existing_text1} s, BM: {bm_time_existing_text1} s, RK: {rk_time_existing_text1} s")

print("Стаття 1 - Вигаданий підрядок:")
print(f"KMP: {kmp_time_non_existing_text1} s, BM: {bm_time_non_existing_text1} s, RK: {rk_time_non_existing_text1} s")

print("Стаття 2 - Існуючий підрядок:")
print(f"KMP: {kmp_time_existing_text2} s, BM: {bm_time_existing_text2} s, RK: {rk_time_existing_text2} s")

print("Стаття 2 - Вигаданий підрядок:")
print(f"KMP: {kmp_time_non_existing_text2} s, BM: {bm_time_non_existing_text2} s, RK: {rk_time_non_existing_text2} s")
