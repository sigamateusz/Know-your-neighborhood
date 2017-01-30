import csv


class Common:
    file_loaded = []

    @classmethod
    def load_file(cls, file_name):
        with open(file_name, 'r') as f:
            data = csv.reader(f, delimiter='\t')
            for row in data:
                cls.file_loaded.append(row)
