# Logs-Analysis

## Project Overview
For this project, I was tasked to create a reporting tool that prints out reports in (plain text) based on the data in a database. This reporting tool is a Python program using the **psycopg2** module to connect to the database.

## The report should answer the following questions:
- What are the most popular three articles of all time?
- Who are the most popular article authors of all time?
- On which days did more than 1% of requests lead to errors?

## Set up the environment
- Install **Python3**
- Install **VirtualBox**
- Install **Vagrant**
- Fork or clone https://github.com/udacity/fullstack-nanodegree-vm repository
- Place the Article.py of this repo under the /vagrant directory
- Download the database script, unzip and place it under the /vagrant directory
- Navigate to the /vagrant directory and run `vagrant up` to start the virtual machine
- Run `vagrant ssh` to log in the virtual machine
- Run `psql -d news -f newsdata.sql`
- To connect database run `psql -d news`
- Create the database and views

### Run the following code to create the necessary views:
```
CREATE VIEW most_popular_articles as
SELECT articles.title, count(log.path) as views
    FROM articles, log
    WHERE log.path LIKE '%' || articles.slug
    GROUP BY articles.title
    ORDER BY views desc;

CREATE VIEW most_popular_author as
SELECT authors.name, count(log.path) as author_views
    FROM authors, articles, log
    WHERE status != '404 NOT FOUND'
    AND articles.author = authors.id
    AND log.path LIKE '%' || articles.slug || '%'
    GROUP BY authors.name
    ORDER BY author_views desc;
    
CREATE VIEW mistake_each_day as
SELECT to_char(log.time, 'FMMonth DD, YYYY') "day", count(log.status) as errors
    FROM log
    WHERE status = '404 NOT FOUND'
    GROUP BY 1
    ORDER BY 1;
```    
```        
CREATE VIEW requests_per_day as
SELECT to_char(log.time, 'FMMonth DD, YYYY') "day", count(log.status) as requests
    FROM log
    GROUP BY 1
    ORDER BY 1;
   
        
CREATE VIEW errors_day as
SELECT mistake_each_day.day, concat(ROUND((100.0 * mistake_each_day.errors / requests_per_day.requests), 2), '%')as percent_errors
    FROM mistake_each_day, requests_per_day
    WHERE mistake_each_day.day = requests_per_day.day
    AND ((100.0 * mistake_each_day.errors / requests_per_day.requests) > 1)                                         ORDER BY percent_errors desc;
```        
- Within the VM, navigate to **cd /vagrant**
- Execute the file `python Article.py`
