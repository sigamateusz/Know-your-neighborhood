import os
from voivodeship import Voivodeship


class Menu:
    @classmethod
    def run(cls):
        voivodeship = Voivodeship.create_voivodeship()
        for county in voivodeship.counties:
            print(county.name)
        input()
        while True:

            os.system('clear')
            options = 'What would you like to do:\n' \
                      '\t(1) List statistics\n' \
                      '\t(2) Display 3 cities with longest names\n' \
                      '\t(3) Display county\'s name with the largest number of communities\n' \
                      '\t(4) Display locations, that belong to more than one category\n' \
                      '\t(5) Advanced search\n' \
                      '\t(0) Exit program\n'

            user_choice = cls.get_menu(options, 0, 5)

            cls.choose_option(user_choice, voivodeship)

    @staticmethod
    def get_menu(menu, menu_from, menu_to):
        """
        printing menu from menu, menu from option to option
        :param menu:
        :param menu_from:
        :param menu_to:
        :return option:
        """
        while True:
            print(menu)
            try:

                option = input("Option: ")
                if menu_from > int(option) or int(option) > menu_to:
                    raise NameError('None option')
                else:
                    break
            except:
                print('Wrong select!')

        return option

    @classmethod
    def choose_option(cls, choice, voivodeship):
        """
        Checks which option was selected by user and run assigned method
        :param choice: string ( user input)
        :param voivodeship: Voivodeship object
        :return: None
        """
        if choice == '1':
            cls.statistics(voivodeship)
            input()
        elif choice == '2':
            pass

        elif choice == '3':
            pass

        elif choice == '4':
            pass

        elif choice == '5':
            pass

        elif choice == '0':
            exit()

    @staticmethod
    def statistics(voivodeship):
        titles = ['', voivodeship.get_name()]
        statistics = [['1', 'wojewódźtwo']]
        statistics.append([int(len(voivodeship.counties)), 'powiaty'])
        # if len(voivodeship.counties)
        # Menu.print_table([['d', 'd'], ['d','d'], ['sdsadsadasd','d'], ['d','d2e22eeqwdwadadssaadsdaadw']],titles)
        Menu.print_table(statistics, titles)

    @staticmethod
    def print_table(table, title_list):
        """
               Displays table

               Args:
                   table(list): table to print
                   title_list(list): headers for table
                Returns:
                   This function doesn't return anything it only prints to console.
        """

        # checking largest cells
        table_size = Menu.count_table_size(table, title_list)
        cell_size = table_size[1]
        table_size = table_size[0]

        print(' /' + '-' * (table_size-2) + '\\')

        for i, title in enumerate(title_list):
            if i == 0:
                print(' |', end="")
            print(' {:{width}} |'.format(title, width=cell_size[i]), end="")
        print()

        for items in table:
            print(' |' + '-' * (cell_size[0]+2) + '+' + '-' * (cell_size[1]+2) + '|')
            # print(' |' + '-' * (table_size-2) + '|')
            for i, item in enumerate(items):
                if i == 0:
                    print(' |', end="")
                print(' {:{width}} |'.format(str(item), width=cell_size[i]), end="")
            print()
        print(' \\' + '-' * (table_size-2) + '/')
        print()

    @staticmethod
    def count_table_size(table, title_list):
        """counting table size, this method use only method print_table"""

        cell_size = []

        for i, title in enumerate(title_list):
            cell_size.append(len(title))

        for items in table:
            for i, item in enumerate(items):
                try:
                    if cell_size[i] < len(str(item)):
                        cell_size[i] = len(str(item))
                except:
                    cell_size.append(len(item))

        # how big table
        table_size = 1
        for dash in cell_size:
            table_size += (dash + 3)

        return table_size, cell_size
