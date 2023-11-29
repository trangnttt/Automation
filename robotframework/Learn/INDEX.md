1. *** Tạo first test case basic ***
FirstTestCase.robot
2. *** Convert Manual Test into Automation Script *** 
- Manual img: https://prnt.sc/oLGc8pHqZ8cC
ConvertManualTest.robot
3. *** How to Create User Defined Keywords ***
CreateUserKeyWord.robot
4. *** Move User Defined Keywords to Resource File ***
- Manual img: https://prnt.sc/q0aMWcZbDc_R
BasicSearch.robot => Resource

5. *** Implement POM in Robot Framework ***
Verify_search_functionality.robot
Resource - HeaderPage
         - SearchResultPage

6. *** Variable Scope ***
VariableScope.robot 

7. *** How to Handle Radio ***
WorkingWithRadio.robot

- Page Should Contain Radio Button- verifies radio button locator found from the current page. 
- Page Should Not Contain Radio Button– Verifies radio button locator is not found on the current page 
- Radio Button Should Not Be Selected – Verifies radio button Group group_name has no selection  
- Select Radio Button – Sets the radio button group Group_name to value   
- Radio Button Should Be Set To – Verifies set radio button Group group_name to value 

8. *** How to Handle Checkbox ***
WorkingWithCheckbox.robot

9. *** How to Handle Frame ***
WorkingWithFrame.robot

10. *** How to Handle Alert ***
WorkingWithAlert.robot

- Handle Alert – Handles the current alert and returns its message.
- Input Text Into Alert – Types the given text into an input field in an alert.  
- Alert Should Be Present – Verifies that an alert is present and by default, accepts it  
- Alert Should Not Be Present – Verifies that no alert is present. 

11. *** How to Handle Mouse Actions ***
WorkingWithMouseActions.robot

- Mouse Down: Using this keyword we can simulate pressing the left mouse button on an element. 
- Mouse Up: Using this keyword we can simulate releasing the left mouse button on the element. 
- Mouse Down On Link: Using this keyword we can simulate the mouse down event on the link. 
- Mouse Over: Using this keyword we can simulate hovering the mouse over the element. 
- Mouse Out: Using this keyword we can simulate moving away from the element. 
- Mouse Down On Image: Using this keyword we can simulate a mouse down event on the image. 
- Drag And Drop: Using this keyword we can drag an element from its position and drop it into the target element. 
- Open Context menu: Using this keyword we can perform the right-click operations. This keyword will open the context menu on the element. 

12. *** IF-ELSE ***
IF-ELSE.robot

13. *** FOR ***
FOR.robot


 *** PROJECT ***
 Login bằng robot framework