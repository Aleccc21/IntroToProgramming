#Display a welcome message for your program
print("Welcome to the Champion Fiber Cable cost machine")

#Get the company name from the user
company_name = input("Please enter the name of your company")

#Get the number of feet of fiber optic to be installed from the user
cable_lenght = float(input("Please enter the number of feet of fiber cable that is to be installed"))

#Evaluate the total cost based upon the number of feet requested
if cable_lenght < 101:
  foot_cost = 0.87
elif cable_lenght < 250:
  foot_cost = 0.80
else:
  foot_cost = 0.70
total_cost = cable_lenght * foot_cost
print(f"Your cable per foot cost is ${foot_cost}")

#Display the calculated information and company name
print("Here is the estimated cost for fiber cable installation for", company_name)
print("Total cost $", total_cost)