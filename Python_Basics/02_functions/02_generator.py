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