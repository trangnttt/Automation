*** Settings ***
Library    SeleniumLibrary
Variables    ../Variables/Variables_WebElemt.py
Resource    ../Resource/validation_Login.robot

*** Keywords ***
Test Case Login
    validation_Login.Test Case Login with username is null and password valid
    validation_Login.Test Case Login with username is valid and password null
    validation_Login.Test Case Login with username and password is null
    validation_Login.Test Case Login with username invalid, password valid
    validation_Login.Test Case Login with username valid, password invalid
    validation_Login.Test Case Login with username invalid, password invalid
    validation_Login.Test Case Login with usename has been locked out
    validation_Login.Test Case Login with username and password valid
