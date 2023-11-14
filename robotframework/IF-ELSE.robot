
*** Settings ***
Library    SeleniumLibrary
Library    String

*** Test Cases ***
My Test Case
    IF    "cat" == "dog"
        Log    Đúng nha
    ELSE
        Log    Sai nè
    END

    IF    len("cat") == 3
        Log    This line IS executed.
    END
    IF    (1 == 1 and 2 == 2) and 3 == 3
        Log    This line IS executed since the expressions evaluate to True.
    END
    IF    (1 == 2 or 3 == 4) or 3 == 3
        Log    This line IS executed since one of the expressions evaluates to True.
    END

Use Run Keyword If in Robot Framework
    Run Keyword If    ${True}    Log    This line IS executed.
    Run Keyword If    ${False}    Log    This line is NOT executed.
