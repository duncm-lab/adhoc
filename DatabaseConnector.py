import MySQLdb as dtb
from _mysql_exceptions import OperationalError, ProgrammingError
import sys

class DatabaseConnector():
    """Initialisation requires Server, Username, Password, Database. 
    Methods:
    CreateQuery - takes an SQL statement.
    dbConn - Connects to database , creates a cursor and executes 
    values given in CreateQuery
    """ 
    def __init__(self, svr='non', usr='non', pwd='non', db='non'):
        try:
            self._con = dtb.connect(svr, usr, pwd, db)
            self._curs = self._con.cursor()
        except OperationalError as e:
            if e[0] == 2005:
                print "The server was incorrect."
                sys.exit()
            elif e[0] == 1045:
                print "The username or password was incorrect"
                sys.exit()
            elif e[0] == 1049:
                print "The Database Name is wrong"
                sys.exit()
            else:
                print "This is an unknown error"
    
    def dbQuery(self, qry="SHOW TABLES"):
        try:
            self._curs.execute(qry)
            check = raw_input("%s has been entered type 'yes' to confirm: " % qry )
            if check == 'yes':
                self._con.commit()
            else:
                print "The query has not been commited" 
        except ProgrammingError:
            print "The query entered was invalid."
        finally:
            self._con.close()
