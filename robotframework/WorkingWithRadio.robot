# Step1: Go to https://demo.automationtesting.in/Register.html

# Step2: Collect the specific locator for radio buttons from DOM 

# Step3: Verifies page contains a radio button 

# Step4: Select the radio button with id and its value ‘FeMale’ or ‘Male’ 

# Step5: Verify radio button is selected or not 

*** Settings ***
Library    SeleniumLibrary
Resource    CreateUserKeyWord.robot

*** Test Cases ***

Testting Radio Buttons
    [Documentation]    Testting Radio Buttons
    Start TestCase
    Verify radio button
    Finish TestCase

*** Keywords ***
Start TestCase
    Open Browser    https://demo.automationtesting.in/Register.html    Chrome
    Maximize Browser Window
    Sleep    3

Verify radio button
    Page Should Contain Radio Button    xpath:(//input[@name='radiooptions'])
    Page Should Not Contain Radio Button    xpath:(//input[@name='radiooptions123'])
    Radio Button Should Not Be Selected    radiooptions
    Select Radio Button    radiooptions   FeMale
    Select Radio Button    radiooptions   Male
    Radio Button Should Be Set To    radiooptions   Male


Finish TestCase
    Close Browser