*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}    https://www.ebay.com/
${browser}    chrome

*** Keywords ***
Start TestCase
    Open Browser    ${url}     ${browser}
    Maximize Browser Window
    Sleep    4

Finish TestCase
    Close Browser