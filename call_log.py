#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('calls.db')
curs = conn.cursor()

def log_call():
    with conn:
        curs.execute("INSERT INTO logged_calls(id) VALUES(null);")


def ring_back():
    with conn:
        curs.execute("INSERT INTO logged_calls(event) VALUES('Called customer');")
  

def rang_IT():
    with conn:
        curs.execute("INSERT INTO logged_calls(event) VALUES('Rang IT');")
  


#if __name__ == '__main__':
#    log_call()
