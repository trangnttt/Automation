*** Settings ***
Library    SeleniumLibrary
*** Test Cases ***

This is a sample test Case
    [Documentation]    Google test 
    [Tags]    regression

    Open Browser    https://www.google.com    chrome
    Close Browser
 