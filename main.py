



def addition(left, right):
    sum = left + right
    return sum

def subtraction(left, right):
    difference = left - right
    return difference

sum = addition(2,3)
difference = subtraction(4,5)

print(sum, difference)

print("sum: " + str(sum) + " difference: " + str(difference))

print(f"sum: {sum} difference: {difference}")