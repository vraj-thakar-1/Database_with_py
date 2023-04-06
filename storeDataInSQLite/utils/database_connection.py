# this file is works as a contrtext manager o our application
# it's like to open the file in pythonic way
import sqlite3


class DatabaseConnection:
    def __init__(self, host):
        self.connection = None
        self.host = host

    def __enter__(self) -> sqlite3.Connection:
        self.connection = sqlite3.connect(self.host)
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        # error happened then value changes from None to something in following values
        if exc_type or exc_val or exc_tb:
            print("Invalid inputs")
            self.connection.close()
            exit()
        else:
            self.connection.commit()
            self.connection.close()
