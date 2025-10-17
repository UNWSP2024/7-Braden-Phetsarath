#Braden phetsarath
#10/16
# Program #4: Coordinates
# Write a distance function that will take two 3-dimensional coordinates (as input)
# and will return (as output) the distance between those points in space.
# The 3-dimensional coordinates must be stored as tuples.
from sys import excepthook


def points_of_interest ():
    data1 = input("Enter first point in space (x, y, z)(Separated by spaces): ").split()
    user_tuple1 = tuple(map(float,data1))


    data2 = input("Enter second point in space (x, y, z)(Separated by spaces): ").split()
    user_tuple2 = tuple(map(float,data2))

    return user_tuple1, user_tuple2

import math
def distance( p1, p2):
    x1 , y1, z1 = p1
    x2, y2, z2 = p2

    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)
# Now write a mainline that has the user enter the two tuples.
# The mainline calls the distance function and stores the distance in a variable.  The mainline then displays the distance.
# Also include exception handling to deal with faulty input.
# The distance between two points (x1,y1,z1) and (x2, y2, z2) is
#    given by:   sqrt ((x2-x1)^2 + (y2 - y1)^2 + (z1 - z2)^2)
def main():
   try:
    t1, t2 = points_of_interest()

    d = distance(t1, t2)
    print("The distance of the two points is", d)

   except ValueError:
    print("Error: Please enter numeric coordinates separated by spaces.")

if __name__ == "__main__":
    main()





