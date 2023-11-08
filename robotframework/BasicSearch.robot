*** Settings ***
Documentation    Move User Defined Keywords to Resource File
Library    SeleniumLibrary

*** Test Cases ***
Verify basic search functionality for eBay
    [Documentation]    This test case verifies the basic search
    [Tags]   Functional
    
    Start TestCase
    Verify Search Results
    Filter results by condition
    # Verify Filter results
    Finish TestCase
    
# How to Create User Defined Keywords?
*** Keywords ***

Start TestCase
    Open Browser    https://www.ebay.com/    chrome
    Maximize Browser Window
Verify Search Results
    Input Text    xpath://input[@id="gh-ac"]   mobile
    Press Keys    xpath://input[@id="gh-btn"]    RETURN

Filter results by condition
    Mouse Over    xpath://div[@class="srp-controls__resize-display"]/span[1]
    Sleep    3s
    Mouse Down    class:faux-link follow-ebay__trigger
    Click Element    class:faux-link follow-ebay__trigger

# Verify Filter results
#     Element Should Contain    xpath://div[@id="srp-river-results"]//ul[@class="srp-results srp-list clearfix"]/li[2]    expected

Finish TestCase
    Close Browser