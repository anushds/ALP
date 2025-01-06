from utils.db.sqlite_db import SQLiteDB

class DBSetup:
    CREATE_CHAR_TABLE_QUERY = """
                              CREATE TABLE IF NOT EXISTS char (
                                id INTEGER PRIMARY KEY,
                                name TEXT,
                                UNIQUE(name)
                              );
                              """
    CREATE_EVENT_TABLE_QUERY = """
                               CREATE TABLE IF NOT EXISTS event (
                                 id INTEGER PRIMARY KEY,
                                 name TEXT,
                                 point INTEGER,
                                 UNIQUE(name)
                               );
                               """
    CREATE_MST_DATE_TABLE_QUERY = """
                                    CREATE TABLE IF NOT EXISTS mst_date (
                                        id INTEGER PRIMARY KEY,
                                        date INTEGER,
                                        UNIQUE(date)
                                        );
                                        """
    CREATE_MST_MONTH_TABLE_QUERY = """
                                    CREATE TABLE IF NOT EXISTS mst_month (
                                        id INTEGER PRIMARY KEY,
                                        month INTEGER,
                                        UNIQUE(month)
                                        );
                                        """
    CREATE_MST_YEAR_TABLE_QUERY = """
                                    CREATE TABLE IF NOT EXISTS mst_year (
                                        id INTEGER PRIMARY KEY,
                                        year INTEGER,
                                        UNIQUE(year)
                                        );
                                        """

    CREATE_MST_DATE_TO_EVENT_MAP_TABLE_QUERY = """
                                                  CREATE TABLE IF NOT EXISTS mst_date_to_event_map (
                                                    id INTEGER PRIMARY KEY,
                                                    date_id INTEGER,
                                                    month_id INTEGER,
                                                    year_id INTEGER,
                                                    event_id INTEGER,
                                                    FOREIGN KEY(date_id) REFERENCES mst_date(id),
                                                    FOREIGN KEY(event_id) REFERENCES event(id),
                                                    FOREIGN KEY(month_id) REFERENCES mst_month(id),
                                                    FOREIGN KEY(year_id) REFERENCES mst_year(id),
                                                    UNIQUE(date_id, month_id, year_id, event_id)
                                                  );
                                                  """
    CREATE_LEADERBOARD_TABLE_QUERY = """
                                        CREATE TABLE IF NOT EXISTS leaderboard (
                                            id INTEGER PRIMARY KEY,
                                            char_id INTEGER,
                                            month_id INTEGER,
                                            year_id INTEGER,
                                            score INTEGER,
                                            FOREIGN KEY(char_id) REFERENCES char(id),
                                            FOREIGN KEY(month_id) REFERENCES mst_month(id),
                                            FOREIGN KEY(year_id) REFERENCES mst_year(id),
                                            UNIQUE(char_id, month_id, year_id)
                                            );
                                            """


    def __init__(self):
        self.db = SQLiteDB('ALP_DB')
        self.db.connect()
        self.create_tables()

    def create_tables(self):
        self.db.execute(DBSetup.CREATE_CHAR_TABLE_QUERY)
        self.db.execute(DBSetup.CREATE_EVENT_TABLE_QUERY)
        self.db.execute(DBSetup.CREATE_MST_DATE_TABLE_QUERY)
        self.db.execute(DBSetup.CREATE_MST_MONTH_TABLE_QUERY)
        self.db.execute(DBSetup.CREATE_MST_YEAR_TABLE_QUERY)
        self.db.execute(DBSetup.CREATE_MST_DATE_TO_EVENT_MAP_TABLE_QUERY)
        self.db.execute(DBSetup.CREATE_LEADERBOARD_TABLE_QUERY)
        self.db.commit()

    def populate_tables(self):
        pass

obj = DBSetup()