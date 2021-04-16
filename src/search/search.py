from dataclasses import dataclass
from src.parsers.search_page_parser import SearchPageParser


@dataclass()
class Search:
    __teachers_location_url: str = 'http://www.osu.ru/doc/1034'

    def teachers_by_name(self, name='', surname='', patronymic=''):
        # На сайте ОГУ используется KOI8-R, поэтому перед POST запросом меняем кодировку
        param = {
            'v_ps': 'prepod',
            'family': f'{surname}'.encode("koi8-r"),
            'name': f'{name}'.encode("koi8-r"),
            'otch': f'{patronymic}'.encode("koi8-r")
        }
        parser = SearchPageParser()
        teachers = parser.parse(self.__teachers_location_url, param)
        return teachers
