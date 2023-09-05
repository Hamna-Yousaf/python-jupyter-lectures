def condition(meter_type):
    if(meter_type == "h"):
        unit=int(input("plz enter your units"))
        if(unit <= 200):
          total_bill=unit*23
        else:
            total_bill=unit*35
    elif(meter_type == "c"):
        unit=int(input("plz enter your units"))
        if(unit <= 200):
            total_bill=unit*43
        else:
            total_bill=unit*57
    else:
        print("plz enter right type of meter")
    print("your total total bill is:",total_bill)


    