# We are going to represent our contacts in a map where both the keys and values are strings.

# Create a map with the following key-value pairs:

# Name (key)	Phone number (value)
# William A. Lathan	405-709-1865
# John K. Miller	402-247-8568
# Hortensia E. Foster	606-481-6467
# Amanda D. Newland	319-243-5613
# Brooke P. Askew	307-687-2982
# Create an application which prints out the answers to the following questions:

# What is John K. Miller's phone number?
# Whose phone number is 307-687-2982?
# Do we know Chris E. Myers' phone number? (yes/no)

map={
    "William A. Lathan" :	"405-709-1865",
"John K. Miller" :	"402-247-8568",
"Hortensia E. Foster" :	"606-481-6467",
"Amanda D. Newland" :	"319-243-5613",
"Brooke P. Askew" :	"307-687-2982"
}

# displaying John K. Miller number 
print(map.get("John K. Miller"))

# display number for 307-687-2982
for key,value in map.items():
     if value =='307-687-2982':
         print (key)

# displaying if Chris E. Myer's number is available
print(map.get("Chris E. Myers","no"))
