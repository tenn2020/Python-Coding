# PI = 3.142
# area = PI * (r**2)


def compute_area_circle():
    # Ten Norsang

    # make definitions here
    PI: float = 3.14
    radius: int = 0

    # get the radius using a function
    def get_radius():
        nonlocal radius
        radius = float(input("Enter the radius: "))
        return radius

    # processing using a function
    def get_area():
        nonlocal PI
        area = PI * (get_radius()**2)
        return area

    # output the area here by calling a function
    print("The area of circle is: ", get_area())

    pass

compute_area_circle()