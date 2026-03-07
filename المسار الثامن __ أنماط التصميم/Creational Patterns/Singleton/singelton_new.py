class DBConnection:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            print("New Instance Created")
        else:
            print("Existing Instance Returned")

        return cls.__instance


if __name__ == "__main__":
    dbCon1 = DBConnection()
    print('Writing Query')
    dbCon2 = DBConnection()
    print('Query 2 Writing')

    print(dbCon1)
    print(dbCon2)
    print(dbCon1 is dbCon2)