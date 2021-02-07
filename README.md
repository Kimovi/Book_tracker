# Book tracker - Library book tracking system
This is a Book tracking web application for book lovers! 
You can run a mini library with your books, we will help you keep on track with your books. Simply just add all your books and trace who has borrowed your book. 


# Intro
I've been having lots of fun with web development using Javascript and React, Now it's the time to step up for me. This time, I've built a CRUD web application with Python and Flask, which is running on my GCP cloud instance with SQL Database. Furthermore, I have used Jenkins for CI delivery. 
That sounds a lot of work, right? I have adopted an Agile methodology to effectively control the project workflow. 
Here are more details of the tools I have used for this project. 

- Trello Board
- Google Cloud Platform for a VM instance
- SQL Database on GCP instance
- Python and Flask programming + Jinja2 for HTML rendering
- Unit testing with Pytest
- Git for version control
- Jenkins for CI delivery
- ERD and CI diagrams to understand the workflow clearly
- Risk Assessment

I have built a Library book tracking system to ensure any books you have, and who is possessing which item.
The application is very simple, and straightforward. Just input your booklist into the main page, then go to the 'user' page to add the user's detail and which book was borrowed by adding book id number. Once the item is returned to you, then simply just delete the user detail. 


# Kanban board
Ok, so there were lots of work needed to build this project and also lots of tools were used. 
To keep on track with everything, I've used Trello board to organize tasks, gather resources I've used, added user stories to ensure all the functions are added correctly. 

<img width="1280" alt="Kanban" src="https://user-images.githubusercontent.com/59723479/107147034-b37d7100-6943-11eb-9751-0a0e1cb6501f.png">


This is how my Kanban board looked like at the beginning of the project. (https://trello.com/b/M1miz90V/book-tracker)

<img width="1280" alt="Kanban1" src="https://user-images.githubusercontent.com/59723479/107147039-b7a98e80-6943-11eb-9f80-09ccea830ceb.png">

This is how it looks like by end of the project. As you can see, each task completed is moved under the 'done' list. 


# ERD (Entity-Relationship Diagram)
I've learned how to set up and use SQL DB on my GCP VM instance, So I wanted to use my instance for DB as well. At this point, I was lost about what to do. so this is what I did :

<img width="849" alt="ERD" src="https://user-images.githubusercontent.com/59723479/107147030-b1b3ad80-6943-11eb-904d-183931a3e8f4.png">

As you can see from the above picture, I've created ERD for my DB structure to visualize what I will need to do. It was easy and keen to understand how I should structure the Database schema.
To design my project, I needed a relational database to ensure there are two separated tables having a one-to-many relationship.
'Users' and 'Book' tables are connected by Primary key and Foreign key where each user can access book lists.


# Pytest
After building up the CRUD function and connect my application to the SQL database on the instance, I ran the unit test with Pytest as my code was written in Python. The purpose of the test was to ensure CRUD functions are working without an error. 

I have tested 4 big parts such as creating DB and add values, access to the designed URLs, update values, and delete values. 

<img width="640" alt="Pytest-warning" src="https://user-images.githubusercontent.com/59723479/107147042-b8dabb80-6943-11eb-8e60-35a083539f50.png">

On the first attempt of running the test, I had a total of 95% pass result and 1 warning which I did not understand. As the test was showing great results, I ran the project on Jenkins which did not work at all. The issue I was having was that as soon as Pytest running on Jenkins, it will collect the test but it never ends, just like an infinity loading. To fix this error, I had amended some test cases and eliminated unessential tests but it still did not work. After spending lots of time fixing it, I only noted that the warning I had was the problem. It was then simply fixed by adding one line of code [app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False]

<img width="1033" alt="Pytest" src="https://user-images.githubusercontent.com/59723479/107147041-b8422500-6943-11eb-9731-8c2213c0d972.png">

This is how it looks like after fixing the error. test coverage went down 95% to 90% as I eliminated unessential tests.


# Continuous Integration Workflow diagram
I have used Jenkins for CI server to the automation of the project. I used VScode for writing the code, commit and push it to Github repository. This will automatically push to Jenkins which I installed it on GCP instance and trigger shell script where I stored commands for running the project such as installing requirements.txt, running Pytest, and deploy with Gunicorn. 

<img width="635" alt="Pytest_jenkins" src="https://user-images.githubusercontent.com/59723479/107153266-7aa1c400-6964-11eb-92da-8edc8eb54f03.png">

If test was passed, it will be deployed by Gunicorn.


# Risk assessment
As this project was mainly focused on implementing a CRUD function with DB using cloud instance and use Jenkins server for CI delivery, there were lots of things I could not manage at this point. 
Please see below a summarization of possible risks.

|Risk Description|Assessment|Impact|Action to take|  
|---|---|---|---|
|Incorrect input value|As there is no validation checker, the user can input empty value to the input box|Low|Add validation checker|
|Non-admin to amend data without permission|Any users can amend or delete data without admin's permissioin|High|Add login system where admin can control the data flow|
|SQL database failure|In case of DB failure, all the data stored would be wiped|High|Create a backup DB|
|GCP instance failure|In case of instance failure, the entire application wouldn't work as SQL and Jenkins are running on the instance|High|Create a backup instance|


# Contributor
Bora Kim