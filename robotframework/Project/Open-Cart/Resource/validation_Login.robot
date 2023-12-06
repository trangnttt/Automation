*** Settings ***
Library    SeleniumLibrary
Variables    ../Variables/Variables_WebElemt.py

*** Variables ***
${email}    qua31601@nezid.com
${password}    123123

${title_page}    My Account

${email_invalid}    email_invalid
${password_invalid}    123456

*** Keywords ***
Verify email and password valid
    Input Text    ${input_email}   ${email}
    Input Text    ${input_password}    ${password}
    Click Button    ${btn_Login}
    Title Should Be    ${title_page}

Verify email and password null
    Click Button    ${btn_Login}
    Page Should Contain Element    ${txt_errors}

Verify email null
    Input Text    ${input_password}    ${password}
    Click Button    ${btn_Login}
    Page Should Contain Element    ${txt_errors}
    Clear Element Input
    

Verify password null
    Input Text    ${input_email}    ${email}
    Click Button    ${btn_Login}
    Sleep    2
    Page Should Contain Element    ${txt_errors}
    Clear Element Input

Verify email invalid
    Input Text    ${input_email}   ${email_invalid}
    Input Text    ${input_password}    ${password}
    Click Button    ${btn_Login}
    Page Should Contain Element    ${txt_errors}
    Clear Element Input


Verify password invalid
    Input Text    ${input_email}   ${email}
    Input Text    ${input_password}    ${password_invalid}
    Click Button    ${btn_Login}
    Page Should Contain Element    ${txt_errors}
    Clear Element Input

Verify email and password invalid
    Input Text    ${input_email}   ${email_invalid}
    Input Text    ${input_password}    ${password_invalid}
    Click Button    ${btn_Login}
    Page Should Contain Element    ${txt_errors}
    Clear Element Input

Clear Element Input
    Clear Element Text    ${input_email}
    Clear Element Text    ${input_password}