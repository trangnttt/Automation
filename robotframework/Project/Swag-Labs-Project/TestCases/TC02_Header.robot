*** Settings ***
Library    SeleniumLibrary
Resource    ../Resource/valid_Header.robot


*** Keywords ***
Test Case Header
    # Open Browser    https://www.saucedemo.com/    chrome
    # Input Text    id:user-name    standard_user
    # Input Text    id:password   secret_sauce
    # Click Button    id:login-button
    # Element Should Contain    xpath://span[@class='title']    Products
    # Sleep    2
    valid_Header.Verify display menu
    Click Button    id:react-burger-menu-btn
    valid_Header.Verify display menu
    valid_Header.Verify text logo menu
    valid_Header.Verify icon Cart
