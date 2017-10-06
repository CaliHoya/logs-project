#!/usr/bin/env python2.7

import psycopg2

DBNAME = "news"


def article_rank():
    """Return the 3 most popular articles"""
    db = psycopg2.connect(dbname=DBNAME)
    c = db.cursor()
    c.execute("select title, count(title) as views from \"pathslug\" "
              "group by title order by views desc limit 3")
    article_table = c.fetchall()
    db.close()
    print "\nThree Most Popular Articles All Time:"
    for article in article_table:
        print str(article[0]) + " - " + str(article[1]) + " views"


def author_rank():
    """Return the most popular article authors"""
    db = psycopg2.connect(dbname=DBNAME)
    c = db.cursor()
    c.execute("select name, count(name) as views from \"authorpath\" "
              "group by name order by views desc")
    author_table = c.fetchall()
    db.close()
    print "\nMost Popular Article Authors of All Time:"
    for author in author_table:
        print str(author[0]) + " - " + str(author[1]) + " views"


def error_report():
    """Return the error rate on each day"""
    db = psycopg2.connect(dbname=DBNAME)
    c = db.cursor()
    c.execute("select to_char(time,'FMMonth DD, YYYY') as date, "
              "round((sum(case when status = '200 OK' "
              "then 0 else 1 end)::decimal / count(*)) * 100,2) "
              "as percent_error from log group by date "
              "having (sum(case when status = '200 OK' "
              "then 0 else 1 end)::decimal / count(*)) * 100 > 1")
    error_table = c.fetchall()
    db.close()
    print "\nDates on Which Over 1% of Requests Led to Errors:"
    for error in error_table:
        print str(error[0]) + " - " + str(error[1]) + "%"

article_rank()
author_rank()
error_report()
