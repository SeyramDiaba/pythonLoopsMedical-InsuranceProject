names = ["Judith", "Abel", "Tyson", "Martha", "Beverley", "David", "Anabel"]
estimated_insurance_costs = [1000.0, 2000.0, 3000.0, 4000.0, 5000.0, 6000.0, 7000.0]
actual_insurance_costs = [1100.0, 2200.0, 3300.0, 4400.0, 5500.0, 6600.0, 7700.0]

########################################
#Original first loop#                  #
# # Add your code here                 #
# total_cost= 0                        # 
# for actual in actual_insurance_costs:#
#   total_cost += actual               #
########################################

#EXTRA activity while loop# 
total_cost= 0
n=0
while n < len(actual_insurance_costs):
  total_cost += actual_insurance_costs[n]
  n += 1


# Average cost
average_cost= total_cost/len(actual_insurance_costs)
print("Average Insurance Cost: "+ str(average_cost)+" dollars")
#Using Range in loops

for i in range(0,len(names)):
  name=names[i]
  insurance_cost=actual_insurance_costs[i]
  far_or_above_estimated_cost=insurance_cost-estimated_insurance_costs[i]
  print("The insurance cost for " + name + " is "+ str(insurance_cost) + " dollars.")
  if far_or_above_estimated_cost < 0:
    print(name + " is below by estimated cost by: " + str(far_or_above_estimated_cost) + " dollars")
  else:
    print(name + " is above estimated cost by: " + str(far_or_above_estimated_cost) + " dollors")
  if insurance_cost > average_cost :
    print("The insurance cost for "+name+" is above average.")
  elif insurance_cost < average_cost:
      print("The insurance cost for "+name+" is below average.")
  else:
        print("The insurance cost for "+name+" is equal to the average")

#Creating List Comprehension
updated_estimated_costs = [estimated_insurance_cost*(11/10) for estimated_insurance_cost in estimated_insurance_costs]
print(updated_estimated_costs)




