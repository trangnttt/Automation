*** Settings ***
Library    SeleniumLibrary
Variables    ../Variables/Variables_WebElemt.py

*** Variables ***
${VALID USER}     admin@example.com
${VALID PASSWORD}    123456


*** Keywords ***
Verify Test Case Login with Invalid Username
    Input Text    ${LoginUserName}    phero@gmail.com
    Input Text  ${LoginPassword}    ${VALID PASSWORD}
    Click Button    ${LoginBtnLogin}
    Sleep    3
    # Alert Should Be Present    User does not exist.
    Element Text Should Be    xpath://span[@data-notify="message"]    Invalid login credentials

Verify Test Case Login with Invalid Password
    Input Text    ${LoginUserName}    ${VALID USER}
    Input Text  ${LoginPassword}    1234567
    Click Button    ${LoginBtnLogin}
    Sleep    3
    Element Text Should Be    xpath://span[@data-notify="message"]    Invalid login credentials


