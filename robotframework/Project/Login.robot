*** Settings ***
Library    SeleniumLibrary
Resource    ./Resource/valid_login.robot
Resource    ./Resource/invalid_login.robot

Test Setup    Open Browser To Login Page
Test Teardown    Close Browser

*** Variables ***
${BROWSER}        Chrome
${URL_LOGIN}      https://cms.anhtester.com/login

*** Test Cases ***
Test Case Login
    invalid_login.Verify Test Case Login with Invalid Username
    invalid_login.Verify Test Case Login with Invalid Password
    valid_login.Verify Test Case Login Pass

*** Keywords ***
Open Browser To Login Page
    Open Browser    ${URL_LOGIN}    ${BROWSER}
    Maximize Browser Window

