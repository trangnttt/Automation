*** Settings ***
Library    SeleniumLibrary
Resource    ../Resource/CommonFunctionality.robot
Resource    ../Resource/validation_TopMenu.robot
Library    Collections
Variables    ../Variables/Variables_WebElemt.py

*** Variables ***
@{logo_url}         http://opencart.abstracta.us/index.php?route=common/home
${value_invalid_Search}    search-invalid
${value_valid_Search}    Macbook
${value_emoji_Search}    ^^


*** Keywords ***
Verify search with value valid 
    Input Text    ${input_search}    ${value_valid_Search}
    Click Button    ${btn_search}
    Element Should Contain    ${txt_search}    Search - ${value_valid_Search}
    Search condition

Verify search with value invalid
    Input Text    ${input_search}     ${value_invalid_Search}
    Click Button    ${btn_search}
    Element Should Contain    ${txt_search}    Search - ${value_invalid_Search}
    Search condition

Verify search with value null
    Click Button    ${btn_search}
    Element Should Contain    ${txt_search}    Search   
    Search condition

Verify search with value emoji
    Input Text    ${input_search}    ${value_emoji_Search}
    Click Button    ${btn_search}
    Element Should Contain    ${txt_search}    Search - ${value_emoji_Search}
    Search condition


Search condition
    ${count_ItemSearch} =    Get Element Count    ${count_proSearch}
    IF    ${count_ItemSearch} > 0
        Log    Search have ${count_ItemSearch} products

    ELSE
        Element Should Contain    ${empty_Search}    Your shopping cart is empty!
    END
