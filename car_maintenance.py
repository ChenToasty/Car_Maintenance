# Sub System 1
# Reads the maintenance records and returns both values.
def getMaintenance():
    """Read the last oil-change and tire-rotation mileages.

    Returns:
        mileages (tuple[int, int]): Last oil-change mileage and last tire-rotation mileage.

    Raises:
        FileNotFoundError: If maintenance.txt is missing from the working folder.
        ValueError: If either of the first two lines is not an integer.
    """
    with open("maintenance.txt", "r") as file:
        last_oil_change = int(file.readline().strip())
        last_tire_rotation = int(file.readline().strip())

    return last_oil_change, last_tire_rotation


# Sub System 2
# Calculates how many miles have been driven since the last oil change.
def checkOil(current_mileage, last_oil_change):
    """Check whether an oil change is due after 3,000 miles.

    Prints whether service is due or how many miles remain.

    Args:
        current_mileage (int): Current vehicle mileage.
        last_oil_change (int): Mileage at the last oil change.

    Returns:
        miles_driven (int): Miles driven since the last oil change.
    """
    miles_driven = current_mileage - last_oil_change

    if miles_driven >= 3000:
        print("\nYour oil change is due.")
    else:
        miles_left = 3000 - miles_driven
        print(f"\nOil change is due in {miles_left} miles.")

    return miles_driven


# Sub System 3
# Calculates how many miles have been driven since the last tire rotation.
def checkTires(current_mileage, last_tire_rotation):
    """Check whether a tire rotation is due after 5,000 miles.

    Prints whether service is due or how many miles remain.

    Args:
        current_mileage (int): Current vehicle mileage.
        last_tire_rotation (int): Mileage at the last tire rotation.

    Returns:
        miles_driven (int): Miles driven since the last tire rotation.
    """
    miles_driven = current_mileage - last_tire_rotation

    if miles_driven >= 5000:
        print("\nYour tire rotation is due.")
    else:
        miles_left = 5000 - miles_driven
        print(f"\nTire rotation is due in {miles_left} miles.")

    return miles_driven


# Updates the correct maintenance mileage when a service is completed.
def updateMaintenance(current_mileage, service, last_oil_change,
                      last_tire_rotation):
    """Update the mileage for a completed service.

    O or o updates oil; T or t updates tires. Other choices leave both values
    unchanged. This function returns values; system saves them to the file.

    Args:
        current_mileage (int): Mileage when the service was completed.
        service (str): O for oil or T for tire rotation.
        last_oil_change (int): Previously recorded oil-change mileage.
        last_tire_rotation (int): Previously recorded tire-rotation mileage.

    Returns:
        mileages (tuple[int, int]): Updated oil-change and tire-rotation mileages.
    """
    if service == "O" or service == "o":
        last_oil_change = current_mileage
    elif service == "T" or service == "t":
        last_tire_rotation = current_mileage

    return last_oil_change, last_tire_rotation


def system():
    """Run the Car Maintenance Tracker menu and save records when quitting.

    Asks for the user's name, car model, and current mileage. Reads the records,
    lets the user check or update a service, and writes both mileages to
    maintenance.txt after Q or q is selected.

    Returns:
        result (None): Information is printed and maintenance records are saved.

    Raises:
        ValueError: If the entered mileage or saved records are not integers.
        FileNotFoundError: If maintenance.txt cannot be found when reading.
        OSError: If the maintenance file cannot be read or written.
    """
    name = input("Enter your name: ")
    car_model = str(input("Enter your car model: "))
    current_mileage = int(input("Enter your current mileage: "))

    print(f"\nWelcome, {name}!")
    print(f"Car Model: {car_model}\n")
    print(f"Current Mileage: {current_mileage}\n")

    last_oil_change, last_tire_rotation = getMaintenance()

    # Lets the user choose which subsystem they want to use.
    # This is basically the menu.
    choice = ""

    while choice != "Q" and choice != "q":
        print("Type (O/o) to check oil change")
        print("Type (T/t) to check tire rotation")
        print("Type (Q/q) to quit")

        choice = input("Enter your choice: ")

        if choice == "O" or choice == "o":
            checkOil(current_mileage, last_oil_change)

            completed = input("Was the oil change completed? (Y/N): ")

            if completed == "Y" or completed == "y":
                last_oil_change, last_tire_rotation = updateMaintenance(
                    current_mileage, "O", last_oil_change,
                    last_tire_rotation)
                print("Oil change mileage updated.")

        elif choice == "T" or choice == "t":
            checkTires(current_mileage, last_tire_rotation)

            completed = input("Was the tire rotation completed? (Y/N): ")

            if completed == "Y" or completed == "y":
                last_oil_change, last_tire_rotation = updateMaintenance(
                    current_mileage, "T", last_oil_change,
                    last_tire_rotation)
                print("Tire rotation mileage updated.")

        elif choice == "Q" or choice == "q":
            print("\nMaintenance information saved.")

        else:
            print("\nInvalid choice.")

    # Writes the maintenance mileage back into the file.
    with open("maintenance.txt", "w") as file:
        file.write(f"{last_oil_change}\n")
        file.write(f"{last_tire_rotation}")


if __name__ == "__main__":
    system()
