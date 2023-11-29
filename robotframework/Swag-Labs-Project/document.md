check https://www.saucedemo.com/

- Resource
- Variable
- TestCases
    - TCLogin.robot
- TestSuites

*** Login ***
Test Case Login gồm các case basic như:
1. Usename, Password valid
2. Usename null, Password valid
3. Usename valid, Password is null
4. Usename, Password null
5. Usename invalid, Password valid
6. Usename valid, Password invalid
7. Usename invalid, Password invalid
8. Usename has been locked out

* Các trường hợp test (Resource/validation_Login.robot) => Find Element (Variables/Variables_WebElemt.py) => run Test Case(TestCases/TCLogin.robot)


*** Menu ***
 # Click Element    id:react-burger-menu-btn
    # Sleep    2
    
    # IF ${transform} == "translate3d(-100%, 0px, 0px)"
    #     Log  Toggle is disabled.
    # ELSE ${transform} != "translate3d(0px, 0px, 0px)"
    #     Log  Toggle is enabled.

    # Should Be Equal  ${transform}  "translate3d(-100%, 0px, 0px)"  (deLoscription="Toggle is disabled.")
    # Sleep    2
    # Click Element    id:react-burger-menu-btn
    # Should Be Equal  ${transform}  "translate3d(-100%, 0px, 0px)"  (description="Toggle is enabled.")
    # Sleep    2
    # Should Be Equal  ${color}  "#132322"  (description="Check if h3 color is red")


    # Should Be Equal  ${transform}  "translate3d(-100%, 0px, 0px)"
    # Log    Menu is disabled
    # Sleep    2
    # Click Element    id:react-burger-menu-btn
    # Sleep    2
    # Should Be Equal  ${transform}  "translate3d(-100%, 0px, 0px)"
    # Log    Menu is enabled
    # Sleep    2



TC
    Open Browser    http://www.google.com    Chrome

    # a CSS property from the element.
    ${element_prop}=    Get CSS Property Value    id=SIvCob    line-height
    Should Be Equal As Strings    ${element_prop}    28px

    # a CSS property inherited from the <body> tag.
    ${body_prop}=    Get CSS Property Value    id=SIvCob    font-family
    Should Be Equal As Strings    ${body_prop}    arial, sans-serif

*** Keywords ***
Get CSS Property Value
    [Documentation]
    ...    Get the CSS property value of an Element.
    ...    
    ...    This keyword retrieves the CSS property value of an element. The element
    ...    is retrieved using the locator.
    ...    
    ...    Arguments:
    ...    - locator           (string)    any Selenium Library supported locator xpath/css/id etc.
    ...    - property_name     (string)    the name of the css property for which the value is returned.
    ...    
    ...    Returns             (string)    returns the string value of the given css attribute or fails.
    ...        
    [Arguments]    ${locator}    ${attribute name}
    ${css}=         Get WebElement    ${locator}
    ${prop_val}=    Call Method       ${css}    value_of_css_property    ${attribute name}
    [Return]     ${prop_val}