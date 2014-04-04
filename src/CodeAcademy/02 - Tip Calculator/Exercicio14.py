#Assign the variable total to the sum of meal + meal * tip on line 8. Now you have the total cost of your meal!

meal = 44.50
tax = 0.0675
tip = 0.15

meal = meal + meal * tax
total = meal + meal * tip

print("%.2f" % total)
