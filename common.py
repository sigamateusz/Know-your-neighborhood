import csv


class Common:

    @staticmethod
    def load_file(file_name):
        read = []
        with open(file_name, 'r') as f:
            data = csv.reader(f, delimiter='\t')
            for row in data:
                read.append(row)
        return read
