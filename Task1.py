def main(): 
    UI = input("Would you like to use Pythagoras, Trigonometry, Sine Rule or Cosine Rule: ")
    if UI.casefold() == 'pythagoras':
        from Func import weird_calculation, weird_calculation2
        weird_answer = weird_calculation2()
        print(weird_answer)
    elif UI.casefold() == 'trigonometry':
        from Func import weird_calculation3, SOH, CAH, TOA
        UI2 = input("Would you like to use Sin, Cos or Tan: ")
        if UI2.casefold() == 'sin':
            weird_answer2 = SOH()
            print(weird_answer2) 
        elif UI2.casefold() == 'cos':
            weird_answer2 = CAH()
            print(weird_answer2)
        elif UI2.casefold() == 'tan':
            weird_answer2 = TOA()
        else: 
            main()
    elif UI.casefold() == 'sine rule': 
        from Func import SinRule
        weird_answer3 = SinRule() 
        print('The size of the other angle is', weird_answer3)
    elif UI.casefold() == 'cosine rule':
        from Func import CosineRule
        weird_answer4 = CosineRule()
        print('The size of the missing lenght is', weird_answer4) 
    else: 
        main() 
main() 



# After you have written the reusable functions, answer the following:
# Questions:
# 1. What are the preconditions for your code not to break?
# The input needs to be an integer or float, there needs to be a check if they dont input anything the code would need to loop back to the question.
# 2. Validate the user's input based on your preconditions.
# COMPLETED
# 3. Why was it useful to use reusable components in this case? Please mention at least 2 reasons and don't forget to contextualise.
# It is useful as you can copy parts of your code like the input validation. 
# Futhermore the copied code will be more reliable as it is tested and not new so there will be less errors 

# Further Tasks:
# 1. Put your functions in seperate appropriate files and import them in.
# COMPLETED (Func.py)
# 2. In your new file add functions for SOH CAH TOA. Also for the sine and cosine rule.
# COMPLETED (Func.py) 
# 3. Let the user choose whether they would like to use Pythogras, SOH, CAH, TOA, sine or cosine rule. Then ask for the relavent information and return the result to them.
# COMPLETED (Task1.py) - cosine rule doesn't output the exact answer 
# 4. Make sure all of your functions (except the main one) only do ONE thing or process.

# Extension:
# After you calculate the the result for the user. Use a library like Turtle to draw an approximation of their triangle for them.
# Hint: import the functions in drawing_functions.py and call them. See what happens. BTW check out the turtle docs for further info on how to use Turtle. 
