def is_triangle(x, y, z):
    if(x + y  < z or x + z < y or z + y < x):
        print "No"
    else:
        print "Yes"

x = int(raw_input("Side 1 length: "))
y = int(raw_input("Side 2 length: "))
z = int(raw_input("Side 3 length: "))

is_triangle(x, y, z)