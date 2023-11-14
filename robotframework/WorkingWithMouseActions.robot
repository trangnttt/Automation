*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
TC with Mouse Actions
    Open Browser    https://the-internet.herokuapp.com/    Chrome
    Set Selenium Implicit Wait    3
    
    Mouse Down    xpath://a[text()="Drag and Drop"]
    Mouse Up    xpath://a[text()="Drag and Drop"]
    Drag And Drop    //div[@id="column-a"]    xpath://div[@id='column-b']
    Go Back
    Click Element    xpath://a[text()='Hovers']
    Mouse Over    xpath://div[@class='example']//div[1]//img[1]
    Mouse Out    xpath://div[@class='example']//div[1]//img[1]
    Go Back
    Click Element   xpath://a[normalize-space()='Context Menu']
    Open Context Menu   xpath://div[@id='hot-spot']


    Close Browser
