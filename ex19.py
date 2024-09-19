def cheese_and_crackers(cheese_count, cracker_count):
	print(f"You have {cheese_count} cheeses.")
	print(f"You have {cracker_count} boxes of crackers.")
	print("Man, that's enough for a party!")
	print("Get a blanket.\n")


print("We can just give the function numbers directly")
cheese_and_crackers(20, 30)


print("OR, we can use variables from our script")
cheese_amount = 10
cracker_amount = 50

cheese_and_crackers(cheese_amount, cracker_amount)


print("We can do math inside too")
cheese_and_crackers(10 + 20, 5 + 6)


print("And we can combine the two, variables and math")
cheese_and_crackers(cheese_amount + 100, cracker_amount + 1000)
