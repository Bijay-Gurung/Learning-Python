#Adding Vector in graphically

#importing matplot module
import matplotlib.pyplot as plt

#title function for Displaying title
def title():
    title = "Displaying the n dimensional real co-ordinate spaces in graphically"
    display = title.center(90)
    print(display + "\n")

#two_dimensional function for 2-dimensional real co-ordinate spaces
def two_dimensional():
    # prompt the value from the user for 2 dimensional real Co-ordinate spaces
    print("Enter the number for A vector")
    a = [int(input("X-Component: ")),int(input("Y-Component: "))]

    print("Enter the number for B vector")
    b = [int(input("X-Component: ")), int(input("Y-Component: "))]
    #c is the result of adding a and b vector
    c = [a[0]+b[0], a[1]+b[1]]

    #using matplot to display the result in graph
    #creating new figure
    plt.figure()

    #plot vector
    plt.quiver(0, 0, a[0], a[1], angles='xy', scale_units='xy', scale=1, color='red', label='a vector')
    plt.quiver(0, 0, b[0], b[1], angles='xy', scale_units='xy', scale=1, color='green', label='b vector')
    plt.quiver(0, 0, c[0], c[1], angles='xy', scale_units='xy', scale=1, color='blue', label='c vector')


    #set labels and legends
    plt.title('2d real co-ordinate spaces')
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')
    plt.legend()

    #show the plot
    plt.xlim(0, 20) #adjusting the limits to 20
    plt.ylim(0, 20)
    plt.grid(True)
    plt.show()

#main function is brain of this code. :D It contorls all the parts.
def main():
    title()
    while True: #using while loop
        print("1. 2-Dimensional Real Co-ordinate Spaces")
        print("2. 3-Dimensional Real Co-ordintae Spaces")
        print("3. 4-Dimensional Real Co-ordinate Spaces")
        print("4. Quit")

        choice = int(input(">"))

        if choice == 1:
            two_dimensional()
        elif choice == 2:
            pass
        elif choice == 3:
            pass
        elif choice == 4:
            break
        else:
            print("Invalid Choice, try again!")

main()