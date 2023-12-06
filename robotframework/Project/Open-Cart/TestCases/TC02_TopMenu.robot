*** Settings ***
Library    SeleniumLibrary
Resource    ../Resource/CommonFunctionality.robot
Resource    ../Resource/validation_TopMenu.robot
Library    Collections
Variables    ../Variables/Variables_WebElemt.py

# Test Setup    CommonFunctionality.Start TestCase
# Test Teardown    CommonFunctionality.Finish TestCase

# *** Test Cases ***
# Test Case Top Menu
#     Test Case left of Top Menu
#     Test Case right of Top Menu  
*** Keywords ***

Test Case Top Menu
    Test Case left of Top Menu
    Test Case right of Top Menu  

Test Case left of Top Menu
    Click Button    ${btn_Currency}
    Sleep    2
    validation_TopMenu.Check display data Currency
    validation_TopMenu.Click item Currency
Test Case right of Top Menu
    validation_TopMenu.Check Icon Text and Link Menu of Top Menu
    validation_TopMenu.Check sub menu of Top Menu 