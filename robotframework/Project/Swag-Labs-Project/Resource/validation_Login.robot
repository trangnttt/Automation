*** Settings ***
Library    SeleniumLibrary
Variables    ../Variables/Variables_WebElemt.py

*** Variables ***
${usernames}    standard_user
${password}    secret_sauce


${usernames_invalid}    standard_user1
${password_invalid}    secret_sauce1

${usernames_locked}    locked_out_user


${titleLoginPass}    Products
${usernamesNull}    Epic sadface: Username is required
${passwordNull}    Epic sadface: Password is required
${user_or_pass_invalid}    Epic sadface: Username and password do not match any user in this service
${usernameLocked}    Epic sadface: Sorry, this user has been locked out.


*** Keywords ***
Test Case Login with username is null and password valid
    Input Text    ${LoginPassword}   ${password}
    Click Button    ${LoginBtnLogin}
    Element Should Contain    ${CheckLogin_Fail}    ${usernamesNull}
    Reload Page

Test Case Login with username is valid and password null
    Input Text    ${LoginUserName}    ${usernames}
    Click Button    ${LoginBtnLogin}
    Element Should Contain    ${CheckLogin_Fail}    ${passwordNull}
    Reload Page


Test Case Login with username and password is null
    Click Button    ${LoginBtnLogin}
    Element Should Contain    ${CheckLogin_Fail}    ${usernamesNull}
    Reload Page


Test Case Login with username invalid, password valid
    Input Text    ${LoginUserName}    ${usernames_invalid}
    Input Text    ${LoginPassword}   ${password}
    Click Button    ${LoginBtnLogin}
    Element Should Contain    ${CheckLogin_Fail}    ${user_or_pass_invalid}
    Reload Page


Test Case Login with username valid, password invalid  
    Input Text    ${LoginUserName}     ${usernames}
    Input Text    ${LoginPassword}   ${password_invalid}
    Click Button    ${LoginBtnLogin}
    Element Should Contain    ${CheckLogin_Fail}    ${user_or_pass_invalid}
    Reload Page

Test Case Login with username invalid, password invalid
    Input Text    ${LoginUserName}     ${usernames_invalid}
    Input Text    ${LoginPassword}   ${password_invalid}
    Click Button    ${LoginBtnLogin}
    Element Should Contain    ${CheckLogin_Fail}    ${user_or_pass_invalid}
    Reload Page

Test Case Login with usename has been locked out
    Input Text    ${LoginUserName}     ${usernames_locked} 
    Input Text    ${LoginPassword}   ${password}
    Click Button    ${LoginBtnLogin}
    Element Should Contain    ${CheckLogin_Fail}   ${usernameLocked}
    Reload Page


Test Case Login with username and password valid
    Input Text    ${LoginUserName}    ${usernames}
    Input Text    ${LoginPassword}   ${password}
    Click Button    ${LoginBtnLogin}
    Element Should Contain    ${CheckLogin_Pass}    ${titleLoginPass}    
    Sleep    2
