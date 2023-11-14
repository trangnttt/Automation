*** Settings ***

*** Variables ***
${VARIABLE_DEMO} =  This is GLOBAL Variable

*** Test Cases ***
This is demo test 1
    ${variable_demo} =    Set Variable    This is TESTCASE variable
    Log    ${VARIABLE_DEMO}

This is demo test 2
    Log    ${VARIABLE_DEMO}

This is demo test 3
    Log    This is demo Keyword


*** Keywords ***
This is demo Keyword
    [Arguments]    ${variable_demo}=This is Keyword variable
    Log    ${VARIABLE_DEMO}