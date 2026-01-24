# Q1. 
def get_ten_points():
    global points
    points = points + 10

points = 0
get_ten_points()
print(points) # 10

# Q2. 
# The code first outputs the value of "a", which is "5", then, after calling the function "foo()", it still outputs "5".
  # This is because the "a" inside the function "foo()" is created as a local variable instead of attempting to change the global variable "a".
  # Thus, the local variable is hidden from the global code.

# Q3.
# If "global a" was added, the "foo()" function would access the global variable "a" instead of creating a brand new local variable. 
  # Therefore, "10" would be printed following the "5".

# Q4. 
# The following code causes a "NameError" because the variable "a" in the last line is undefined.
  # This is because although it seems to have been already defined in the "create_variable()" function, it is only created as a lcoal variable and is actually inaccessible/hidden outside of it.

# Q5. 
# I would modify the code to work by including a "global a" at the beginning of the "create_variable()" function.
# Ex:

def create_variable():
    global a
    a = 5

create_variable()
print(a) # 5
