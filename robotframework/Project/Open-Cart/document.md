https://opencart.abstracta.us/

Account: qua31601@nezid.com - 123123

*** Login ***
Test Case Login gồm các case basic như:
1. Login email and password null
2. Login email null
3. Login password null
4. Login email invalid
5. Login password invalid
6. Login email and password invalid
7. Login pass 

*** Top Menu ***
Test case Top Menu
    Left:   Currency    - Check display data Currency
                        - Click item Currency
    Right:  Menu    - Check icon, text, link
            SubMenu - Check text, link

Test case Header
    Logo    - Check text
            - Check Link
    Search  - No value => check class của product không có, count = 0
            - Value valid => check class của product có, count > 0
            - Value invalid => check class của product không có, count = 0
            - Value emoji => check class của product không có, count = 0
    Cart    - Check text
            - Check click button             


Test Suite
    TS_Login    - TC Login
    TS_Header   - TC Top Menu
                - TC Header     