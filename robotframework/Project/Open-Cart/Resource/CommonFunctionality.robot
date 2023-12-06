*** Settings ***
Library    SeleniumLibrary
Variables    ../Variables/Variables_WebElemt.py

*** Variables ***
${url}    https://opencart.abstracta.us/
${browser}    chrome

*** Keywords ***
Start TestCase
    Open Browser    ${url}    ${browser}

Finish TestCase
    Close Browser