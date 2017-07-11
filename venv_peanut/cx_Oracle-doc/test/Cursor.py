#------------------------------------------------------------------------------
# Copyright 2016, 2017, Oracle and/or its affiliates. All rights reserved.
#
# Portions Copyright 2007-2015, Anthony Tuininga. All rights reserved.
#
# Portions Copyright 2001-2007, Computronix (Canada) Ltd., Edmonton, Alberta,
# Canada. All rights reserved.
#------------------------------------------------------------------------------

"""Module for testing cursor objects."""

import cx_Oracle
import sys

class TestCursor(BaseTestCase):

    def testCreateScrollableCursor(self):
        """test creating a scrollable cursor"""
        cursor = self.connection.cursor()
        self.assertEqual(cursor.scrollable, False)
        cursor = self.connection.cursor(True)
        self.assertEqual(cursor.scrollable, True)
        cursor = self.connection.cursor(scrollable = True)
        self.assertEqual(cursor.scrollable, True)
        cursor.scrollable = False
        self.assertEqual(cursor.scrollable, False)

    def testExecuteNoArgs(self):
        """test executing a statement without any arguments"""
        result = self.cursor.execute("begin null; end;")
        self.assertEqual(result, None)

    def testExecuteNoStatementWithArgs(self):
        """test executing a None statement with bind variables"""
        self.assertRaises(cx_Oracle.ProgrammingError, self.cursor.execute,
                None, x = 5)

    def testExecuteEmptyKeywordArgs(self):
        """test executing a statement with args and empty keyword args"""
        simpleVar = self.cursor.var(cx_Oracle.NUMBER)
        args = [simpleVar]
        kwArgs = {}
        result = self.cursor.execute("begin :1 := 25; end;", args, **kwArgs)
        self.assertEqual(result, None)
        self.assertEqual(simpleVar.getvalue(), 25)

    def testExecuteKeywordArgs(self):
        """test executing a statement with keyword arguments"""
        simpleVar = self.cursor.var(cx_Oracle.NUMBER)
        result = self.cursor.execute("begin :value := 5; end;",
                value = simpleVar)
        self.assertEqual(result, None)
        self.assertEqual(simpleVar.getvalue(), 5)

    def testExecuteDictionaryArg(self):
        """test executing a statement with a dictionary argument"""
        simpleVar = self.cursor.var(cx_Oracle.NUMBER)
        dictArg = { "value" : simpleVar }
        result = self.cursor.execute("begin :value := 10; end;", dictArg)
        self.assertEqual(result, None)
        self.assertEqual(simpleVar.getvalue(), 10)

    def testExecuteMultipleMethod(self):
        """test executing a statement with both a dict arg and keyword args"""
        simpleVar = self.cursor.var(cx_Oracle.NUMBER)
        dictArg = { "value" : simpleVar }
        self.assertRaises(cx_Oracle.InterfaceError, self.cursor.execute,
                "begin :value := 15; end;", dictArg, value = simpleVar)

    def testExecuteAndModifyArraySize(self):
        """test executing a statement and then changing the array size"""
        self.cursor.execute("select IntCol from TestNumbers")
        self.cursor.arraysize = 20
        self.assertEqual(len(self.cursor.fetchall()), 10)

    def testCallProc(self):
        """test executing a stored procedure"""
        var = self.cursor.var(cx_Oracle.NUMBER)
        results = self.cursor.callproc("proc_Test", ("hi", 5, var))
        self.assertEqual(results, ["hi", 10, 2.0])

    def testCallProcNoArgs(self):
        """test executing a stored procedure without any arguments"""
        results = self.cursor.callproc("proc_TestNoArgs")
        self.assertEqual(results, [])

    def testCallFunc(self):
        """test executing a stored function"""
        results = self.cursor.callfunc("func_Test", cx_Oracle.NUMBER,
                ("hi", 5))
        self.assertEqual(results, 7)

    def testCallFuncNoArgs(self):
        """test executing a stored function without any arguments"""
        results = self.cursor.callfunc("func_TestNoArgs", cx_Oracle.NUMBER)
        self.assertEqual(results, 712)

    def testExecuteManyByName(self):
        """test executing a statement multiple times (named args)"""
        self.cursor.execute("truncate table TestTempTable")
        rows = [ { "value" : n } for n in range(250) ]
        self.cursor.arraysize = 100
        statement = "insert into TestTempTable (IntCol) values (:value)"
        self.cursor.executemany(statement, rows)
        self.connection.commit()
        self.cursor.execute("select count(*) from TestTempTable")
        count, = self.cursor.fetchone()
        self.assertEqual(count, len(rows))

    def testExecuteManyByPosition(self):
        """test executing a statement multiple times (positional args)"""
        self.cursor.execute("truncate table TestTempTable")
        rows = [ [n] for n in range(230) ]
        self.cursor.arraysize = 100
        statement = "insert into TestTempTable (IntCol) values (:1)"
        self.cursor.executemany(statement, rows)
        self.connection.commit()
        self.cursor.execute("select count(*) from TestTempTable")
        count, = self.cursor.fetchone()
        self.assertEqual(count, len(rows))

    def testExecuteManyWithPrepare(self):
        """test executing a statement multiple times (with prepare)"""
        self.cursor.execute("truncate table TestTempTable")
        rows = [ [n] for n in range(225) ]
        self.cursor.arraysize = 100
        statement = "insert into TestTempTable (IntCol) values (:1)"
        self.cursor.prepare(statement)
        self.cursor.executemany(None, rows)
        self.connection.commit()
        self.cursor.execute("select count(*) from TestTempTable")
        count, = self.cursor.fetchone()
        self.assertEqual(count, len(rows))

    def testExecuteManyWithRebind(self):
        """test executing a statement multiple times (with rebind)"""
        self.cursor.execute("truncate table TestTempTable")
        rows = [ [n] for n in range(235) ]
        self.cursor.arraysize = 100
        statement = "insert into TestTempTable (IntCol) values (:1)"
        self.cursor.executemany(statement, rows[:50])
        self.cursor.executemany(statement, rows[50:])
        self.connection.commit()
        self.cursor.execute("select count(*) from TestTempTable")
        count, = self.cursor.fetchone()
        self.assertEqual(count, len(rows))

    def testExecuteManyWithResize(self):
        """test executing a statement multiple times (with resize)"""
        self.cursor.execute("truncate table TestTempTable")
        rows = [ ( 1, "First" ),
                 ( 2, "Second" ),
                 ( 3, "Third" ),
                 ( 4, "Fourth" ),
                 ( 5, "Fifth" ),
                 ( 6, "Sixth" ),
                 ( 7, "Seventh and the longest one" ) ]
        sql = "insert into TestTempTable (IntCol, StringCol) values (:1, :2)"
        self.cursor.executemany(sql, rows)
        self.cursor.execute("""
                select IntCol, StringCol
                from TestTempTable
                order by IntCol""")
        fetchedRows = self.cursor.fetchall()
        self.assertEqual(fetchedRows, rows)

    def testExecuteManyWithExecption(self):
        """test executing a statement multiple times (with exception)"""
        self.cursor.execute("truncate table TestTempTable")
        rows = [ { "value" : n } for n in (1, 2, 3, 2, 5) ]
        statement = "insert into TestTempTable (IntCol) values (:value)"
        self.assertRaises(cx_Oracle.DatabaseError, self.cursor.executemany,
                statement, rows)
        self.assertEqual(self.cursor.rowcount, 3)

    def testPrepare(self):
        """test preparing a statement and executing it multiple times"""
        self.assertEqual(self.cursor.statement, None)
        statement = "begin :value := :value + 5; end;"
        self.cursor.prepare(statement)
        var = self.cursor.var(cx_Oracle.NUMBER)
        self.assertEqual(self.cursor.statement, statement)
        var.setvalue(0, 2)
        self.cursor.execute(None, value = var)
        self.assertEqual(var.getvalue(), 7)
        self.cursor.execute(None, value = var)
        self.assertEqual(var.getvalue(), 12)
        self.cursor.execute("begin :value2 := 3; end;", value2 = var)
        self.assertEqual(var.getvalue(), 3)

    def testExceptionOnClose(self):
        "confirm an exception is raised after closing a cursor"
        self.cursor.close()
        self.assertRaises(cx_Oracle.InterfaceError, self.cursor.execute,
                "select 1 from dual")

    def testIterators(self):
        """test iterators"""
        self.cursor.execute("""
                select IntCol
                from TestNumbers
                where IntCol between 1 and 3
                order by IntCol""")
        rows = []
        for row in self.cursor:
            rows.append(row[0])
        self.assertEqual(rows, [1, 2, 3])

    def testIteratorsInterrupted(self):
        """test iterators (with intermediate execute)"""
        self.cursor.execute("truncate table TestTempTable")
        self.cursor.execute("""
                select IntCol
                from TestNumbers
                where IntCol between 1 and 3
                order by IntCol""")
        testIter = iter(self.cursor)
        if sys.version_info[0] >= 3:
            value, = next(testIter)
        else:
            value, = testIter.next()
        self.cursor.execute("insert into TestTempTable (IntCol) values (1)")
        if sys.version_info[0] >= 3:
            self.assertRaises(cx_Oracle.InterfaceError, next, testIter)
        else:
            self.assertRaises(cx_Oracle.InterfaceError, testIter.next)

    def testBindNames(self):
        """test that bindnames() works correctly."""
        self.assertRaises(cx_Oracle.ProgrammingError, self.cursor.bindnames)
        self.cursor.prepare("begin null; end;")
        self.assertEqual(self.cursor.bindnames(), [])
        self.cursor.prepare("begin :retval := :inval + 5; end;")
        self.assertEqual(self.cursor.bindnames(), ["RETVAL", "INVAL"])
        self.cursor.prepare("begin :retval := :a * :a + :b * :b; end;")
        self.assertEqual(self.cursor.bindnames(), ["RETVAL", "A", "B"])
        self.cursor.prepare("begin :a := :b + :c + :d + :e + :f + :g + " + \
                ":h + :i + :j + :k + :l; end;")
        self.assertEqual(self.cursor.bindnames(),
                ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L"])
        self.cursor.prepare("select :a * :a + :b * :b from dual")
        self.assertEqual(self.cursor.bindnames(), ["A", "B"])

    def testBadPrepare(self):
        """test that subsequent executes succeed after bad prepare"""
        self.assertRaises(cx_Oracle.DatabaseError,
                self.cursor.execute,
                "begin raise_application_error(-20000, 'this); end;")
        self.cursor.execute("begin null; end;")

    def testBadExecute(self):
        """test that subsequent fetches fail after bad execute"""
        self.assertRaises(cx_Oracle.DatabaseError,
                self.cursor.execute, "select y from dual")
        self.assertRaises(cx_Oracle.InterfaceError,
                self.cursor.fetchall)

    def testScrollAbsoluteExceptionAfter(self):
        """test scrolling absolute yields an exception (after result set)"""
        cursor = self.connection.cursor(scrollable = True)
        cursor.arraysize = self.cursor.arraysize
        cursor.execute("""
                select NumberCol
                from TestNumbers
                order by IntCol""")
        self.assertRaises(cx_Oracle.DatabaseError, cursor.scroll, 12,
                "absolute")

    def testScrollAbsoluteInBuffer(self):
        """test scrolling absolute (when in buffers)"""
        cursor = self.connection.cursor(scrollable = True)
        cursor.arraysize = self.cursor.arraysize
        cursor.execute("""
                select NumberCol
                from TestNumbers
                order by IntCol""")
        cursor.fetchmany()
        self.assertTrue(cursor.arraysize > 1,
                "array size must exceed 1 for this test to work correctly")
        cursor.scroll(1, mode = "absolute")
        row = cursor.fetchone()
        self.assertEqual(row[0], 1.25)
        self.assertEqual(cursor.rowcount, 1)

    def testScrollAbsoluteNotInBuffer(self):
        """test scrolling absolute (when not in buffers)"""
        cursor = self.connection.cursor(scrollable = True)
        cursor.arraysize = self.cursor.arraysize
        cursor.execute("""
                select NumberCol
                from TestNumbers
                order by IntCol""")
        cursor.scroll(6, mode = "absolute")
        row = cursor.fetchone()
        self.assertEqual(row[0], 7.5)
        self.assertEqual(cursor.rowcount, 6)

    def testScrollFirstInBuffer(self):
        """test scrolling to first row in result set (when in buffers)"""
        cursor = self.connection.cursor(scrollable = True)
        cursor.arraysize = self.cursor.arraysize
        cursor.execute("""
                select NumberCol
                from TestNumbers
                order by IntCol""")
        cursor.fetchmany()
        cursor.scroll(mode = "first")
        row = cursor.fetchone()
        self.assertEqual(row[0], 1.25)
        self.assertEqual(cursor.rowcount, 1)

    def testScrollFirstNotInBuffer(self):
        """test scrolling to first row in result set (when not in buffers)"""
        cursor = self.connection.cursor(scrollable = True)
        cursor.arraysize = self.cursor.arraysize
        cursor.execute("""
                select NumberCol
                from TestNumbers
                order by IntCol""")
        cursor.fetchmany()
        cursor.fetchmany()
        cursor.scroll(mode = "first")
        row = cursor.fetchone()
        self.assertEqual(row[0], 1.25)
        self.assertEqual(cursor.rowcount, 1)

    def testScrollLast(self):
        """test scrolling to last row in result set"""
        cursor = self.connection.cursor(scrollable = True)
        cursor.arraysize = self.cursor.arraysize
        cursor.execute("""
                select NumberCol
                from TestNumbers
                order by IntCol""")
        cursor.scroll(mode = "last")
        row = cursor.fetchone()
        self.assertEqual(row[0], 12.5)
        self.assertEqual(cursor.rowcount, 10)

    def testScrollRelativeExceptionAfter(self):
        """test scrolling relative yields an exception (after result set)"""
        cursor = self.connection.cursor(scrollable = True)
        cursor.arraysize = self.cursor.arraysize
        cursor.execute("""
                select NumberCol
                from TestNumbers
                order by IntCol""")
        self.assertRaises(cx_Oracle.DatabaseError, cursor.scroll, 15)

    def testScrollRelativeExceptionBefore(self):
        """test scrolling relative yields an exception (before result set)"""
        cursor = self.connection.cursor(scrollable = True)
        cursor.arraysize = self.cursor.arraysize
        cursor.execute("""
                select NumberCol
                from TestNumbers
                order by IntCol""")
        self.assertRaises(cx_Oracle.DatabaseError, cursor.scroll, -5)

    def testScrollRelativeInBuffer(self):
        """test scrolling relative (when in buffers)"""
        cursor = self.connection.cursor(scrollable = True)
        cursor.arraysize = self.cursor.arraysize
        cursor.execute("""
                select NumberCol
                from TestNumbers
                order by IntCol""")
        cursor.fetchmany()
        self.assertTrue(cursor.arraysize > 1,
                "array size must exceed 1 for this test to work correctly")
        cursor.scroll(2 - cursor.rowcount)
        row = cursor.fetchone()
        self.assertEqual(row[0], 2.5)
        self.assertEqual(cursor.rowcount, 2)

    def testScrollRelativeNotInBuffer(self):
        """test scrolling relative (when not in buffers)"""
        cursor = self.connection.cursor(scrollable = True)
        cursor.arraysize = self.cursor.arraysize
        cursor.execute("""
                select NumberCol
                from TestNumbers
                order by IntCol""")
        cursor.fetchmany()
        cursor.fetchmany()
        self.assertTrue(cursor.arraysize > 1,
                "array size must exceed 2 for this test to work correctly")
        cursor.scroll(3 - cursor.rowcount)
        row = cursor.fetchone()
        self.assertEqual(row[0], 3.75)
        self.assertEqual(cursor.rowcount, 3)

    def testScrollNoRows(self):
        """test scrolling when there are no rows"""
        self.cursor.execute("truncate table TestTempTable")
        cursor = self.connection.cursor(scrollable = True)
        cursor.execute("select * from TestTempTable")
        cursor.scroll(mode = "last")
        self.assertEqual(cursor.fetchall(), [])
        cursor.scroll(mode = "first")
        self.assertEqual(cursor.fetchall(), [])
        self.assertRaises(cx_Oracle.DatabaseError, cursor.scroll, 1,
                mode = "absolute")

    def testScrollDifferingArrayAndFetchSizes(self):
        """test scrolling with differing array sizes and fetch array sizes"""
        self.cursor.execute("truncate table TestTempTable")
        for i in range(30):
            self.cursor.execute("insert into TestTempTable values (:1, null)",
                    (i + 1,))
        for arraySize in range(1, 6):
            cursor = self.connection.cursor(scrollable = True)
            cursor.arraysize = arraySize
            cursor.execute("select IntCol from TestTempTable order by IntCol")
            for numRows in range(1, arraySize + 1):
                cursor.scroll(15, "absolute")
                rows = cursor.fetchmany(numRows)
                self.assertEqual(rows[0][0], 15)
                self.assertEqual(cursor.rowcount, 15 + numRows - 1)
                cursor.scroll(9)
                rows = cursor.fetchmany(numRows)
                numRowsFetched = len(rows)
                self.assertEqual(rows[0][0], 15 + numRows + 8)
                self.assertEqual(cursor.rowcount,
                        15 + numRows + numRowsFetched + 7)
                cursor.scroll(-12)
                rows = cursor.fetchmany(numRows)
                self.assertEqual(rows[0][0], 15 + numRows + numRowsFetched - 5)
                self.assertEqual(cursor.rowcount,
                        15 + numRows + numRowsFetched + numRows - 6)

    def testSetInputSizesMultipleMethod(self):
        """test setting input sizes with both positional and keyword args"""
        self.assertRaises(cx_Oracle.InterfaceError,
                self.cursor.setinputsizes, 5, x = 5)

    def testSetInputSizesByPosition(self):
        """test setting input sizes with positional args"""
        var = self.cursor.var(cx_Oracle.STRING, 100)
        self.cursor.setinputsizes(None, 5, None, 10, None, cx_Oracle.NUMBER)
        self.cursor.execute("""
                begin
                  :1 := :2 || to_char(:3) || :4 || to_char(:5) || to_char(:6);
                end;""", [var, 'test_', 5, '_second_', 3, 7])
        self.assertEqual(var.getvalue(), "test_5_second_37")

