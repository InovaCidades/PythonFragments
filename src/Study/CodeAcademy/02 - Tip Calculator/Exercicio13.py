#On line 7, reassign meal to the value of itself + itself * tax. And yes, you're allowed to reassign a variable in terms of itself!
#We're only calculating the cost of meal and tax here. We'll get to the tip soon.

meal = 44.50
tax = 0.0675
tip = 0.15

meal = meal + meal * tax
