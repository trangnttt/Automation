*** Settings ***
Documentation    Move User Defined Keywords to Resource File
Resource    ./Resource/CommonFunctionality.robot
Resource    ./Resource/eBay_UserDefinedKeyWord.robot

Test Setup    CommonFunctionality.Start TestCase
Test Teardown    CommonFunctionality.Finish TestCase

*** Test Cases ***
Verify basic search functionality for eBay
    [Documentation]    This test case verifies the basic search
    [Tags]   Functional
    
    
    eBay_UserDefinedKeyWord.Verify Search Results
    eBay_UserDefinedKeyWord.Filter results by condition
    eBay_UserDefinedKeyWord.Verify Filter results

    
