import math  
def weird_calculation():
    opp1 = input("Enter your first triangle's opposite side length: ")
    adj1 = input("Enter your first triangle's adjacent side length: ")
    opp2 = input("Enter your second triangle's opposite side length: ")
    adj2 = input("Enter your second triangle's adjacent side length: ")
    try: 
        hyp1 = math.sqrt(float(opp1)**2 + float(adj1)**2)
        hyp2 = math.sqrt(float(opp2)**2 + float(adj2)**2)
    except ValueError:  
        print("Please enter a number")
        weird_calculation() 
    else: 
        return hyp1, hyp2
def weird_calculation2(): 
    x = weird_calculation()
    opp1 = x[0]
    adj1 = x[1]  
    hyp3 = math.sqrt(opp1**2 + adj1**2)
    return hyp3
def weird_calculation3():    
    opp1 = input("Enter the opposite side of your triangle: ")
    adj1 = input("Enter the adjacent side of your triangle: ")
    hyp1 = input("Enter the hypotenuse side of your triangle: ")
    return opp1, hyp1, adj1
def SOH(): 
    x = weird_calculation3()
    opp1 = x[0]
    hyp1 = x[1]
    try: 
        ang1 = math.degrees(math.asin(int(opp1) / int(hyp1)))
    finally: 
        return ang1 
def CAH(): 
    x = weird_calculation3() 
    adj1 = x[2]
    hyp1 = x[1]
    try:
        ang1 = math.degrees(math.acos(int(adj1) / int(hyp1)))
    finally: 
        return ang1 
def TOA(): 
    x = weird_calculation3() 
    opp1 = x[0]
    adj1 = x[2]
    try:
        ang1 = math.degrees(math.atan(int(opp1) / int(adj1)))
    finally:
        return ang1
def SinRule(): 
    opp1 = input("Enter your triangle's side lenght: ")
    ang1 = input("Enter your triangle's opposite angle size: ")
    opp2 = input("Enter the lenght of a different side: ")
    try:    
        ang = (math.sin(math.radians(int(ang1)))/int(opp1))*int(opp2)
        ang2 = math.degrees(math.asin(ang))
    except ValueError: 
        print("Please enter a number")
        SinRule() 
    else: 
        return ang2 
def CosineRule(): 
    s1 = input("Enter your triangle's side lenght: ")
    s2 = input("Enter another of your triangle's side: ")
    opp1 = input("Enter the opposite angle of your unknown side: ")
    try: 
        ang = float(s1)** + float(s2)** - 2 * float(s1) * float(s2) * math.cos(math.radians(float(opp1)))
        ang2 = math.sqrt(float(ang))
    except ValueError:
        print("Please enter a number")
        CosineRule() 
    else: 
        return ang2
    #THE ASNWER IS CLOSE TO THE ACTUAL ANSWER FOR COSINE RULE BUT NOT EXACT (I TIRED) :(
        
