def divisible_by_ten(nums):
    count = 0
    for number in nums:
        if(number % 10 == 0):
            count += 1
    return count

print(divisible_by_ten([20, 25, 30, 35, 40]))

def add_greetings(names):
    greeted_names = []
    for name in names:
        greeted_names.append("Hello, " + name)
    return greeted_names

print(add_greetings(["Owen", "Max", "Sophie"]))