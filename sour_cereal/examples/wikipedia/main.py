'''This example creates a custom connection to Wikipedia used to retrieve its
pages tables in an easy way.'''

import pandas
from sour_cereal import SourceConnection


class WikiTableConnection(SourceConnection):
    def execute_extraction(
        self: 'WikiTableConnection',
        parameters: dict
    ) -> pandas.DataFrame:
        table = pandas.read_html(parameters['url'])[parameters['table_index']]
        table = table.iloc[1:]
        return table


if __name__ == '__main__':
    con = WikiTableConnection()

    parameters = {
        'gdps': {
            'url': 'https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(' +
            'nominal)',
            'table_index': 7

        },
        'companies': {
            'url': 'https://en.wikipedia.org/wiki/List_of_largest_companies_' +
            'by_revenue',
            'table_index': 0
        }
    }

    extractions = {
        tag: con.new_extraction(parameters=parameters[tag])
        for tag in parameters
    }

    results = {
        tag: extractions[tag].execute()
        for tag in parameters
    }

    for tag, result in results.items():
        print(tag + ':' + '\n---------------------------------------\n')
        print(result)
        print('\n')
