*** Settings ***
Resource  resource.robot
Resource  login_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page
Test Teardown  Reset Application

*** Test Cases ***
Register With Valid Username And Password
    Set Username  kaaleppi
    Set Password  kuomaseni17
    Confirm Password  kuomaseni17
    Submit Registration
    Registration Should Succeed

Register With Too Short Username And Valid Password
    Set Username  k
    Set Password  kuomaseni17
    Confirm Password  kuomaseni17
    Submit Registration
    Registration Should Fail With Message  Username does not fulfill requirements

Register With Valid Username And Invalid Password
# salasana sisältää vain kirjainmerkkejä
    Set Username  kaaleppi
    Set Password  saleeAivanHyva
    Confirm Password  saleeAivanHyva
    Submit Registration
    Registration Should Fail With Message  Password does not fulfill requirements

# salasana ei ole tarpeeksi pitkä
    Set Username  kaaleppi
    Set Password  lyhyt1
    Confirm Password  lyhyt1
    Submit Registration
    Registration Should Fail With Message  Password does not fulfill requirements

Register With Nonmatching Password And Password Confirmation
    Set Username  kaaleppi
    Set Password  ensimmainen1
    Confirm Password  toinen2erilainen
    Submit Registration
    Registration Should Fail With Message  Passwords should match

Login After Successful Registration
    Set Username  kaaleppi
    Set Password  kuomaseni17
    Confirm Password  kuomaseni17
    Submit Registration
    Registration Should Succeed
    Go To Login Page
    Set Username  kaaleppi
    Set Password  kuomaseni17
    Submit Credentials
    Login Should Succeed

Login After Failed Registration
    Set Username  :)
    Set Password  xkcd/327
    Confirm Password  xkcd/327
    Submit Registration
    Registration Should Fail With Message  Username does not fulfill requirements
    Go To Login Page
    Set Username  :)
    Set Password  xkcd/327
    Submit Credentials
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Registration Should Succeed
    Welcome Page Should Be Open

Registration Should Fail With Message
    [Arguments]  ${message}
    Registration Page Should Be Open
    Page Should Contain  ${message}

Confirm Password
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Submit Registration
    Click Button  Register
