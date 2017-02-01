import csv


class Common:
    file_loaded = []

    @classmethod
    def load_file(cls, file_name):
        with open(file_name, 'r') as f:
            data = csv.reader(f, delimiter='\t')
            for row in data:
                cls.file_loaded.append(row)
        cls.file_loaded = cls.file_loaded[1:]
    @staticmethod
    def sort_quick(table, index=0):
        """
        Sorts table. Type index to define key for sorting
        Args:
            table: table to sort
            index: index item in the list on which should be sorted
        Returns:
            Sorted table
        """
        less = []  # less than pivot
        equal = []
        greater = []  # bigger than pivot

        if len(table) > 1:  # When table have more than one element
            pivot = table[0][index]
            for x in table:
                if x[index] < pivot:
                    less.append(x)
                if x[index] == pivot:
                    equal.append(x)
                if x[index] > pivot:
                    greater.append(x)
            # Just use the + operator to join lists
            return Common.sort_quick(less, index) + equal + Common.sort_quick(greater, index)
        else:  # when you only have one element in your table, just return the table.
            return table
