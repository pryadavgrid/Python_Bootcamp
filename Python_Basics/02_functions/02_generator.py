# Write a generator function that yield even number up to a specific limit


def even_generator(limit):
    for i in range(2, limit + 1, 2):
        yield i


# print(even_generator(10).__next__())
# print(even_generator(10).__next__())
# print(even_generator(10).__next__())
# print(even_generator(10).__next__())

# my_gen_value = even_generator(10)
# print(my_gen_value.__next__())
# print(my_gen_value.__next__())
# print(my_gen_value.__next__())

for i in even_generator(10):
    print(i)


nums = (x for x in range(5))
# print(nums.__next__())
# print(nums.__next__())



#  it is a way to return a list look like generator but it use more memory
def number_print(num):
    result = []
    for i in range(10):
        result.append(i)

    return result

# simply we loop in list
for i in number_print(10):
    print(i)


#  it is a generator it use less memory because it generate the value when we call
# yield return a value and store in a memory that what we return and what will return in next call
def number_generator(nums):
    for i in range(nums):
        yield i

for i in number_generator(10):
    print(i)