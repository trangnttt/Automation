*** Settings ***
Library    SeleniumLibrary
Resource    ../TestCases/TC01_Login.robot
Resource    ../TestCases/TC02_Header.robot

Test Setup    Open Browser    https://www.saucedemo.com/    chrome
Test Teardown    Close Browser

*** Test Cases ***
Chay Test Case 
    TC01_Login.Test Case Login
    TC02_Header.Test Case Header
