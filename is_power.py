def is_divisible(a, b):
    if a % b == 0:
        return True
    else:
        return False

def is_power(a, b):
     if not is_divisible(a, b): # check if the first_argument divided by the second_argument
         return False
     if a == b: # cheking for equality; conditions of exiting from the recursion
         return True
     if b == 1 and a != 1:
         return False # checking for power of 1
     else:
         return is_power(a / b, b) # recursion

#tests
print("is_power(10, 2) returns: ", is_power(10, 2))
print("is_power(27, 3) returns: ", is_power(27, 3))
print("is_power(1, 1) returns: ", is_power(1, 1))
print("is_power(10, 1) returns: ", is_power(10, 1))
print("is_power(3, 3) returns: ", is_power(3, 3))
