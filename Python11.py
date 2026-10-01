print("\n TASK 1")
class NumberIterator:
    def __init__(self):
        self.current = 1   # starting point

    def __iter__(self):
        return self        # returns the iterator object itself

    def __next__(self):
        if self.current <= 10:
            num = self.current
            self.current += 1
            return num
        else:
            raise StopIteration   # signals the end of iteration


# Using the custom iterator
numbers = NumberIterator()

for n in numbers:
    print(n)
print("\n TASK 2")

# Define a list of colors
colors = ["Red", "Green", "Blue", "Yellow"]

# Create an iterator object from the list
color_iterator = iter(colors)

# Manually iterate using next()
print(next(color_iterator))  # First element → Red
print(next(color_iterator))  # Second element → Green
print(next(color_iterator))  # Third element → Blue
print(next(color_iterator))  # Fourth element → Yellow
print("\n TASK 3")

class ReverseIterator:
    def __init__(self, text):
        self.text = text
        self.index = len(text) - 1   # start from last character

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= 0:
            char = self.text[self.index]
            self.index -= 1
            return char
        else:
            raise StopIteration   # end of iteration


# Example usage
word = "Python"
rev_iter = ReverseIterator(word)

for ch in rev_iter:
    print(ch)
print("\n TASK 4")

class EvenIterator:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        # Move forward until we find an even number
        while self.current <= self.end:
            if self.current % 2 == 0:
                num = self.current
                self.current += 1
                return num
            self.current += 1
        raise StopIteration   # End of iteration


# Example usage
evens = EvenIterator(1, 20)

for n in evens:
    print(n)
print("\n TASK 5")

# Define a tuple of names
names = ("Alice", "Bob", "Charlie", "David")

# Create an iterator object from the tuple
name_iterator = iter(names)

# Manually iterate using next()
print(next(name_iterator))  # First → Alice
print(next(name_iterator))  # Second → Bob
print(next(name_iterator))  # Third → Charlie
print(next(name_iterator))  # Fourth → David
print("\n TASK 6")

class CountdownIterator:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= 1:
            num = self.current
            self.current -= 1
            return num
        else:
            raise StopIteration   # end of iteration


# Example usage
countdown = CountdownIterator(10)

for n in countdown:
    print(n)
print("\n TASK 7")

class StepIterator:
    def __init__(self, start, end, step):
        self.current = start
        self.end = end
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.end:
            num = self.current
            self.current += self.step
            return num
        else:
            raise StopIteration   # end of iteration


# Example usage
step_iter = StepIterator(0, 20, 3)

for n in step_iter:
    print(n)
print("\n TASK 8")

class CircularIterator:
    def __init__(self, items):
        self.items = items
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        # Always return the current item, then move to the next
        item = self.items[self.index]
        self.index = (self.index + 1) % len(self.items)  # wrap around
        return item


# Example usage
cycle = CircularIterator(["A", "B", "C"])

# Print first 10 elements to demonstrate cycling
for i in range(10):
    print(next(cycle))
print("\n TASK 9")

class PrimeIterator:
    def __init__(self, limit):
        self.limit = limit
        self.current = 2   # start from the first prime

    def __iter__(self):
        return self

    def __next__(self):
        while self.current <= self.limit:
            if self.is_prime(self.current):
                num = self.current
                self.current += 1
                return num
            self.current += 1
        raise StopIteration   # end of iteration

    def is_prime(self, n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True


# Example usage
primes = PrimeIterator(50)

for p in primes:
    print(p)
print("\n TASK 10")

class FibonacciIterator:
    def __init__(self, limit):
        self.limit = limit
        self.a, self.b = 0, 1   # starting values

    def __iter__(self):
        return self

    def __next__(self):
        if self.a <= self.limit:
            num = self.a
            self.a, self.b = self.b, self.a + self.b  # update values
            return num
        else:
            raise StopIteration   # end of iteration


# Example usage
fib = FibonacciIterator(50)

for n in fib:
    print(n)
print("\n TASK 11")

# Open the file in read mode
with open("data.txt", "r") as f:
    # Create an iterator from the file object
    file_iterator = iter(f)

    # Manually iterate using next()
    try:
        while True:
            line = next(file_iterator)   # get next line
            print(line.strip())          # strip removes extra newline
    except StopIteration:
        pass   # end of file reached
print("\n TASK 12")

import time
import random

def data_stream(limit=10):
    """Simulates a live data stream using yield."""
    for _ in range(limit):
        # Simulate a new data point (e.g., stock price or sensor reading)
        value = round(random.uniform(100, 200), 2)   # random float between 100–200
        yield value
        time.sleep(1)   # simulate real-time delay (1 second)


# Example usage
for data in data_stream(5):   # stream 5 data points
    print("Live Data:", data)
print("\n TASK 13")

class PaginationIterator:
    def __init__(self, data, page_size=5):
        self.data = data
        self.page_size = page_size
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.data):
            # Slice the next page
            page = self.data[self.index:self.index + self.page_size]
            self.index += self.page_size
            return page
        else:
            raise StopIteration   # no more pages


# Example usage
large_dataset = list(range(1, 26))  # dataset of 25 items
pages = PaginationIterator(large_dataset, 5)

for page in pages:
    print("Page:", page)
print("\n TASK 14")

def number_generator():
    for i in range(1, 11):
        yield i   # yield one number at a time

# Example usage
for num in number_generator():
    print(num)
print("\n TASK 15")

def even_numbers():
    for i in range(2, 51, 2):   # start at 2, step by 2
        yield i

# Example usage
for num in even_numbers():
    print(num)
print("\n TASK 16")

def square_generator():
    for i in range(1, 11):
        yield i * i   # yield the square of i

# Example usage
for num in square_generator():
    print(num)
print("\n TASK 17")

def prime_generator(n):
    count = 0
    num = 2   # start from the first prime
    while count < n:
        if is_prime(num):
            yield num
            count += 1
        num += 1

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True


# Example usage: first 10 primes
for p in prime_generator(10):
    print(p)
print("\n TASK 18")

def char_generator(text):
    for ch in text:
        yield ch   # yield each character

# Example usage
for c in char_generator("PYTHON"):
    print(c)
print("\n TASK 19")

def fibonacci_generator():
    a, b = 0, 1
    while True:   # infinite loop
        yield a
        a, b = b, a + b   # update values


# Example usage: print first 15 Fibonacci numbers
fib = fibonacci_generator()

for _ in range(15):
    print(next(fib))
print("\n TASK 20")

def countdown_generator(start):
    while start >= 0:
        yield start
        start -= 1   # decrease by 1 each time

# Example usage
for num in countdown_generator(10):
    print(num)
print("\n TASK 21")

def file_line_generator(filename):
    with open(filename, "r") as f:
        for line in f:
            yield line.strip()   # yield each line, removing extra newline


# Example usage
for line in file_line_generator("data.txt"):
    print(line)
print("\n TASK 22")

import random
import string

def password_generator(length=12, count=5):
    """Generates random passwords with uppercase, lowercase, digits, and special characters."""
    chars = string.ascii_letters + string.digits + string.punctuation
    for _ in range(count):
        password = ''.join(random.choice(chars) for _ in range(length))
        yield password


# Example usage
for pwd in password_generator(length=12, count=3):
    print("Generated Password:", pwd)
print("\n TASK 23")

def alternating_generator():
    n = 1
    while True:   # infinite loop
        yield n
        yield -n
        n += 1


# Example usage: print first 10 values
gen = alternating_generator()

for _ in range(10):
    print(next(gen))
print("\n TASK 24")

def error_log_reader(filename):
    with open(filename, "r") as f:
        for line in f:
            if "ERROR" in line:   # filter only error messages
                yield line.strip()


# Example usage
for error in error_log_reader("system.log"):
    print("Error Found:", error)
print("\n TASK 25")

def triangular_generator(limit):
    """Yields triangular numbers up to the given limit (count of terms)."""
    n = 1
    while n <= limit:
        yield n * (n + 1) // 2   # triangular number formula
        n += 1


# Example usage: first 10 triangular numbers
for t in triangular_generator(10):
    print(t)
print("\n TASK 26")

import uuid

def session_id_generator(count=5):
    """Generates unique session IDs using UUID4."""
    for _ in range(count):
        yield str(uuid.uuid4())   # convert UUID object to string


# Example usage
for sid in session_id_generator(5):
    print("Session ID:", sid)
print("\n TASK 27")

def number_generator():
    for i in range(1, 6):
        yield i   # yield one number at a time

# Example usage
for num in number_generator():
    print(num)
print("\n TASK 28")

def square_generator():
    for i in range(1, 11):
        yield i * i   # yield the square of i

# Example usage
for num in square_generator():
    print(num)
print("\n TASK 29")

def fibonacci_upto(limit):
    a, b = 0, 1
    while a <= limit:
        yield a
        a, b = b, a + b   # update values


# Example usage: Fibonacci numbers up to 50
for num in fibonacci_upto(50):
    print(num)
print("\n TASK 30")

def odd_generator():
    for i in range(1, 51, 2):   # step by 2 gives only odd numbers
        yield i

# Example usage
for num in odd_generator():
    print(num)
print("\n TASK 31")

def string_length_generator(strings):
    for s in strings:
        yield len(s)   # yield the length of each string

# Example usage
words = ["Python", "AI", "Generator", "Code", "Sowjanya"]
for length in string_length_generator(words):
    print(length)
print("\n TASK 32")

def file_reader(filename):
    with open(filename, "r") as f:
        for line in f:
            yield line.strip()   # yield each line, removing newline


# Example usage
for line in file_reader("bigdata.txt"):
    print(line)
print("\n TASK 33")

def prime_generator(limit):
    for num in range(2, limit + 1):
        if is_prime(num):
            yield num

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


# Example usage: primes up to 50
for p in prime_generator(50):
    print(p)
print("\n TASK 34")

def custom_range(start, stop, step=1):
    """Generator that mimics range() behavior."""
    current = start
    while (step > 0 and current < stop) or (step < 0 and current > stop):
        yield current
        current += step


# Example usage
for num in custom_range(1, 10, 2):
    print(num)
print("\n TASK 35")

def uppercase_generator(words):
    for word in words:
        yield word.upper()   # convert each word to uppercase

# Example usage
words = ["python", "generator", "code", "practice", "sowjanya"]
for w in uppercase_generator(words):
    print(w)
print("\n TASK 36")

import requests

def api_data_generator(base_url, params=None, page_param="page", start_page=1):
    """Generator that fetches paginated API data page by page."""
    page = start_page
    while True:
        # Add page number to query params
        query_params = params.copy() if params else {}
        query_params[page_param] = page

        response = requests.get(base_url, params=query_params)
        if response.status_code != 200:
            break   # stop if request fails

        data = response.json()
        if not data or len(data) == 0:
            break   # stop if no more data

        yield data   # yield one page of results
        page += 1


# Example usage (dummy API)
for page_data in api_data_generator("https://jsonplaceholder.typicode.com/posts", params={}, page_param="_page"):
    print("Page:", page_data[:2])   # show first 2 items from each page
print("\n TASK 37")

def infinite_counter(start=1):
    """Generator that yields an infinite sequence of numbers incrementing by 1."""
    n = start
    while True:   # infinite loop
        yield n
        n += 1


# Example usage: print first 10 numbers
gen = infinite_counter()
for _ in range(10):
    print(next(gen))
print("\n TASK 38")

def alternating_values(val1="A", val2="B"):
    """Generator that alternates between two values infinitely."""
    while True:
        yield val1
        yield val2


# Example usage: print first 10 values
gen = alternating_values()
for _ in range(10):
    print(next(gen))
print("\n TASK 39")

import random

def dice_rolls():
    """Generator that simulates rolling a dice infinitely."""
    while True:
        yield random.randint(1, 6)   # random number between 1 and 6


# Example usage: roll dice 10 times
gen = dice_rolls()
for _ in range(10):
    print("Rolled:", next(gen))
