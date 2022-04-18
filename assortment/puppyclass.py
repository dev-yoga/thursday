class Puppy:
  def __init__(self, input_name, input_breed, input_age = 0, input_friendliness = True):

      self.name = input_name
      self.breed = input_breed
      self.age = input_age
      self.is_friendly = input_friendliness
  def __str__(self):
    # new way >.>
    return '{} {} {}'.format(self.name, self.breed, self.age)
    # old way:
    #return  '%s %s %s'%(self.name, self.breed, self.age)

puppy_one = Puppy("Finn", "Italian Greyhound", 2)
puppy_two = Puppy("Bailey", "Italian Greyhound", 1)

print(puppy_one)
print(puppy_two)