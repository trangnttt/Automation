check https://www.saucedemo.com/

- Resource
- Variable
- TestCases
    - TCLogin.robot
- TestSuites

*** Login ***
Test Case Login gồm các case basic như:
1. Usename, Password valid
2. Usename null, Password valid
3. Usename valid, Password is null
4. Usename, Password null
5. Usename invalid, Password valid
6. Usename valid, Password invalid
7. Usename invalid, Password invalid
8. Usename has been locked out

* Các trường hợp test (Resource/validation_Login.robot) => Find Element (Variables/Variables_WebElemt.py) => run Test Case(TestCases/TC01_Login.robot)


*** Header ***
- Menu: check display menu
- Logo: check text logo
* Các trường hợp test (Resource/valid_Header.robot) => run Test Case(TestCases/TC02_Heard.robot)

*** TestSuites ***
https://docs.robotframework.org/docs/parallel

 pip install -U robotframework-pabot