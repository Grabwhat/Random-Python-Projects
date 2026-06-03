import math
def nature_roots():
    
    while True:
        
        coefficients = input("\nEnter 3 integers (a, b, c) ")
        
        if coefficients.count(",") == 2:
            coefficients = coefficients.split(",")
        else:
            print("Please enter in format (a, b, c) ")
            continue

        a, b, c = map(int, coefficients)

        discrim = (b**2) - (4*a*c)
        if discrim > 0:

            root1 = (-b + math.sqrt(discrim))/(2*a)
            root2 = (-b - math.sqrt(discrim))/(2*a)

            if math.sqrt(discrim).is_integer():
                print("\nReal Rational Roots")
            else:
                print("\nIrrational Real Roots")
            
            print(f"Roots: {round(root1, 8)}, {round(root2, 8)}")
            print("___________________________")

        elif discrim == 0:
            print("\nA Real Double Root")
            print(f"Root: {-b/(2*a)}")

            print("___________________________")
        else:
            print("\nImaginary Roots")

            discrim = abs(discrim)
            root1 = (math.sqrt(discrim))/(2*a)
        
            print(f"Roots: {-b/(2*a)} + {round(root1, 8)}i, {-b/(2*a)} - {round(root1, 8)}i")
            
            print("___________________________")

nature_roots()