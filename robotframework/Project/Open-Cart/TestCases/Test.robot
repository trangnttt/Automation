*** Settings ***
Library    SeleniumLibrary
Variables    ../Variables/Variables_WebElemt.py
Resource    ../Resource/CommonFunctionality.robot
Resource    ../TestCases/TC02_TopMenu.robot
Resource    ../TestCases/TC03_Header.robot

Test Setup    CommonFunctionality.Start TestCase
Test Teardown    CommonFunctionality.Finish TestCase

*** Test Cases ***
Test Suite Login
    TC02_TopMenu.Test Case Top Menu
    TC03_Header.Test Case Header
    
