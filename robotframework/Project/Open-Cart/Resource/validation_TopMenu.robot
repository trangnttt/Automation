*** Settings ***
Library         SeleniumLibrary
Resource        ../Resource/CommonFunctionality.robot
Library         Collections
Variables       .././Variables/Variables_WebElemt.py

*** Variables ***
@{data_linkTopMenu}         http://opencart.abstracta.us/index.php?route=information/contact     https://opencart.abstracta.us/index.php?route=account/account     https://opencart.abstracta.us/index.php?route=account/wishlist     http://opencart.abstracta.us/index.php?route=checkout/cart     https://opencart.abstracta.us/index.php?route=checkout/checkout
@{icon_TopMenu}    fa fa-phone    fa fa-user    fa fa-heart    fa fa-shopping-cart    fa fa-share
@{text_subMenu_TopMenu}    Register    Login 
@{link_subMenu_TopMenu}    https://opencart.abstracta.us/index.php?route=account/register    https://opencart.abstracta.us/index.php?route=account/login


*** Keywords ***
# Left Top Menu
Check display data Currency
    ${dataCurrency}    Create List    € Euro    £ Pound Sterling    $ US Dollar
    ${countCurrency}    Get Element Count    ${elm_countCurrency}
    ${listCurrency}    Create List
    FOR    ${i}    IN RANGE    1    ${countCurrency}+1
        ${text}    Get Text    //div[@class='pull-left']//ul[@class='dropdown-menu']//li[${i}]
        Append To List    ${listCurrency}    ${text}
    END
    Lists Should Be Equal    ${listCurrency}    ${dataCurrency}    -----Currency pass data-----

Click item Currency
    Mouse Down    ${elm_chosseCurrency}
    Click Element    ${elm_chosseCurrency}
    Element Text Should Be    ${elm_btnCurrency}    £

# Right Top Menu
Check Icon Text and Link Menu of Top Menu
    ${item_topMenu}    Create List    123456789    My Account    Wish List (0)    Shopping Cart    Checkout
    ${count_item_topMenuRight}    Get Element Count    ${elm_countMenuTop}
    
    ${listIcon_TopMenuRight}    Create List 
    ${listText_TopMenuRight}    Create List
    ${listLink_TopMenuRight}    Create List 

    FOR    ${i}    IN RANGE    1    ${count_item_topMenuRight}+1
        # Check icon
        ${icon-menu}    Get Element Attribute    xpath=//div[@id='top-links']//ul[@class='list-inline']/li[${i}]//i    class
        Append To List    ${listIcon_TopMenuRight}    ${icon-menu}
        
        # Check text 
        ${text}    Get Text    //div[@id='top-links']//ul[@class='list-inline']/li[${i}]
        Append To List    ${listText_TopMenuRight}    ${text}
        
        # Check link 
        ${link_url}    Get Element Attribute    xpath=//div[@id='top-links']//ul[@class='list-inline']/li[${i}]/a    href
        Append To List    ${listLink_TopMenuRight}    ${link_url}

    END

    Should Be Equal    ${listIcon_TopMenuRight}    ${icon_TopMenu}    -----Icons pass data-----
    Lists Should Be Equal    ${listText_TopMenuRight}    ${item_topMenu}    -----Texts pass data-----
    Should Be Equal    ${listLink_TopMenuRight}    ${data_linkTopMenu}    -----Links pass data-----

Check sub menu of Top Menu    
    Click Element    ${elmt_SubMenuTop}

    ${count_submenu_TopMenu} =    Get Element Count    ${elmt_countSubMenuTop}
    ${listTextSubMenu_TopMenuRight}    Create List 
    ${listLinkSubMenu_TopMenuRight}    Create List 

    FOR    ${i}    IN RANGE    1    ${count_submenu_TopMenu}+1
        # Check text 
        ${text}    Get Text    //div[@id='top-links']//ul[@class='list-inline']/li[2]//li[${i}]
        Append To List    ${listTextSubMenu_TopMenuRight}    ${text}

        # Check link 
        ${link_url}    Get Element Attribute    xpath=//div[@id='top-links']//ul[@class='list-inline']/li[2]//li[${i}]/a    href
        Append To List    ${listLinkSubMenu_TopMenuRight}    ${link_url}
    END
    Should Be Equal    ${listTextSubMenu_TopMenuRight}    ${text_subMenu_TopMenu}    -----Text Sub menu of Top Menu pass data-----
    Should Be Equal    ${listLinkSubMenu_TopMenuRight}    ${link_subMenu_TopMenu}    -----Link Sub menu of Top Menu pass data-----
    Reload Page