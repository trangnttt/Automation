*** Settings ***
Library    SeleniumLibrary
Resource    ../Resource/CommonFunctionality.robot
Resource    ../Resource/validation_Search.robot
Library    Collections
Variables    .././Variables/Variables_WebElemt.py

# Test Setup    CommonFunctionality.Start TestCase
# Test Teardown    CommonFunctionality.Finish TestCase

*** Variables ***
@{logo_url}         http://opencart.abstracta.us/index.php?route=common/home
# *** Test Cases ***
# Test Case Header
#     Check logo
#     Check search
#     Check button cart default

*** Keywords ***

Test Case Header
    Check logo
    Check search
    Check button cart default
    
Check logo
    Element Should Contain    ${Logo}    Your Store
    Element Attribute Value Should Be    ${link_Login}    href    @{logo_url} 

Check search
    validation_Search.Verify search with value null
    validation_Search.Verify search with value invalid
    validation_Search.Verify search with value valid
    validation_Search.Verify search with value emoji

Check button cart default
    Click Button    ${btn_Cart}
    ${display_BtnCart} =    Get Element Attribute    ${btn_Cart}    aria-expanded 
    IF    '${display_BtnCart} == true'
        Element Should Be Enabled    //div[@id='cart']//p
        Log    dropdown btn Cart enable
    END

    