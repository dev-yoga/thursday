weight = 41.5

if weight <= 2:
  ground_cost = weight * 1.50 + 20
elif weight > 2 and weight <= 6: 
  ground_cost = weight * 3.00 + 20
elif weight > 6 and weight <= 10:
  ground_cost = weight * 4.00 + 20
elif weight > 10:
  ground_cost = weight * 4.75 + 20
else:
  print("Error")
print("Ground cost: ", ground_cost)

premium_ground = 125
print("Premium Ground flat rate:", premium_ground)

if weight <= 2:
  drone_cost = weight * 4.50
elif weight > 2 and weight <= 6: 
  drone_cost = weight * 9.00
elif weight > 6 and weight <= 10:
  drone_cost = weight * 12.00
elif weight > 10:
  drone_cost = weight * 14.25
else:
  print("Error")
print("Drone cost: ", round(drone_cost, 2))