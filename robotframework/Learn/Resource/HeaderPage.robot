*** Settings ***
Library    SeleniumLibrary
Variables    ./Variables_WebElemt.py

*** Variables ***
${search_text}    mobile
# ${search_text_box}    xpath://input[@id="gh-ac"]
# ${search_button}     xpath://input[@id="gh-btn"]
# ${search_Advanced}     xpath://a[@id="gh-as-a"]

*** Keywords ***
Input Search Text and Click Search
    Input Text   ${HomePageSearchTextBox}    ${search_text}
    Press Keys    ${HomePageSearchButton}    RETURN

Click on Advanced Search Link
    Click Element    ${HomePageSearchAdvanced} 

    