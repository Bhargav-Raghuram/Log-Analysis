# Log-Analysis
Final project of the UDACITY Full Stack Developer NanoDegree

## Technologies used
1. PostgreSQL
2. Python



## System setup 
This project makes use of Udacity's Linux-based virtual machine (VM) configuration which includes all of the necessary software to run the application.
1. Download [Vagrant](https://www.vagrantup.com/) and install.
2. Download [Virtual Box](https://www.virtualbox.org/) and install. 
3. Clone this repository to a directory of your choice.
4. Download the **newsdata.sql** (extract from **newsdata.zip**) and **Log_analysis.py** files from the respository and move them to your **vagrant** directory within your VM.

#### Run these commands from the terminal in the folder where your vagrant is installed in: 
1. ```vagrant up``` to start up the VM.
2. ```vagrant ssh``` to log into the VM.
3. ```cd /vagrant``` to change to your vagrant directory.
4. ```psql -d news -f newsdata.sql``` to load the data and create the tables.
5. ```python3 Log_analysis.py``` to run the reporting tool.

## Views used
#### article_view
````sql
CREATE VIEW article_view AS 
SELECT title,author,count(*) as num_views 
FROM articles,log 
WHERE log.path like concat('%',articles.slug) 
GROUP BY articles.title,articles.author 
ORDER BY num_views DESC;
````
#### error_view
````sql
CREATE VIEW error_view AS 
SELECT date(time),round(100.0*sum(case log.status when '200 OK' 
then 0 else 1 end)/count(log.status),2) as "Percentage Error" from log group by date(time) 
ORDER BY "Percentage Error" DESC;
````
