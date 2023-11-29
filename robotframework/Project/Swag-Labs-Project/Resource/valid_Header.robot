*** Settings ***
Library    SeleniumLibrary

*** Keywords ***
Verify display menu
    ${for_value}=   Get Element Attribute  xpath://div[@class='bm-menu-wrap']   aria-hidden
    IF    '${for_value}' == 'false'
        Log   Menu is enabled.
    ELSE
        Log  Menu is disabled.
    END

Verify text logo menu
    Element Text Should Be    xpath://div[@class='app_logo']    Swag Labs

Verify icon Cart
    Element Text Should Not Be    xpath://a[@class='shopping_cart_link']    not_expected