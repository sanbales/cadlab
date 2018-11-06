*** Settings ***
Library  SeleniumLibrary
Resource  ../../resources/Launch.robot
Resource  ../../resources/Shell.robot
Resource  ../../resources/Notebook.robot
Test Template   Can I make a Robot Notebook?

*** Test Cases ***
Chrome   headlesschrome
Firefox  headlessfirefox

*** Keywords ***
Can I make a Robot Notebook?
  [arguments]  ${browser}
  Set Tags    browser:${browser}
  Open RobotLab  ${browser}
  Launch a new  Robot Framework  Notebook
  Capture Page Screenshot  01_notebook.png
  Add and Run Cell  | *Test Case* |${\n}| Hello |${\n}| | Log | Hello World
  Capture Page Screenshot  02_execute.png
  Wait Until Kernel Is Idle
  Capture Page Screenshot  03_execute_result.png
  The Robot Popup Should Contain  Log  1 passed, 0 failed
  The Robot Popup Should Contain  Report  All tests passed
  Execute JupyterLab Command    Save Notebook
  Capture Page Screenshot  05_save.png

The Robot Popup Should Contain
  [Arguments]  ${document}  ${msg}
  Click Link    ${document}
  Sleep  0.5s
  Select Window  Jupyter ${document}
  Page Should Contain  ${msg}
  Capture Page Screenshot  04_${document.lower()}.png
  Close Window
  Select Window  JupyterLab