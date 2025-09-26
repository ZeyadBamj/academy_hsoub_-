
class Model:
    db = None
    connection = None

    def __init__(self):
        self._create_table()
        self._save = False


    @classmethod
    def _get_table_name(cls):
        return cls.__name__.lower()

    @classmethod
    def get_columns(cls):
        columns = {}
        for key, value in cls.__dict__.items():
            if str(key).startswith('_'):
                continue
            columns[str(key)] = str(value)
        return columns


    def _create_table(self):
        columns = ', '.join(' '.join((key, value)) for (key, value) in self.get_columns().items())
        sql = f"create table if not exists {self._get_table_name()} (id integer primary key autoincrement, {columns})"
        cursor = self.connection.cursor()
        result = cursor.execute(sql)
        return result