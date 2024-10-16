#Program 3 – Auto Insurance
#Write a program that computes monthly insurance according to the provided schedule. 

#Student #:     Alex Barr
#Student Name:  W0487099

#Initialize Variables

ageTier1 = [15,25] #Age tiers put here so they are editable if need be in the future
ageTier2 = [25,40] #ageTierX[0] = the first age in the range
ageTier3 = [40,70] #ageTierX[1] = the last age in the range

insuranceRateList = [[0.2,0.15,0.1],[0.25,0.17,0.1]] #first list values are for female tiers, second is for male

userSex = 0
userAge = 0
vehiclePrice = 0.0
insuranceRate = 0.0
finalInsurance = 0.0

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)

    #Ask the user whether they are male or female
 
    userSex = input("Are you 'Male' or 'Female'?: ").lower()
    print("")

    #Convert userSex to int for later calculations
    
    if userSex == "male":
            userSex = 1
    elif userSex == "female":
            userSex = 0
    else:
         print("Incorrect Value; Program Ending")
         return

    #Ask the user what their age is
 
    userAge = int(input("Enter your age: "))
    print("")

    #Ask the user what purchase price of the vehicle

    vehiclePrice = float(input("Enter the purchase price of the vehicle: "))
    print("")

    #Calculate the monthly insurance based on age and sex

    match userSex:
        
        case 1:

            if userAge >= ageTier1[0] and userAge < ageTier1[1]:
                insuranceRate = insuranceRateList[1][0]
            elif userAge >= ageTier2[0] and userAge < ageTier2[1]:
                insuranceRate = insuranceRateList[1][1]
            else:
                insuranceRate = insuranceRateList[1][2]
        
        case 0:

            if userAge >= ageTier1[0] and userAge < ageTier1[1]:
                insuranceRate = insuranceRateList[0][0]
            elif userAge >= ageTier2[0] and userAge < ageTier2[1]:
                insuranceRate = insuranceRateList[0][1]
            else:
                insuranceRate = insuranceRateList[0][2]

    #Calculate the monthly insurance rate by multiplying the insuranceRate and the Vehicle Price

    finalInsurance = (insuranceRate * vehiclePrice) / 12

    #Tell the user what the monthly insurance rate is

    print(f"Your monthly insurance will be ${finalInsurance:.2f}")
    print("")

    # YOUR CODE ENDS HERE

main()