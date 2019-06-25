import numpy as np

pol_degree = int(input("What is the highest degree of your polynomial:"))
if pol_degree == 0:
    print("Nice try! The derivative of a constant(s) is zero!")

elif pol_degree < 0:
    print("Polynomial degree cannot be negative!")

else:
    list_of_coeff = []

    for i in range(pol_degree + 1):
        h = int(input("Enter coeff {}:".format(i)))
        list_of_coeff.insert(i, h)

    list_of_power = []
    for i in range(pol_degree + 1):
        list_of_power.append(i)

    list_of_power.remove(0)  # derivative of constant = 0
    list_of_coeff.pop(0)
    result = np.multiply(list_of_power, list_of_coeff)

# The code below helps display the result in the form ax^0 + bx^1 +...

print("The derivative is:")
temp_list = [] # to store ax^0, bx^1 separately
for i in range(pol_degree):
    temp_list.append(str("{}x^{}".format(result[i], i)))

k = len(temp_list)
count = 1
for j in temp_list:
    count+=1
    print(j,end=" ")
    if count <= k:
        print("+", end=" ")

    else:
        break
