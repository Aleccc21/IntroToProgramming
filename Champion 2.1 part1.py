#Display a welcome message for your program
print("Welcome to the Champion Fiber Cable cost machine")

#Get the company name from the user
company_name = input("Please enter the name of your company")

#Get the number of feet of fiber optic to be installed from the user
cable_lenght = float(input("Please enter the number of feet of fiber cable that is to be installed"))

#Multiply the total cost as the number of feet times $0.87
foot_cost = .87
total_cost = cable_lenght * foot_cost

#Display the calculated information and company name
print("Here is the estimated cost for fiber cable installation for", company_name)
print("Total cost $", total_cost)