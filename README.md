# Instawork Django Assessment  

 

# App Description 

 

A simple team-member management application that allow the user to view, edit, add, and delete team members. The app consists of 3 pages. 

 

Team members 
You have 4 team members 
Adrien Olczak (Admin) 
(415) 310-1618 
adrien@instawork.com 
Charlene Pham 
(415) 310-1619 
charlene@instawork.com 
Benson Mach 
(415) 310-1621 
benson@instawork.com 
Dan Petrie 
(415) 310-1620 
dan@instawork.com 

Add a team member 
Set email, location and role. 
Info 
First Name 
Last Name 
Email 
Phone Number 
Role: 
Regular - Can't delete members 
Admin - Can delete members 
O 
Save 
Edit team member 
Edit contact info, location and role. 
Info 
Charlene 
Pham 
Charlene@instawork.com 
(415) 310-1619 
Role: 
Regular - Can't delete members 
Admin - Can delete members 
Delete 
O 
Save 
 

  

Estimated time spent: ~14 hours 

 

## Requirements  

 

Python3 

https://www.python.org/downloads/ 

Pip3  

https://www.geeksforgeeks.org/how-to-install-pip-in-macos/ 

 

 

## Setup 

 

Clone the project, open a new terminal & cd into your directory 

 

```cd Instawork-Django-Assessment``` 

 

Create a virtual environment  

 

```python3 –m venv venv``` 

 

Enable the virtual environment  

 

```source venv/bin/activate```  

 

Install Django 

 

```python3 –m pip install Django``` 

 

Install the following modules  

 

``` 

pip install django-db-logger 

pip install django-phonenumber-field 

pip install django-phonenumbers 

pip install django-multiselectfield 

 

``` 

Lastly 

 

```Python3 manage.py runserver```  

 

Click on the port link to run the application 

 

## Testing 

 

### Home Page 

 


 

 

On the home page, click on the plus sign at the top right to direct you to the Add Page.  

 

Click on any of the listed members to be directed to its edit page. 

 

### Add Page  

 

Add a team member 
Set email, location and role. 
Info 
First Name 
Last Name 
Email 
Phone Number 
Role: 
Regular - Can't delete members 
Admin - Can delete members 
O 
Save 
 

Clicking save before filling out the form completely should throw a message 'Please fill out this field' for the fields that are blank. 

 

Fill the form completely with invalid formatting for email and phone number. Clicking save should result in the following messages. 

 

• Enter a valid email address. 
test 
• Enter a valid phone number (e.g. (201) 555-0123) or a number with 
an international call refix. 
3123 
 

Re-enter the fields with a valid email and phone number and click save. This should redirect you back to the home page.  

 

On the home page, you should see the newly created member at the bottom of the list. The sub-heading at the top should say 'You have 5 team members', reflecting the actual amount of members being listed.  

 

Go back to the Add page and fill in the form with valid information. This time, select Admin under 'Role' and click Save. On the bottom of the home page, you should see the newly created member with an '(Admin)' attached to the right of the member's name.  

 

### Edit Page  

 

Edit team member 
Edit contact info, location and role. 
Info 
Charlene 
Pham 
Charlene@instawork.com 
(415) 310-1619 
Role: 
Regular - Can't delete members 
Admin - Can delete members 
Delete 
O 
Save 
 

Similar to the Add page, clicking Save with empty fields will result in error messages that prevent the edit from taking place. 

 

Fill in the form with valid information. Select Admin under 'Role' and click Save. On the bottom of the home page, you should see the edited member with an '(Admin)' attached to the right of the member's name. 

 

Go back to an Edit page. Clicking Delete will redirect you back to the home page and you should no longer see the deleted team member in the list.  

 

 

 

 

 

 

 

 
