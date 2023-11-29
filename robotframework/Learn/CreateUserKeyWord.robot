*** Settings ***
Documentation    Create User Defined Keywords
Library    SeleniumLibrary

*** Test Cases ***
Verify basic search functionality for eBay
    [Documentation]    This test case verifies the basic search
    [Tags]   Functional
    
    Start TestCase
    Verify Search Results
    Finish TestCase
    
# How to Create User Defined Keywords?
*** Keywords ***

Start TestCase
    Open Browser    https://www.ebay.com/    chrome
    Maximize Browser Window
Verify Search Results
    Input Text    xpath://input[@id="gh-ac"]   mobile
    Press Keys    xpath://input[@id="gh-btn"]    RETURN

Finish TestCase
    Close Browser