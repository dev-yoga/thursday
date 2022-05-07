train_mass = 22680
train_acceleration = 10
train_distance = 100

def get_force(mass, acceleration):
  return mass * acceleration

get_force(train_mass, train_acceleration)

def get_work(mass, acceleration, distance):
  force = get_force(mass, acceleration)
  return force * distance
  
train_work = get_work(train_mass, train_acceleration, train_distance)

print("The GE train does", train_work, "Joules of work over", train_distance, "meters.")