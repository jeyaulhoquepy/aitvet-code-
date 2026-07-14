# This fuction adds two number 
def add (a,b):
    return a+b

#This function subtracts two number

def subtract (a,b):
    return a-b

#This function multiplies two number 
def multiply(a,b):
    return a*b

#This function divides two number
def divide(a,b):
    return a/b

print("Select Operation")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")


while True:
    choice = input("Enter chioce(1/2/3/4)=")


    if choice in ('1','2','3','4'):
        try:
            num1 = float(input("Enter 1st Number ="))
            num2 = float(input("Enter 2nd Number ="))

        except ValueError:  # eitata provlame asea but akhon thik hoya ga sa 


            
            print("Invalid Input mama 😁. Please enter a number.")
            continue
            if choice == '1':
                print(num1, "+", num2, "=", add(num1,num2))

            elif  choice == '2':
                print(num1, "-", num2, "=", subtract(num1,num2))

            elif  choice == '3':
                print(num1, "*", num2, "=", multiply(num1,num2))

            elif  choice == '4':
                print(num1, "/", num2, "=", divide(num1,num2))

# akhon break sitam add kora divo
                next_calculation = input("Let's do next calculation? (Yes / No)=")

                if next_calculation == 'no':
                    break

                else:
                    print("Invalid Input mama 😂")
                    


 
            
