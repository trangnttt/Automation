*** Settings ***
Library    SeleniumLibrary
Variables    ../Variables/Variables_WebElemt.py

*** Variables ***
${VALID USER}     admin@example.com
${VALID PASSWORD}    123456


*** Keywords ***
Verify Test Case Login Pass
    Input Text    ${LoginUserName}    ${VALID USER}
    Input Text  ${LoginPassword}    ${VALID PASSWORD}
    Click Button    ${LoginBtnLogin}
    Sleep    3
    Element Should Contain    ${CheckPassLogin}    admin

