import car_maintenance as car


# Test Subsystem 1
oil_mileage, tire_mileage = car.getMaintenance()

if type(oil_mileage) == int and type(tire_mileage) == int:
    print("maintenance read test passed!")
else:
    print("maintenance read test failed :(")


# Test Subsystem 2
miles_driven = car.checkOil(59000, 56000)

if miles_driven == 3000:
    print("oil change test passed!")
else:
    print("oil change test failed :(")


# Test Subsystem 3
miles_driven = car.checkTires(59000, 53000)

if miles_driven == 6000:
    print("tire rotation test passed!")
else:
    print("tire rotation test failed :(")


# Test updating the oil-change mileage
oil_mileage, tire_mileage = car.updateMaintenance(60000, "O", 55000, 53000)

if oil_mileage == 60000 and tire_mileage == 53000:
    print("maintenance update test passed!")
else:
    print("maintenance update test failed :(")
