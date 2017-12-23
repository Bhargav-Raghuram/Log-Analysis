#! /usr/bin/env python
import psycopg2

DB_NAME = "news"


def query_result(query):
    ''' CONNECT TO THE DATABASE AND EXECUTE THE QUERY'''
    db_conn = psycopg2.connect(database=DB_NAME)
    cur = db.cursor()
    cur.execute(query)
    return cur.fetchall()
    db_conn.close()

# Question 1: WHAT ARE THE MOST POPULAR 3 ARTICLES OF ALL TIME?
query1 = ''' select title,count(*) as num_views from articles,log where
log.path=CONCAT('/article/',articles.slug) group by articles.title order by
num_views DESC limit 3 '''

# Question 2: WHO ARE THE MOST POPULAR ARTICLE AUTHORS OF ALL TIME  ?
query2 = ''' select authors.name,sum(article_view.num_views) as views from
article_view,authors where authors.id = article_view.author
group by authors.name order by views desc '''

# Question 3: ON WHICH DAYS DID MORE THAN 1% OF REQUESTS LEAD TO ERRORS?
query3 = "select * from error_view where \"Percentage Error\" > 1"


def query1_results(query):
    result = query_result(query)
    print('\nQuery 1: THE 3 MOST POPULAR ARTICLES OF ALL TIME :\n')
    for res in result:
        print ('\t' + str(res[0]) + ' - ' + str(res[1]) + ' views')


def query2_results(query):
    result = query_result(query)
    print('\nQuery 2: THE MOST POPULAR ARTICLE AUTHORS OF ALL TIME :\n')
    for res in result:
        print ('\t' + str(res[0]) + ' - ' + str(res[1]) + ' views')


def query3_results(query):
    result = query_result(query)
    print('\nQuery 3: DAYS ON WHICH MORE THAN 1% OF REQUESTS LEAD TO ERRORS :\n')
    for res in result:
        print ('\t' + str(res[0]) + ' - ' + str(res[1]) + ' %')

#CALL THE FUNCTIONS TO PRINT THE RESUTS
query1_results(query1)
query2_results(query2)
query3_results(query3)
