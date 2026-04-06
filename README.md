File Name: Troubleshooters POS system
Author: Timore Bennett
Date Created: April 5, 2026
Course:ITT103
GitHub Public URL to Code: https://github.com/rgb-timore/Troubleshooters-POS-sy.git

##OVERVIEW
- This is a basic POS system built using Python with predefined products, stocks and prices.
- I will assume that whoever runs this program has some basic knowledge of python and has an IDE (integrated Development Environment). Here is a link to a free online IDE: https://www.online-ide.com/ to run the program in the browser.

##HOW TO USE
- Run the .py file in the IDE of choice
- Add items from the preprogrammed list using number from 1 to 12
- Remove items that were added to the customers cart by entering "r" or "R" then enter the item number to remove one quantity at a time
- To checkout enter "q" or "Q"
- Enter the money received from customer which the system will do the calculations
- A simple receipt is then printed

Example of the receipt:
=============================================
---------------WALMART RECEIPT---------------
=============================================
Adidas shoes         x4  $40.00
Hanes shirt          x1  $8.50
PlayStation 4        x1  $100.00
=============================================
Items: 6
Subtotal:        $148.50
Discount:       -$14.85
Tax (10%):      +$13.37
=============================================
TOTAL:           $147.02
Cash:            $500.00
Change:          $352.99
=============================================
   Thank you for shopping!
=============================================

##FEATURES
- The system displays items added to the cart in real-time
- A 10% tax is applied to each purchase, and a 5% discount is applied for every 3 items. The discount increases as more items are added (eg. 3 items 5%, 6 items 10%, 9items 15%)
- Some items may reach 0 stock. This is intentional to demonstrate how the system handles low or out-of-stock items
