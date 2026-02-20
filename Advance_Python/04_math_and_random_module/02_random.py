import random

print(random.random())  # Returns a random float number between 0 and 1
print(random.randint(1, 100))  # Returns a random integer between 1 and 10

colors = ['red', 'blue', 'green']
print(random.choice(colors))  # Returns a random element from a list, tuple, or string

numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(numbers)  # Shuffles the elements of a list in place.

print(random.sample(numbers, 3))  # Returns k unique random elements from a sequence.

print(random.uniform(1, 5))  # Returns a random float between a and b.  

# When we store a value in random.seed(n) after that if we call random.randint(a,b) then it return a value, and when we run code again and again then it return same value 
random.seed(100)
print(random.randint(1,100))
print(random.randint(1,100))





