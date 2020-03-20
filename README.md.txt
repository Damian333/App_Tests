Tests were divided into two parts. The first part of the registration test was contained in the "Test_Regestration" folder, the second in the "Test_Login" folder. These parts work independently of each other.
The "Test Regestration" folder consists of the following files:
- "input_test_data_reg.xlsx" with input data (email address, password, name, surname, date of birth, etc.),
- the file launching "INITReg.py",
- the base class for the test "test_case_reg.py",
- Class containing the test of the new user registration procedure "regestration.py",
- The text file "test_results.txt" in which the test results are saved.

The "Test Login" folder consists of the following files:

- "input_test_data_log.xlsx" with input data (user email address and password),
- the file launching "INITLog.py",
- the base class for the test "test_case_reg.py",
- Class containing the test of the registration procedure of the new user "login.py",
- The text file "test_results.txt" in which the test results are saved.
Implementation of test cases using the above scripts can be done by changing the input data, entering correct or incorrect passwords, registering an existing or non-existent account, etc.
The following tools were used to write tests outside the Selenium framework and Python (version 2.7):
- the "pandas" module for handling input data downloaded from an xlsx file,
- MSExcel program for entering input data.
Test launch procedure:
- entering the desired input data to the xlsx file,
- entering "python INITReg.py" for registration tests and "python INITLog.py" for login tests on the command / terminal line.
The test scripts deliberately introduce delays after each step taken to visualize how the test works. The built-in "time" module was used for this.