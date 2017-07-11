#------------------------------------------------------------------------------
# Copyright 2016, 2017, Oracle and/or its affiliates. All rights reserved.
#
# Portions Copyright 2007-2015, Anthony Tuininga. All rights reserved.
#
# Portions Copyright 2001-2007, Computronix (Canada) Ltd., Edmonton, Alberta,
# Canada. All rights reserved.
#------------------------------------------------------------------------------

"""Module for testing long and long raw variables."""

class TestLongVar(BaseTestCase):

    def __PerformTest(self, a_Type, a_InputType):
        self.cursor.execute(u"truncate table Test%ss" % a_Type)
        if a_InputType == cx_Oracle.LONG_STRING:
            longString = u""
        else:
            longString = ""
        for i in range(1, 11):
            if a_InputType == cx_Oracle.LONG_STRING:
                char = unichr(ord('A') + i - 1)
            else:
                char = chr(ord('A') + i - 1)
            longString += char * 25000
            self.cursor.setinputsizes(longString = a_InputType)
            self.cursor.execute(u"""
                    insert into Test%ss (
                      IntCol,
                      %sCol
                    ) values (
                      :integerValue,
                      :longString
                    )""" % (a_Type, a_Type),
                    integerValue = i,
                    longString = longString)
        self.connection.commit()
        self.cursor.execute(u"""
                select *
                from Test%ss
                order by IntCol""" % a_Type)
        longString = ""
        while 1:
            row = self.cursor.fetchone()
            if row is None:
                break
            integerValue, fetchedValue = row
            char = unichr(ord('A') + integerValue - 1)
            longString += char * 25000
            self.assertEqual(len(fetchedValue), integerValue * 25000)
            self.assertEqual(fetchedValue, longString)

    def testLongs(self):
        "test binding and fetching long data"
        self.__PerformTest("Long", cx_Oracle.LONG_STRING)

    def testLongRaws(self):
        "test binding and fetching long raw data"
        self.__PerformTest("LongRaw", cx_Oracle.LONG_BINARY)

    def testLongCursorDescription(self):
        "test cursor description is accurate for longs"
        self.cursor.execute(u"select * from TestLongs")
        self.assertEqual(self.cursor.description,
                [ (u'INTCOL', cx_Oracle.NUMBER, 10, None, 9, 0, 0),
                  (u'LONGCOL', cx_Oracle.LONG_STRING, None, None, None, None,
                        0) ])

    def testLongRawCursorDescription(self):
        "test cursor description is accurate for long raws"
        self.cursor.execute(u"select * from TestLongRaws")
        self.assertEqual(self.cursor.description,
                [ (u'INTCOL', cx_Oracle.NUMBER, 10, None, 9, 0, 0),
                  (u'LONGRAWCOL', cx_Oracle.LONG_BINARY, None, None, None,
                        None, 0) ])

    def testArraySizeTooLarge(self):
        "test array size too large generates an exception"
        self.cursor.arraysize = 268435456
        self.assertRaises(cx_Oracle.DatabaseError, self.cursor.execute,
                u"select * from TestLongRaws")

