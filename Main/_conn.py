# This file is provided for connecting and operations with databases.
import cx_Oracle


# This class is responsible for providing the basic connecting and other database operations.
class Connect:

    gl_conn = None
    gl_cursor = None

    def __init__(self, user, password, ip, port, service):
        self._user = user
        self._password = password
        self._ip = ip
        self._port = port
        self._service = service
        self._connect_f()
        pass

    # ******************************************************************
    #   connection
    # ******************************************************************

    # This method is responsible for connecting to the database.
    def _connect_f(self):
        self.gl_conn = cx_Oracle.connect(self._user, self._password, cx_Oracle.makedsn(
            self._ip, self._port, self._service))
        pass

    # This method is responsible for disconnecting from the database.
    def _disConnect_f(self):
        self.gl_conn.close()
        pass

    # This method is responsible for running sql sentences.
    def _sql_f(self, _input):

        self.gl_cursor = self.gl_conn.cursor()
        sql = str(_input)
        self.gl_cursor.execute(sql)
        self.gl_conn.commit()
        row = self.gl_cursor.fetchall()
        for x in row:
            print(x)
        self.gl_conn.commit()
        self.gl_cursor.close()
        return row
