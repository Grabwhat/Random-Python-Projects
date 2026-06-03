def geo_sum(term, upl, lowl):
    a1 = 1
    ratio = 0

    if lowl != 1:
        upl = upl - lowl + 1

    if "*" in term:
        term = term.split("*")

        for i in range(len(term)):
            if "^" in term[i]:
                exp_term = term[i].split("^")
                if exp_term[0][0] == "(" and exp_term[0][-1] == ")":
                    exp_term[0] = exp_term[1:-1]

                a1 *= int(exp_term[0]) ** lowl
                ratio = int(exp_term[0])
            
            else:
                a1 *= int(term[i])

    else:
        term = term.split("^")
        if term[0][0] == "(" and term[0][-1] == ")":
            term[0] = term[0][1:-1]

        if "/" in term[0]:
            term[0] = term[0].split("/")
            term[0] = int(term[0][0])/int(term[0][1])

        if "." not in str(term[0]):
            term[0] = int(term[0])
            
        a1 *= term[0] ** lowl
        ratio = term[0]
    
    ans = (a1 * (1 - ratio ** upl )) / (1 - ratio)

    return round(ans, 8)

def compute_term_arith(term, lowl, upl):
    a1 = an = 0

    for i in range(len(term)):
        if "n" in term[i]:

            if "/" in term[i]:
                break_down = term[i].split("/")
                first = eval(break_down[0])
                
                a1 = first * lowl
                an = first * upl
            
            elif "*" in term[i]:
                break_down = term[i].split("*")
                first = eval(break_down[0])
                
                a1 = first * lowl
                an = first * upl
            
            else:

                if len(term[i]) - 1 > 1:
                    a1 = float(term[i][:-1]) * lowl
                    an = float(term[i][:-1]) * upl
                
                else:
                    a1 = int(term[i][0]) * lowl
                    an = int(term[i][0]) * upl
    
    return [a1, an]

def arith_sum(term, upl, lowl):
    a1 = 0
    an = 0

    if "+" in term:
        term = term.split("+")
        a1, an = compute_term_arith(term, lowl, upl)
        
        if "n" in term[0]:
            a1 += float(term[1])
            an += float(term[1])
        
        else:
            a1 += float(term[0])
            an += float(term[0])

    else:
        term = term.split("-")
        a1, an = compute_term_arith(term, lowl, upl)
                    
        if "n" in term[0]:
            a1 -= float(term[1])
            an -= float(term[1])
        
        else:
            a1 -= float(term[0])
            an -= float(term[0])
    
    if lowl == upl: return a1

    return (upl * (a1 + an)) * 0.5

def is_geo(term):
    if "^" not in term: return False

    operation = ""
    if "+" in term:
        operation = "+"
    elif "-" in term and "-" != term[0]:
        operation = "-"
    elif "*" in term:
        operation = "*"
 
    term = [term] if operation == "" else term.split(operation) 

    for i in range(len(term)):            
        if "^" in term[i]:
            temp = term[i].split("^")

            if temp[0] == "n":
                return False

    return True

def is_arith(term):
    return "^" not in term

def main():
    print("\nWelcome to Sum & Type of Series.")
    print("You will enter the lower and upper limit of a series, then you will get the type of the series (arithmetic or geometric) and the sum.")

    low_lim = 0
    up_lim = 0

    while True:
        low = input("\nEnter the lower limit of the series: \n")

        if not low.isdigit():
            print("\nInvalid Input. Limits must be postive whole numbers.")
            continue
        
        low_lim =  int(low)
        break

    while True:
        up = input("\nEnter the upper limit of the series (no infinity): \n")

        if not up.isdigit():
            print("\nInvalid Input. Limits must be postive whole numbers.")
            continue
        
        up_lim = int(up)
        break
    
    print("\nFor a general term, use n to denote the position in the series. Use ^ to denote exponents.")

    print("\n****************************************************")
    print("\nFor an arithmetic series, only two terms will be accepted.")
    print("For a geometric series, only one term will be accepted.\n")
    print("****************************************************\n")
    term = input("Enter the general term in the series (ex: 2n + 1 or 3*2^n): \n")

    if low_lim > up_lim:
        print("\nInvalid limits; lower limit should be <= than upper limit.")
        

    elif "n" not in term:
        print("Not Geometric Nor Arithmetic")
        try:
            print(f"\nSum: {int(term) * ( up_lim - (low_lim - 1) )}")
        
        except:
            print("\nError Calculating. Check to make sure if general term is valid. (ex: 2n + 1 or 3*2^n)")
            print("\nNote: If you want one term for arithmetic series, you can add 0 (ex: 3x+0, x+0).")

    elif is_geo(term):
        print("\nGeometric Series")

        try:
            print(f"\nSum: {geo_sum(term, up_lim, low_lim)}")
        
        except:
            print("\nError Calculating. Check to make sure if general term is valid. (ex: 2n + 1 or 3*2^n)")
            print("\nNote: If you want one term for arithmetic series, you can add 0 (ex: 3x+0, x+0).")

    elif not is_geo(term) and is_arith(term):
        print("\nArithmetic Series")

        try:
            print(f"\nSum: {arith_sum(term, up_lim, low_lim)}")
        
        except:
            print("\nError Calculating. Check to make sure if general term is valid. (ex: 2n + 1 or 3*2^n)")
            print("\nNote: If you want one term for arithmetic series, you can add 0 (ex: 3x+0, x+0).")

    else:
        print("Not Geometric Nor Arithmetic")
        print("Cannot Calculate.")

if __name__ == "__main__":
    main_loop = True

    while main_loop:
        main()

        while True:
            again = input("\nDo you want to calculate again? (Y/N): ")
            if again in "yY":
                break
            
            elif again in "nN":
                print("\nGoodbye!\n")
                main_loop = False
                break

            else:
                print("\nInvalid Input.")
                continue
        
        continue