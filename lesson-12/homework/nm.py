import threading
import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def check_primes(start, end, result):
    for num in range(start, end):
        if is_prime(num):
            result.append(num)

if __name__ == "__main__":
    start_range = 1
    end_range = 100
    num_threads = 4

    threads = []
    results = [[] for _ in range(num_threads)]

    chunk_size = (end_range - start_range) // num_threads

    for i in range(num_threads):
        start = start_range + i * chunk_size
        end = start_range + (i + 1) * chunk_size if i != num_threads - 1 else end_range
        t = threading.Thread(target=check_primes, args=(start, end, results[i]))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    primes = [prime for sublist in results for prime in sublist]
    primes.sort()
    print("Prime numbers in range:", primes)

import threading
from collections import Counter

lines = [
    "This is a test file.",
    "It contains some words.",
    "Some words appear more than once.",
    "Words, words, words!"
]

def count_words(lines_chunk, counter):
    local_counter = Counter()
    for line in lines_chunk:
        words = line.replace('.', '').replace(',', '').split()
        local_counter.update(words)
    counter.update(local_counter)

num_threads = 2  
chunk_size = len(lines) // num_threads
threads = []
counters = [Counter() for _ in range(num_threads)]

for i in range(num_threads):
    start = i * chunk_size
    end = (i + 1) * chunk_size if i != num_threads - 1 else len(lines)
    t = threading.Thread(target=count_words, args=(lines[start:end], counters[i]))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

total_counter = Counter()
for c in counters:
    total_counter.update(c)

print("Word occurrences:")
for word, count in total_counter.most_common():
    print(f"{word}: {count}")
