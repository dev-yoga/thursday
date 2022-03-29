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
favorite_fruit_responses.sort(reverse=True)
print(favorite_fruit_responses)

#the sort method doesn't return any value and thus does not need to be assigned to a variable since it modifies the list directly, if you assign the result of the method it will assign the value of None to the variable

try_again = favorite_fruit_responses.sort()
print(try_again)

#also None
print(favorite_fruit_responses.sort())

#sorted(), however, comes before a list & generates a new lsit rather than modifying the one that already exists

sorted_fruits = sorted(favorite_fruit_responses)
print(sorted_fruits)