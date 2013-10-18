#PyQt and Databases

This code is designed to help you learn about the Git version control system and also how to make use of the **QSQL module** in PyQt to simplify working with databases and PyQt based user interfaces.

##Git

Git is a **version control** system - this means that it can help you keep track of the changes you make to your code. This is incredibly useful as you will often want to try new things and know that you can always go back to an older version if your changes don't work out.

Git is installed on all of the Computers in the Computing and ICT department and you can download and install it for free at home. Today you are going to take your first steps learning how to work with Git.

###Getting started

1. Create an account on the [GitHub website][3]
2. **Fork** this repository - you will probably need to make use of the help and support section of the website.
3. Open the GitHub application on your machine and set it up for use with your account
4. Clone your copy of this repository to the computer
5. Open the files in Idle

##Exploring the repository

The **PyQtDatabases** repository that you have cloned contains the beginnings of an application to manage a Coffee Shop. It is far from complete however and over the next few weeks we will add to and improve the program.

There are four files currently:

- main_interface.py
- sql_connection.py
- add_customer.py
- coffee_shop.db

You will need to explore these files to answer the questions below.

###Code questions

1. Why has the code for the **AddCustomerWidget** been separated into its own file?
2. How does the **AddCustomerWidget** communicate with the **ShopWindow** widget?
3. Why has the code for the **SQLConnection** object been separated into its own file?
4. What does a QAction represent?
5. How could the code for the QActions be improved? You may need to refer to the [PyQt documentation][2]
6. Make one improvement to the code for a QAction

##Committing changes

Now that you have made a change to the code you need to **commit** that change to your local repository (your copy of the code).

1. Find out how to **commit** a change using the Windows GitHub application (see [Windows help][1])
2. Commit the change to your repository
3. Find out how to **roll-back** any changes you commit

Having had a little taste of commiting changes can you answer the following question:

1. Why is it important to commit your changes frequently?

##Building the application

At the moment the application is pretty threadbare - only the add customer feature works. However, there is already a bug in the code! On Windows the menu bar does not show up as expected.

1. Find out how to add the menu bar to the **ShopWindow** class properly and then make the necessary change in your code - remember to commit your change afterwards!
2. Add the code necessary to **add products** to the database - your teacher may give you a user interface design to work from

##Pushing your changes

It is probably towards the end of the period now (if not then well done for moving so fast!) and you will want to **push** your code to the remote repository so that you can pick the code up again at home.

1. Find out how to push the changes you have made your local repository to the remote repository
2. Push your code!

##Wrapping up
Today you have had a brief introduction to version control and we have started to think about how to use databases with PyQt. There are lots of cool things you can do with GitHub and we will explore these in future lessons.

Finally, take a look at the code for this **README** file. [Markdown][4] is awesome. 



[1]: http://windows.github.com/help
[2]: http://pyqt.sourceforge.net/Docs/PyQt4/classes.html
[3]: http://www.github.com
[4]: http://daringfireball.net/projects/markdown/



