import os
from voivodeship import Voivodeship


class Menu:
    @classmethod
    def run(cls):
        voivodeship = Voivodeship.create_voivodeship()
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
            input('Press ENTER')
        elif choice == '2':
            cls.longest_names(voivodeship)
            input('Press ENTER')
        elif choice == '3':
            cls.max_communities(voivodeship)
            input('Press ENTER')

        elif choice == '4':
            cls.more_category(voivodeship)
            input('Press ENTER')

        elif choice == '5':
            Menu.advanced_search(voivodeship)
            input('Press ENTER')
        elif choice == '0':
            exit()

    @staticmethod
    def advanced_search(voivodeship):
        titles = ['LOCATION', 'TYPE']
        user_input = input('Searching for: ')
        full_list = Menu.list_of_all_objects(voivodeship)
        output_list = []
        for location in full_list:
            if user_input in str(location.get_name()):
                output_list.append([location.get_name(), location.get_kind()])
        print('\nFound {} location(s):\n'.format(len(output_list)))
        Menu.print_table(output_list, titles)

    @staticmethod
    def list_of_all(voivodeship):
        """
        Creates list with strings of all locations
        :param voivodeship: Voivodeship object
        :return: None
        """
        full_list = []

        for county in voivodeship.counties:
            full_list.append(county.get_name())
            for municipality in county.municipality:
                full_list.append(municipality.get_name())
            for towns_with_district_rights in county.town_with_district_rights:
                full_list.append(towns_with_district_rights.get_name())
            for rural_area in county.rural_area:
                full_list.append(rural_area.get_name())
            for rural_commune in county.rural_commune:
                full_list.append(rural_commune.get_name())
            for urban_rural_commune in county.urban_rural_commune:
                full_list.append(urban_rural_commune.get_name())
            for cities in county.cities:
                full_list.append(cities.get_name())
            for delegacy in county.delegacy:
                full_list.append(delegacy.get_name())

        for town in voivodeship.towns_with_district_rights:
            full_list.append(town.get_name())
            for municipality in town.municipality:
                full_list.append(municipality.get_name())
            for towns_with_district_rights in town.town_with_district_rights:
                full_list.append(towns_with_district_rights.get_name())
            for rural_area in town.rural_area:
                full_list.append(rural_area.get_name())
            for rural_commune in town.rural_commune:
                full_list.append(rural_commune.get_name())
            for urban_rural_commune in town.urban_rural_commune:
                full_list.append(urban_rural_commune.get_name())
            for cities in town.cities:
                full_list.append(cities.get_name())
            for delegacy in town.delegacy:
                full_list.append(delegacy.get_name())

        return full_list

    @staticmethod
    def list_of_all_objects(voivodeship):
        """
        Creates list with strings of all locations
        :param voivodeship: Voivodeship object
        :return: None
        """
        full_list = []

        for county in voivodeship.counties:
            full_list.append(county)
            for municipality in county.municipality:
                full_list.append(municipality)
            for towns_with_district_rights in county.town_with_district_rights:
                full_list.append(towns_with_district_rights)
            for rural_area in county.rural_area:
                full_list.append(rural_area)
            for rural_commune in county.rural_commune:
                full_list.append(rural_commune)
            for urban_rural_commune in county.urban_rural_commune:
                full_list.append(urban_rural_commune)
            for cities in county.cities:
                full_list.append(cities)
            for delegacy in county.delegacy:
                full_list.append(delegacy)

        for town in voivodeship.towns_with_district_rights:
            full_list.append(town)
            for municipality in town.municipality:
                full_list.append(municipality)
            for towns_with_district_rights in town.town_with_district_rights:
                full_list.append(towns_with_district_rights)
            for rural_area in town.rural_area:
                full_list.append(rural_area)
            for rural_commune in town.rural_commune:
                full_list.append(rural_commune)
            for urban_rural_commune in town.urban_rural_commune:
                full_list.append(urban_rural_commune)
            for cities in town.cities:
                full_list.append(cities)
            for delegacy in town.delegacy:
                full_list.append(delegacy)

        return full_list

    @staticmethod
    def more_category(voivodeship):
        """
        Displays locations, that belong to more than one category
        :param voivodeship: Voivodeship object
        :return: None
        """
        repeated = []
        full_list = Menu.list_of_all(voivodeship)
        while len(full_list) > 1:
            location = full_list.pop(0)
            if location in full_list:
                repeated.append(location)

        repeated = set(repeated)
        repeated = list(repeated)
        repeated.sort()
        for location in repeated:
            print(':::{:^25}:::'.format(location))

    @staticmethod
    def max_communities(voivodeship):
        """
        Prints county with maximal number of communities
        :param voivodeship: Voivodeship object
        :return: None
        """
        maximal = ['random', 0]

        for county in voivodeship.counties:
            local_max = 0
            local_max += len(county.municipality)
            local_max += len(county.rural_commune)
            local_max += len(county.urban_rural_commune)
            # local_max += len(county.town_with_district_rights)
            if local_max > maximal[1]:
                maximal = [county.get_name(), local_max]

        output_string = '\n...:::County {} have : {} communities:::...\n'.format(maximal[0], maximal[1])

        print(output_string)

    @staticmethod
    def longest_names(voivodeship):
        """
        Prints 3 cities with largest names
        :param voivodeship: Voivodeship object
        :return: None
        """
        length_name = 0
        longest_cities = []
        for county in voivodeship.counties:
            for city in county.cities:
                if len(city.get_name()) > length_name:
                    length_name = len(city.get_name())

        for town in voivodeship.towns_with_district_rights:
            for city in town.cities:
                if len(city.get_name()) > length_name:
                    length_name = len(city.get_name())

        while len(longest_cities) < 3:
            for county in voivodeship.counties:
                for city in county.cities:
                    if len(city.get_name()) == length_name:
                        longest_cities.append(city.get_name())
            for town in voivodeship.towns_with_district_rights:
                for city in town.cities:
                    if len(city.get_name()) == length_name:
                        longest_cities.append(city.get_name())
            length_name -= 1

        output_string = '\n...:::{} -- {} characters:::...\n' \
                        '...:::{} -- {} characters:::...\n' \
                        '...:::{} -- {} characters:::...\n'.format(longest_cities[0], len(longest_cities[0]),
                                                                   longest_cities[1], len(longest_cities[1]),
                                                                   longest_cities[2], len(longest_cities[2]))
        print(output_string)

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

    @staticmethod
    def statistics(voivodeship):
        """
        Counts and displays statistics
        :param voivodeship: Voivodeship object
        :return: None
        """
        titles = ['', voivodeship.get_name()]
        statistics = [[1, 'wojewódźtwo'], [int(len(voivodeship.counties)), 'powiaty']]

        town_with_district_rights = len(voivodeship.towns_with_district_rights)
        calculations = {'municipality': 0, 'rural_area': 0, 'rural_commune': 0,
                        'urban_rural_commune': 0, 'cities': 0, 'delegacy': 0}

        for county in voivodeship.counties:
            Menu.calculating_statistics(county, calculations)
        for town in voivodeship.towns_with_district_rights:
            Menu.calculating_statistics(town, calculations)

        Menu.connect_stats(statistics, calculations, town_with_district_rights)
        Menu.print_table(statistics, titles)

    @staticmethod
    def connect_stats(statistics, calculations, town_with_district_rights):
        """
        It combines all the statistics in one list
        :param statistics: list
        :param calculations: dict
        :param town_with_district_rights: int
        :return: None
        """
        statistics.append([calculations['municipality'], 'gmina miejska'])
        statistics.append([calculations['rural_commune'], 'wiejska'])
        statistics.append([calculations['urban_rural_commune'], 'gmina miejsko - wiejska'])
        statistics.append([calculations['rural_area'], 'obszar wiejski'])
        statistics.append([calculations['cities'], 'miasto'])
        statistics.append([town_with_district_rights, 'miasto na prawach powiatu'])
        statistics.append([calculations['delegacy'], 'delegatura'])

    @staticmethod
    def calculating_statistics(county, calculations):
        """
        Added together statistics
        :param county: County object
        :param calculations: dict
        :return: None
        """
        calculations['municipality'] += int(len(county.municipality))
        calculations['rural_area'] += int(len(county.rural_area))
        calculations['rural_commune'] += int(len(county.rural_commune))
        calculations['urban_rural_commune'] += int(len(county.urban_rural_commune))
        calculations['cities'] += int(len(county.cities))
        calculations['delegacy'] += int(len(county.delegacy))

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
