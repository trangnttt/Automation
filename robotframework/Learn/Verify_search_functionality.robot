*** Settings ***
Documentation    Move User Defined Keywords to Resource File
Resource    ./Resource/CommonFunctionality.robot
Resource    ./Resource/eBay_UserDefinedKeyWord.robot
Resource    ./Resource/HeaderPage.robot
Resource    ./Resource/SearchResultPage.robot

Test Setup    CommonFunctionality.Start TestCase
Test Teardown    CommonFunctionality.Finish TestCase

*** Test Cases ***
Verify basic search functionality for eBay
    [Documentation]    This test case verifies the basic search
    [Tags]   Functional
    
    HeaderPage.Input Search Text and Click Search
    SearchResultPage.Verify Search Results

Verify advanced search functionality
    [Documentation]    This test case verifies the advanced search
    [Tags]   Functional
    
    HeaderPage.Click on Advanced Search Link
    

    
