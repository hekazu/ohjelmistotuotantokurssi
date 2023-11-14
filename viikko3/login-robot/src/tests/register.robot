*** Settings ***
Resource  resource.robot
Test Setup  Input Register Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  kaaleppi  kuomaseni17
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kaaleppi  kuomaseni17
    Output Should Contain  New user registered
    Input Register Command
    Input Credentials  kaaleppi  lottovoitto2024
    Output Should Contain  User with username kaaleppi already exists

Register With Too Short Username And Valid Password
    Input Credentials  k  kuomaseni17
    Output Should Contain  Username does not fulfill requirements

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials  kaaleppi1  kuomaseni17
    Output Should Contain  Username does not fulfill requirements

Register With Valid Username And Too Short Password
    Input Credentials  kaaleppi  shorty7
    Output Should Contain  Password does not fulfill requirements

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  kaaleppi  pitkasanaonpitka
    Output Should Contain  Password does not fulfill requirements
