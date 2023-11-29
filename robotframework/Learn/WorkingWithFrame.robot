*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
TC with Frame
    Open Browser    https://the-internet.herokuapp.com/nested_frames    Chrome
    Set Selenium Implicit Wait    3
    Select Frame    name:frame-top
    Select Frame  name:frame-left
    Current Frame Should Contain    LEFT

    Unselect Frame

    Select Frame    name:frame-bottom
    Current Frame Should Contain    BOTTOM
    Close Browser