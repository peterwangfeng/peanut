#------------------------------------------------------------------------------
# Copyright 2016, 2017, Oracle and/or its affiliates. All rights reserved.
#
# Portions Copyright 2007-2015, Anthony Tuininga. All rights reserved.
#
# Portions Copyright 2001-2007, Computronix (Canada) Ltd., Edmonton, Alberta,
# Canada. All rights reserved.
#------------------------------------------------------------------------------

"""Module for testing connections."""

import threading

class TestConnection(TestCase):

    def __ConnectAndDrop(self):
        """Connect to the database, perform a query and drop the connection."""
        connection = cx_Oracle.connect(self.username, self.password,
                self.tnsentry, threaded = True)
        cursor = connection.cursor()
        cursor.execute("select count(*) from TestNumbers")
        count, = cursor.fetchone()
        self.assertEqual(count, 10)

    def setUp(self):
        self.username = USERNAME
        self.password = PASSWORD
        self.tnsentry = TNSENTRY

    def verifyArgs(self, connection):
        self.assertEqual(connection.username, self.username,
                "user name differs")
        self.assertEqual(connection.tnsentry, self.tnsentry,
                "tnsentry differs")

    def testAllArgs(self):
        "connection to database with user, password, TNS separate"
        connection = cx_Oracle.connect(self.username, self.password,
                self.tnsentry)
        self.verifyArgs(connection)

    def testBadConnectString(self):
        "connection to database with bad connect string"
        self.assertRaises(cx_Oracle.DatabaseError, cx_Oracle.connect,
                self.username)
        self.assertRaises(cx_Oracle.DatabaseError, cx_Oracle.connect,
                self.username + "@" + self.tnsentry)
        self.assertRaises(cx_Oracle.DatabaseError, cx_Oracle.connect,
                self.username + "@" + self.tnsentry + "/" + self.password)

    def testBadPassword(self):
        "connection to database with bad password"
        self.assertRaises(cx_Oracle.DatabaseError, cx_Oracle.connect,
                self.username, self.password + "X", self.tnsentry)

    def testEncodings(self):
        "connection with only encoding or nencoding specified should work"
        connection = cx_Oracle.connect(self.username, self.password,
                self.tnsentry)
        encoding = connection.encoding
        nencoding = connection.nencoding
        connection = cx_Oracle.connect(self.username, self.password,
                self.tnsentry, encoding = "UTF-8")
        self.assertEqual(connection.encoding, "UTF-8")
        self.assertEqual(connection.nencoding, nencoding)
        connection = cx_Oracle.connect(self.username, self.password,
                self.tnsentry, nencoding = "UTF-8")
        self.assertEqual(connection.encoding, encoding)
        self.assertEqual(connection.nencoding, "UTF-8")

    def testExceptionOnClose(self):
        "confirm an exception is raised after closing a connection"
        connection = cx_Oracle.connect(self.username, self.password,
                self.tnsentry)
        connection.close()
        self.assertRaises(cx_Oracle.DatabaseError, connection.rollback)

    def testMakeDSN(self):
        "test making a data source name from host, port and sid"
        formatString = "(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)" + \
                "(HOST=%s)(PORT=%d))(CONNECT_DATA=(SID=%s)))"
        args = ("hostname", 1521, "TEST")
        result = cx_Oracle.makedsn(*args)
        self.assertEqual(result, formatString % args)

    def testSingleArg(self):
        "connection to database with user, password, TNS together"
        connection = cx_Oracle.connect("%s/%s@%s" % \
                (self.username, self.password, self.tnsentry))
        self.verifyArgs(connection)

    def testVersion(self):
        "connection version is a string"
        connection = cx_Oracle.connect(self.username, self.password,
                self.tnsentry)
        self.assertTrue(isinstance(connection.version, str))

    def testRollbackOnClose(self):
        "connection rolls back before close"
        connection = cx_Oracle.connect(self.username, self.password,
                self.tnsentry)
        cursor = connection.cursor()
        cursor.execute("truncate table TestTempTable")
        otherConnection = cx_Oracle.connect(self.username, self.password,
                self.tnsentry)
        otherCursor = otherConnection.cursor()
        otherCursor.execute("insert into TestTempTable (IntCol) values (1)")
        otherConnection.close()
        cursor.execute("select count(*) from TestTempTable")
        count, = cursor.fetchone()
        self.assertEqual(count, 0)

    def testRollbackOnDel(self):
        "connection rolls back before destruction"
        connection = cx_Oracle.connect(self.username, self.password,
                self.tnsentry)
        cursor = connection.cursor()
        cursor.execute("truncate table TestTempTable")
        otherConnection = cx_Oracle.connect(self.username, self.password,
                self.tnsentry)
        otherCursor = otherConnection.cursor()
        otherCursor.execute("insert into TestTempTable (IntCol) values (1)")
        del otherCursor
        del otherConnection
        cursor.execute("select count(*) from TestTempTable")
        count, = cursor.fetchone()
        self.assertEqual(count, 0)

    def testThreading(self):
        "connection to database with multiple threads"
        threads = []
        for i in range(20):
            thread = threading.Thread(None, self.__ConnectAndDrop)
            threads.append(thread)
            thread.start()
        for thread in threads:
            thread.join()

