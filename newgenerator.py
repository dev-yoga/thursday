def username_generator(first_name, last_name):
  username = first_name[0:3] + last_name[0:4]
  return username

username_generator("Bob", "Smith")