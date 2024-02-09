fruits = ["mango","mango",  "angur", "lichi"]
# print(fruits[0])
# print(fruits[-0])
# print(fruits[-1])
# print(fruits[-5])


# for fr in fruits:
#     print(fr , end="  ")

# print()
# for f in fruits[-1 : -3 : -1] :
#     print(f , end=" ")


# fruits.sort()
# print(fruits)
# fruits.sort(reverse = True)
# print(fruits)

new_fruit =  [fruit for fruit in fruits if "an" in fruit]
print(new_fruit)