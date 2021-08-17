import csv
from os import access


access_fee=1000

print(f"Please Pay Amount {access_fee}\n")
data=[]
number_plate=input("Enter Vehicle Reg: ")
payment=int(input(f"({access_fee}) Enter Amount Given By Driver: "))

if(payment<1000):
    bal=access_fee-payment
    print(f"The Drive Has a deficite Amount of: ksh {bal}\nPlease Pay Right Amount To Proceed!!")
    
else:    
    header=["Vehicle Reg","Amount"]
    data.append(number_plate)
    data.append(payment)

    print(f"Please Confirm Paying {access_fee} KSHS For Vehicle {number_plate}")

    ans=input("Input Y: Yes\nInput N : No\n_")

    if(ans=="Y" or ans=="y"):
        print("Vehicle Has Been Cleared")
        with open('records.csv','w') as f:
            writer=csv.writer(f)
            writer.writerow(header)
            writer.writerow(data)
        data=[]
    elif(ans=='N' or 'n'):
        print("Vehicle has not been cleared Please Try Again")

    else:
        print("An Error Occured")








