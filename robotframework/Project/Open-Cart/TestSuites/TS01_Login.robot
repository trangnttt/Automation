*** Settings ***
Library    SeleniumLibrary
Variables    ../Variables/Variables_WebElemt.py
Resource    ../Resource/CommonFunctionality.robot
Resource    ../TestCases/TC01_Login.robot

Test Setup    CommonFunctionality.Start TestCase
Test Teardown    CommonFunctionality.Finish TestCase

*** Test Cases ***
Test Suite Login
    TC01_Login.Test Case Login
    
