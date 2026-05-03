import psycopg2
from psycopg2 import OperationalError
from django.conf import settings

class DatabBaseConnection:
    
    def __init__(self):
        self.connection = None
        self.cursor = None

    def get_connection(self):
        
        try:
            if self.connection:
                return self.connection
            else:
                incoming_settings = settings.DATABASES.get('default')
                if not incoming_settings:
                    print("PostgreSQL database settings not found.")
                    return None
                else:
                    self.connection = psycopg2.connect(
                        host=incoming_settings['HOST'],
                        port=incoming_settings['PORT'],
                        database=incoming_settings['NAME'],
                        user=incoming_settings['USER'],
                        password=incoming_settings['PASSWORD'],
                    )
        
            #asigna una referencia al cursor para ejecutar consultas
            self.cursor = self.connection.cursor()
    
        except OperationalError as e:
            print(f"Database connection error: {e}")
            
    def fetchall(self, query):
        if self.cursor:
            try:
                self.cursor.execute(query)
                return self.cursor.fetchall()
            except Exception as e:
                print(f"Error executing query: {e}")
                return None
        else:
            print("No database connection.")
            return None
            
    def close_connection(self):
        
        if self.cursor:
            self.cursor.close()
            
        if self.connection:
            self.connection.close()
            
    def check_connection(self):
        try:
            if self.connection:
                print("Database connection is active.")
                return True
        except Exception as e:
            print(f"Database connection check failed: {e}")
            return False