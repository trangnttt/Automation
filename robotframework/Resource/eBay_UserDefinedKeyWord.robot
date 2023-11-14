*** Settings ***
Library    SeleniumLibrary

*** Keywords ***
Verify Search Results
    Input Text    xpath://input[@id="gh-ac"]   mobile
    Press Keys    xpath://input[@id="gh-btn"]    RETURN

Filter results by condition
    Mouse Over    //div[@class="srp-controls__resize-display"]/span[1]
    Sleep    4
    Click Element   //div[@class="srp-controls__resize-display"]/span[1]
    Mouse Over    //div[@class="srp-controls__resize-display"]/span[1]/span/ul/li[2]
    Click Element    //div[@class="srp-controls__resize-display"]/span[1]/span/ul/li[2]

Verify Filter Results
    Element Should Contain    xpath://div[@id="srp-river-results"]//span[text() = "8910 Original NOKIA 8910 Mobile Phone 2G GSM 900/1800 Unlocked phone One year wa"]    8910 Original NOKIA 8910 Mobile Phone 2G GSM 900/1800 Unlocked phone One year wa
