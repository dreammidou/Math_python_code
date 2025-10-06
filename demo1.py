import random
import string
import time
import threading
import math
from collections import Counter, defaultdict
from typing import List, Dict, Any, Callable

# --- Utilities ---

def random_string(length=8):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def timer(func: Callable):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"Function '{func.__name__}' executed in {time.time() - start:.4f}s")
        return result
    return wrapper

# --- Data Structures ---

class Node:
    def __init__(self, value: Any):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value: Any):
        if not self.head:
            self.head = Node(value)
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = Node(value)

    def to_list(self):
        result = []
        curr = self.head
        while curr:
            result.append(curr.value)
            curr = curr.next
        return result

# --- Algorithms ---

@timer
def quicksort(arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return arr
    pivot = arr[random.randint(0, len(arr) - 1)]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def fibonacci(n: int) -> int:
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, a + b
    return b

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def primes_up_to(n: int) -> List[int]:
    return [x for x in range(2, n+1) if is_prime(x)]

# --- Multithreading Example ---

def worker(name, count):
    for i in range(count):
        print(f"Worker {name}: {i}")
        time.sleep(0.01)

def run_threads():
    threads = []
    for i in range(3):
        t = threading.Thread(target=worker, args=(f"T{i+1}", 5))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

# --- File I/O Example ---

def write_random_file(filename: str, lines: int = 10):
    with open(filename, 'w') as f:
        for _ in range(lines):
            f.write(random_string(16) + '\n')

def read_file(filename: str) -> List[str]:
    with open(filename, 'r') as f:
        return f.readlines()

# --- Data Analysis Example ---

def word_count(text: str) -> Dict[str, int]:
    words = text.lower().split()
    return dict(Counter(words))

def most_common_words(text: str, n: int = 5) -> List[str]:
    counts = word_count(text)
    return sorted(counts, key=counts.get, reverse=True)[:n]

# --- Decorators and Higher-Order Functions ---

def repeat(n: int):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def hello():
    print("Hello, world!")

# --- Class Inheritance Example ---

class Animal:
    def speak(self):
        return "..."

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# --- Main Demo ---

def main():
    print("=== LinkedList Demo ===")
    ll = LinkedList()
    for i in range(5):
        ll.append(random_string(5))
    print("LinkedList contents:", ll.to_list())

    print("\n=== Quicksort Demo ===")
    arr = [random.randint(0, 100) for _ in range(20)]
    print("Original:", arr)
    sorted_arr = quicksort(arr)
    print("Sorted:", sorted_arr)

    print("\n=== Fibonacci Demo ===")
    for i in range(10):
        print(f"fib({i}) = {fibonacci(i)}")

    print("\n=== Primes Demo ===")
    print("Primes up to 30:", primes_up_to(30))

    print("\n=== Multithreading Demo ===")
    run_threads()

    print("\n=== File I/O Demo ===")
    filename = "demo.txt"
    write_random_file(filename, 5)
    print("File contents:", read_file(filename))

    print("\n=== Data Analysis Demo ===")
    text = "hello world hello python python code code code"
    print("Word count:", word_count(text))
    print("Most common words:", most_common_words(text))

    print("\n=== Decorator Demo ===")
    hello()

    print("\n=== Inheritance Demo ===")
    animals = [Dog(), Cat(), Animal()]
    for a in animals:
        print(f"{a.__class__.__name__} says: {a.speak()}")

if __name__ == "__main__":
    main()