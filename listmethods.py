# .count() .insert() .pop() range() .len() .sort() .sorted()

fruits = ["apple", "peach", "banana", "orange", "papaya"]

fruits.insert(2, "guava")

print(fruits)

fruits.pop()

print(fruits)

fruits.pop(0)

print(fruits)

some_range = range(10)
print(list(some_range))

range_diff_3 = range(0, 90, 3)
print(list(range_diff_3))

fruit_len = len(fruits)
print(fruit_len)

more_fruits = ["kiwi", "guava", "mango", "pineapple", "dragonfruit", "lychee"]
print(more_fruits)

sliced_fruits = more_fruits[2:4]
print(sliced_fruits)

favorite_fruit_responses = ["orange", "orange", "apple", "orange", "orange", "orange", "mango", "banana", "banana", "orange", "orange", "persimmon"]

orange_count = favorite_fruit_responses.count("orange")
banana_count = favorite_fruit_responses.count("banana")

print(orange_count)
print(banana_count)

favorite_fruit_responses.sort()
print(favorite_fruit_responses)