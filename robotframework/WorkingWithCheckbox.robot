# Open the browser and copy URL − https://demo.automationtesting.in/Register.html in Chrome.
# Verify that the page contains CheckBox.
# Verify that the page does not contain CheckBox. Provided the locator for Radio button.
# Check “Cricket” and “Hockey” options of CheckBox.
# Uncheck “Hockey” option of CheckBox.
# Verify that “Cricket“ option of CheckBox is checked.
# Verify that “Hockey“ option of CheckBox is not checked.

*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***

Testting CheckBox Buttons
    [Documentation]    Testting CheckBox Buttons
    Open the Browser with URL
    Verifies page contains a checkbox
    Select the checkbox options Cricket and Hockey
    Unselect the checkbox option Hockey
    Verify Checkbox option Cricket is selected
    Verify Checkbox option Hockey is not selected
    
*** Keywords ***
Open the browser with URL
    Open Browser    https://demo.automationtesting.in/Register.html    Chrome
    Set Selenium Implicit Wait    2

Verifies page contains a checkbox
    Page Should Contain Checkbox    id:checkbox1
    Page Should Not Contain Checkbox   name:radiooptions   #This is the locator for Radio Button

Select the checkbox options Cricket and Hockey
    Select Checkbox    id:checkbox1
    Select Checkbox    id:checkbox3

Unselect the checkbox option Hockey
    Unselect Checkbox    id:checkbox3

Verify Checkbox option Cricket is selected
    Checkbox Should Be Selected    id:checkbox1

Verify Checkbox option Hockey is not selected
    Checkbox Should Not Be Selected    id:checkbox3