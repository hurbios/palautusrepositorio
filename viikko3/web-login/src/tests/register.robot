*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  kallekaks
    Set Password  kalle123
    Set Password confirmation  kalle123
    Submit Registeration
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  k
    Set Password  kalle123
    Set Password confirmation  kalle123
    Submit Registeration
    Register Should Fail With Message    Username too short

Register With Valid Username And Too Short Password
    Set Username  kalle2
    Set Password  kall3
    Set Password confirmation  kall3
    Submit Registeration
    Register Should Fail With Message    Password too short

Register With Valid Username And Invalid Password
    Set Username  kalle3
    Set Password  kallekalle
    Set Password confirmation  kallekalle
    Submit Registeration
    Register Should Fail With Message    Password does not meet criteria

Register With Nonmatching Password And Password Confirmation
    Set Username  kallekaks
    Set Password  kalle123
    Set Password confirmation  kalle124
    Submit Registeration
    Register Should Fail With Message    Passwords do not match

Register With Username That Is Already In Use
    Set Username  kalle
    Set Password  kalle123
    Set Password confirmation  kalle123
    Submit Registeration
    Register Should Fail With Message    User with username kalle already exists

Login After Successful Registration
    Set Username  kallekaks
    Set Password  kalle123
    Set Password confirmation  kalle123
    Submit Registeration
    Register Should Succeed
    Logout
    Set Username  kallekaks
    Set Password  kalle123
    Submit Credentials
    Login Should Succeed

Login After Failed Registration
    Set Username  k
    Set Password  kalle123
    Set Password confirmation  kalle123
    Submit Registeration
    Register Should Fail With Message    Username too short
    Go To Login Page
    Set Username  kallekaks
    Set Password  kalle123
    Submit Credentials
    Login Should Fail With Message    Invalid username or password

*** Keywords ***
Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Submit Registeration
    Click Button  Register

Submit Credentials
    Click Button  Login

Register Should Succeed
    Welcome Page Should Be Open

Logout
    Go To Loggedin Page
    Click Button    Logout

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain    ${message}

Login Should Succeed
    Main Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}

*** Keywords ***
Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To Register Page