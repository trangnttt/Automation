*** Settings ***
Documentation    Basic Search Functionality
Library    SeleniumLibrary

*** Test Cases ***
Verify basic search functionality for eBay
    [Documentation]    This test case verifies the basic search
    [Tags]   Functional

    Open Browser    https://www.ebay.com/    chrome
    Maximize Browser Window
    Input Text    xpath://input[@id="gh-ac"]   mobile
    Press Keys    xpath://input[@id="gh-btn"]    RETURN
    Page Should Contain    Results
    Close Browser
