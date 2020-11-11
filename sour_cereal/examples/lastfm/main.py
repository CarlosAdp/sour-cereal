'''This example shows how an AuthSourceConnection should work.'''
from pprint import pprint

import requests

from sour_cereal import AuthSourceConnection


class LastFMAlbumGetterConnection(AuthSourceConnection):
    BASE_URL = 'http://ws.audioscrobbler.com/2.0/'

    QUERY_PROTOTYPE = {
        'method': 'album.getinfo',
        'format': 'json',
        'api_key': None,
        'artist': None,
        'album': None,
    }

    def execute_extraction(
        self: 'LastFMAlbumGetterConnection',
        parameters: dict
    ) -> dict:
        query = self.QUERY_PROTOTYPE.copy()
        query.update({
            'api_key': self._credentials,
            'artist': parameters['artist'],
            'album': parameters['album']
        })

        response = requests.get(
            url=self.BASE_URL,
            params=query
        )

        return response.json()


if __name__ == '__main__':
    api_key = input("Please insert your LastFM API Key: ")
    con = LastFMAlbumGetterConnection(credentials=api_key)

    parameters_list = [
        {'artist': 'Judas Priest', 'album': 'Painkiller'},
        {'artist': 'Lady Gaga', 'album': 'Chromatica'},
        {'artist': 'Banda Calypso', 'album': 'Calypso Pelo Brasil'}
    ]

    extractions = [
        con.new_extraction(parameters=parameters)
        for parameters in parameters_list
    ]

    albuns_infos = [
        extraction.execute() for extraction in extractions
    ]

    pprint(albuns_infos)
