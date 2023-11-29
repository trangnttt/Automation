*** Settings ***
Library    SeleniumLibrary
Resource    ./HeaderPage.robot

*** Variables ***
${search_results}    results for


*** Keywords ***
Verify Search Results
    Page Should Contain    ${search_results} ${search_text}

# Select product condition

# Select delivery options