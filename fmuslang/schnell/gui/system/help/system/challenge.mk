--% crossover

ATTENTION! YOUR APPLICATION WILL BE REJECTED IF IT:
- Does not compile
- Does not contain unit tests
- Unit tests are failing

Requirements:
Objective
Create a public news publishing portal where news can be published and disseminated

Instructions:
- Try to complete as much as possible within the given time frame. 
If you need more time, please ask for an extension. 
You must complete full-functionality of the application 
  with industry-level coding style/commenting. 
Unfinished assignments will not be considered.
- Please note that you are expected to work on the assignment independently. 
Discussing assignment details with colleagues or any indication of outside help 
  will be considered cheating.
- Please do not expect too much hand-holding as this is an evaluation assignment.
- Read the complete assignment before you start. 
  Understand clearly what is required so that your work will be appropriate and easier.

Preconditions
- You should work on your local machine.
- You may use any IDE or editor for developing the application.
- You must use the latest PHP7 version compatible with required libraries.
- You must use Nginx or Apache or IIS as the web server.
- You must use MySQL as database.
- You must use one of these frameworks:
  Laravel
  CodeIgniter
  Yii2
  Symfony2
- Failing to follow these rules will invalidate your submission and you will not be evaluated.

Delivery for this assignment should consist of an archive named <your_name> - Software Engineer - PHP.zip
containing the following:
- Source code/project
  Application Demo
  - Record the demonstration of the application using Wink. Do not upload the video. Save it to your local machine.
  Database script
  - Create a single SQL script file to create the database, its schema and any stored procedure you may use.
- Wink recording, download version 2 from Wink, render the video to swf format
- Readme.txt containing the instructions to configure and run the application, notes and feedback
  Readme
  - Create a txt file with the following information
  - Steps to create and initialize the database
  - Steps to prepare the source code to build/run properly
  - Any assumptions made and missing requirements that are not covered in the specifications
  - Any feedback you may wish to give about improving the assignment
- Design.doc with needed diagrams
  Design diagrams
  - Create a doc file containing the following information and diagrams
  - List of technologies and design patterns used
  - An overall activity or sequence diagram
  - An overall layer or component interaction diagram

To be evaluated
1. The quality of the output (functionality)
2. Code quality and completeness
3. Technologies applied
4. Extra validations and assumptions which are not described
5. Add missing requirements to the implementation, according to your experience

Technical Specifications
- Use MVC design.
- Use MySQL database. Create the needed tables.
- Use a PDF export library.
- Create a single application with the publishing, newsstand and RSS service.
- Use PHP Mailer as mailing library.
- Apply input validations and constraints wherever necessary to create a stable application.
- Even if you are not able to complete all the tasks, try to achieve a working application.

Functional Specifications
Create a public news publishing system where people can report or read news
I. News publishing web application
I.1 Any user could register with an email address. 
The application sends a verification link to the email address. 
When the user clicks the link, the application asks for a new password 
  (can be tested on localhost w/o need for a public domain). 
Now the user is registered and is able to publish news. 
Without this verification user cannot publish news.

I.2 After log in the user could see his own published news list, remove or publish a new article.
No edit of news is permitted.

I.3 For each news article the following information is required
  I.3.1 News title
  I.3.2 A single photo
  I.3.3 News text
  I.3.4 Current date and time
  I.3.5 Reporter user name / email

I.4 Newsstand web application available w/o log in for general public
  I.4.1 Users could see the news highlights. Latest 10 news only.
  I.4.2 Upon clicking an article highlight, the user is able to view a complete article.
  I.4.3 The user is able to download a PDF file of the displayed news article.

I.5 A News RSS feed service
  I.5.1 An RSS feed can be subscribed to, which includes latest 10 news articles

--#

--% ghost
cara kerja: kita oprek yg sudah dikerjakan di spor...
lalu coba apply ke react yg kita punya...

Discussion

[avatar] [text area                                   ] [comment]
[avatar] [name] [time ago]
         [content]
         [upvote] [reply]
...
[avatar] [name] [time ago]
         [content]
         [upvote] [reply]
...
         [avatar] [name] [time ago]
                  [content]
                  [upvote] [reply]
...
--#
