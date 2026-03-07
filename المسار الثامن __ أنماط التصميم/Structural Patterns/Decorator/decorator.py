from abc import ABC, abstractmethod



class DataSource(ABC):
    @abstractmethod
    def write_data(self, data):
        pass

    @abstractmethod
    def read_data(self):
        pass

class FileDataSource(DataSource):
    def __init__(self, filename):
        self._filename = filename

    def write_data(self, data):
        print("Write \"", data, "\" to the file using FileDataSource")

    def read_data(self):
        print("Read data from the file using FileDataSource")
        return "data"

class DataSourceDecorator(DataSource):
    def __init__(self, source: DataSource):
        self.__wr = source

    def write_data(self, data):
        self.__wr.write_data(data)

    def read_data(self):
        return self.__wr.read_data()

class EncryptionDecorator(DataSourceDecorator):
    def __init__(self, source: DataSource):
        super().__init__(source)

    def write_data(self, data):
        print("Encrypt passed data using EncryptionDecorator")
        super().write_data(data)

    def read_data(self):
        result = super().read_data()
        print("Decryption Data using EncryptionDecorator")
        return result

class CompressionDecorator(DataSourceDecorator):
    def __init__(self, source: DataSource):
        super().__init__(source)

    def write_data(self, data):
        print("Compress data")
        super().write_data(data)

    def read_data(self):
        print("deCompress data")
        return super().read_data()

class Application:
    @staticmethod
    def usage_example():
        salary_record = "Salary is 123$"
        source = FileDataSource("somefile.dat")
        source.write_data(salary_record)

        source = CompressionDecorator(source)
        source.write_data(salary_record)

        source = EncryptionDecorator(source)
        source.write_data(salary_record)


if __name__ == "__main__":
    Application.usage_example()