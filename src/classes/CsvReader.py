import csv


class CsvReader():
    CSV_EXTENSION = "csv"

    def get_file_extension(file_name):
        return file_name.split(".")[-1].lower()

    @classmethod
    def read_file(cls, file_name):
        file_extension = cls.get_file_extension(file_name)
        if file_extension != cls.CSV_EXTENSION:
            raise FileNotFoundError(f"Extensão inválida: '{file_name}'")

        try:
            with open(file_name) as file:
                file_data = csv.DictReader(
                    file,
                    delimiter=",",
                    quotechar='"',
                    fieldnames=['name', 'dish', 'day']
                )
                return list(file_data)
        except FileNotFoundError:
            raise FileNotFoundError(f"Arquivo inexistente: '{file_name}'")
