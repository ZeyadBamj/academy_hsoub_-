class DBConnection:
    __instance = None

    @staticmethod
    def get_instance():
        if DBConnection.__instance is None:
            DBConnection.__instance = DBConnection()
            print('New Instance has Created')
        else:
            print('Existed Instance')

        return DBConnection.__instance

    def query(self):
        pass


if __name__ == "__main__":
    dbCon1 = DBConnection()
    print('Writing Query')
    dbCon2 = DBConnection()
    print('Query 2 Writing')
    dbCon2.get_instance()

    print(dbCon1)
    print(dbCon2)
    print(dbCon1 is dbCon2)