## UI tests for Stellar Burgers

Url: https://stellarburgers.nomoreparties.site/ 

**Password recovery - test_password_recovery:**
- go to the password recovery page using the “Recover Password” button,
- enter your email and click on the “Restore” button,
- clicking on the show/hide password button makes the field active.

**Personal account - test_profile:**
- click on “Personal Account”,
- go to the “Order History” section,
- log out of your account.

**The main functionality of the constructor is test_constructor:**
- click on “Constructor”,
- click on “Order Feed”,
- if you click on an ingredient, a pop-up window with details will appear,
- the pop-up window can be closed by clicking on the cross,
- when adding an ingredient to an order, the counter of this ingredient increases,
- a logged-in user can place an order.

**Section “Order Feed” - test_feed:**
- if you click on an order, a pop-up window with details will open,
- user orders from the “Order History” section are displayed on the “Order Feed” page,
- when creating a new order, the Completed counter for all time increases,
- when creating a new order, the Completed for today counter increases,
- after placing an order, its number appears in the In progress section.


The browser is selected in conftest in the driver fixture parameters: Chrome or Firefox\
Running tests: python -m pytest tests\
Reading run results: allure serve allure_results 
