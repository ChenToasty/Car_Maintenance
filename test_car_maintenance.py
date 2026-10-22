import unittest
from contextlib import redirect_stdout
from io import StringIO
from unittest.mock import mock_open, patch

import car_maintenance as car


class TestCarMaintenance(unittest.TestCase):
    # Subsystem 1: Read both maintenance mileages from the file.
    def test_getMaintenance(self):
        with patch("builtins.open", mock_open(read_data="56000\n53000")):
            oil_mileage, tire_mileage = car.getMaintenance()

        self.assertEqual(oil_mileage, 56000)
        self.assertEqual(tire_mileage, 53000)

    # Subsystem 2: Check the miles driven and the oil-change message.
    def test_checkOil_due(self):
        output = StringIO()
        with redirect_stdout(output):
            miles_driven = car.checkOil(59000, 56000)

        self.assertEqual(miles_driven, 3000)
        self.assertEqual(output.getvalue(), "\nYour oil change is due.\n")

    def test_checkOil_not_due(self):
        output = StringIO()
        with redirect_stdout(output):
            miles_driven = car.checkOil(58000, 56000)

        self.assertEqual(miles_driven, 2000)
        self.assertEqual(output.getvalue(), "\nOil change is due in 1000 miles.\n")

    # Subsystem 3: Check the miles driven and the tire-rotation message.
    def test_checkTires_due(self):
        output = StringIO()
        with redirect_stdout(output):
            miles_driven = car.checkTires(59000, 53000)

        self.assertEqual(miles_driven, 6000)
        self.assertEqual(output.getvalue(), "\nYour tire rotation is due.\n")

    def test_checkTires_not_due(self):
        output = StringIO()
        with redirect_stdout(output):
            miles_driven = car.checkTires(56000, 53000)

        self.assertEqual(miles_driven, 3000)
        self.assertEqual(output.getvalue(), "\nTire rotation is due in 2000 miles.\n")

    # Updating one service should leave the other service alone.
    def test_updateMaintenance_oil(self):
        oil_mileage, tire_mileage = car.updateMaintenance(60000, "O", 55000, 53000)
        self.assertEqual((oil_mileage, tire_mileage), (60000, 53000))

    def test_updateMaintenance_tires(self):
        oil_mileage, tire_mileage = car.updateMaintenance(60000, "t", 55000, 53000)
        self.assertEqual((oil_mileage, tire_mileage), (55000, 60000))

    # Run the menu with simulated answers and check what it saves.
    @patch("builtins.input", side_effect=["Chris", "WRX", "59000", "O", "Y", "Q"])
    def test_system_saves_completed_oil_change(self, mock_input):
        fake_file = mock_open(read_data="56000\n53000")
        with patch("builtins.open", fake_file), redirect_stdout(StringIO()):
            car.system()

        fake_file.assert_any_call("maintenance.txt", "w")
        handle = fake_file()
        handle.write.assert_any_call("59000\n")
        handle.write.assert_any_call("53000")


if __name__ == "__main__":
    unittest.main()
