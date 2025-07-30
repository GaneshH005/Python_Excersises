# start_odo = 143002
start_odo = int(input("enter the start odometer reading: "))
# end_odo = 143681
end_odo = int(input("enter the end odometer reading: "))
dist_travel = (end_odo - start_odo)
# fuel_consum = 68
fuel_consum = int(input("enter the fuel consumed in ltr: "))
milage = dist_travel // fuel_consum

print("milage of the vehicle", milage, 
        ", for the distance travelled", dist_travel, "kms")
