# We are going to represent our products in a map where the keys are strings representing the product's name and the values are numbers representing the product's price.

# Create a map with the following key-value pairs:

# Product name (key)	Price (value)
# Eggs	200
# Milk	200
# Fish	400
# Apples	150
# Bread	50
# Chicken	550
# Create an application which prints out the answers to the following questions:

# How much is the fish?
# What is the most expensive product?
# What is the average price?
# How many products' price is below 300?
# Is there anything we can buy for exactly 125?
# What is the cheapest product?
# The full output of your main method should be the following:

# 400
# Chicken
# 258.33334
# 4
# no
# Bread

map={
 
 "Eggs": 	200,
 "Milk":	200,
 "Fish":	400,
 "Apples":	150,
 "Bread":	50,
"Chicken":	550,
}

# How much is the fish?
print(map.get("Fish"))

# What is the most expensive product?
expensive_value= max(map,key=lambda x:map[x])
print(expensive_value)

# What is the average price?
average_value= sum(list(map.values()))/ len(list(map.values()))
print((average_value))

# How many products' price is below 300?
for keys,values in map.items():
    if values < 300:
        
        print(values)

# Is there anything we can buy for exactly 125?
print(map.get(125,"NO"))

# What is the cheapest product?
cheapest_value= min(map,key=lambda x:map[x])
print(cheapest_value)