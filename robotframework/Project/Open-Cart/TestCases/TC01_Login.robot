*** Settings ***
Library    SeleniumLibrary
Variables    .././Variables/Variables_WebElemt.py
Resource    ../Resource/validation_Login.robot
# Resource    ../Resource/CommonFunctionality.robot

# Test Setup    CommonFunctionality.Start TestCase
# Test Teardown    CommonFunctionality.Finish TestCase

*** Keywords ***
Test Case Login
    Click Element    ${dropdown_Login}
    Mouse Down    ${elm_link_Login}
    Click Element    ${elm_link_Login}
    Sleep    3
    validation_Login.Verify email and password null
    validation_Login.Verify email null
    validation_Login.Verify password null
    validation_Login.Verify email invalid
    validation_Login.Verify password invalid
    validation_Login.Verify email and password invalid
    validation_Login.Verify email and password valid
