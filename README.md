Overview
========

Aqueous is a project I started many years ago as as a PHP website.  I actually
only got as far as the database design and life got in the way which didn't
give me enough time to work on the project.  It is now at least 4 years since I
initially started the project and a lot has changed.  I still don't really have
a great deal of time to devote to such a project, but technology has progressed
and I have hopes of getting something actually functional up and running

Technology
==========
I am not doing any PHP development anymore, and have since become interested in
Python.  As such I am going to develop this as a Django app.  It is strictly a
web and database app, so Django is perfectly suited for the job.  In the last
iteration, I chose PostgreSQL as the database backend.  Basically because at
the time it vastly outdid the MySQL of the day.  Since I am migrating this to
Django, the database back-end doesn't matter as much.  You can choose to
utilize whatever works for you, and of course is supported by Django.

Goals
=====
With a projec that has been on the back-burner longer than I have actively
worked on it, I find it hard to define goals for the project at all.  But to
give some idea of what I have in mind:

Project Goals
----------------
1.  Getting something actually functionally working
2.  Manage multiple aquariums
3.  Manage maintenance tasks
4.  Alerting (email definitely, perhaps using something like pushover.net)
5.  Creating a multi-user environment that could be hosted or self-deployed

Bigger goals
------------
1.  Mobile-specific view (phone specific.)
2.  I'd love to integrate with something like Encyclopedia of Life (eol.org)
    for species identification and logging
