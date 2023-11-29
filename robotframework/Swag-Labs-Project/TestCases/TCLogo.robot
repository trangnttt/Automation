*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${transform}    "translate3d(-100%, 0px, 0px)"

*** Test Cases ***
Test Case Menu
    Open Browser    https://www.saucedemo.com/    chrome
    Input Text    id:user-name    standard_user
    Input Text    id:password   secret_sauce
    Click Button    id:login-button
    Element Should Contain    xpath://span[@class='title']    Products
    Sleep    2
    Verify display menu
    Click Button    id:react-burger-menu-btn
    Verify display menu

*** Keywords ***
Verify display menu
    ${for_value}=   Get Element Attribute  xpath://div[@class='bm-menu-wrap']   aria-hidden
    IF    '${for_value}' == 'false'
        Log   Menu is enabled.
    ELSE
        Log  Menu is disabled.
    END