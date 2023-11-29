*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
TC with Alert
    Open Browser    https://demo.automationtesting.in/Alerts.html    Chrome
    Set Selenium Implicit Wait    3
    
    Click Element    //div[@id="OKTab"]/button
    # Handle Alert    accept
    # Handle Alert    dismiss
    # Handle Alert    leave
    Alert Should Be Present    I am an alert box!

    Close Browser