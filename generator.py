first_name = "samo"
last_name = "burja"

def generator(first_name, last_name):
  return first_name[len(first_name)-3:] + last_name[len(last_name)-3:]

temp_password = generator(first_name, last_name)

print(temp_password)

#saving this because it could be a fun generator to iterate on