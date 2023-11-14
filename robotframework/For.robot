
*** Settings ***
Library    SeleniumLibrary

*** Variables ***
@{robots} =    Bender    Johnny5    Terminator    Robocop    Joh

*** Test Cases ***
Test Case with FOR
    FOR    ${robot}    IN    @{robots}
        Log    ${robot}
    END
    
Test Case with FOR using CONTINUE
    FOR    ${robot}    IN    @{robots}
        IF    $robot == 'Terminator'  CONTINUE
        Log    ${robot}
    END

Test Case with FOR using BREAK
    FOR    ${robot}    IN    @{ROBOTS}
        IF    $robot == 'Johnny5'    BREAK
        Log    ${robot}
    END