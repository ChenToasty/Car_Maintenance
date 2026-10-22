# Car Maintenance Tracker

This Python program helps a user check when an oil change or tire rotation is due. It reads saved service mileages, compares them with the current mileage, and saves updated records when the user quits.

## System and subsystems

- **Subsystem 1 — getMaintenance:** Reads the two saved service mileages.
- **Subsystem 2 — checkOil:** Checks the 3,000-mile oil-change interval.
- **Subsystem 3 — checkTires:** Checks the 5,000-mile tire-rotation interval.
- **updateMaintenance:** Updates the selected service mileage in memory.
- **system:** Runs the menu, calls the subsystems, and saves records on exit.

## Maintenance file

`maintenance.txt` contains two integers: the oil-change mileage on the first line and tire-rotation mileage on the second. Run the program from the project folder so it can find this file.

## Function reference

The sections below are generated directly from the docstrings in the Python file.

::: car_maintenance
