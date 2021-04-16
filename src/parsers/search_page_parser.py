from dataclasses import dataclass
from typing import Dict

from lxml import html, etree
import requests

from src.parsers.parser import Parser
from src.parsers.teacher_page_parser import TeacherPageParser
from src.users.teacher import Teacher


@dataclass()
class SearchPageParser(Parser):

    def _open_file(self, path: str, params: Dict[str, str]) -> 'file':
        re = requests.post(f'{path}', data=params)
        return re

    def _extract_data(self, file):
        return file.content

    def _parse_data(self, raw_data) -> []:
        data = []
        tree = html.fromstring(raw_data)
        get_url = etree.XPath('@href')
        get_title = etree.XPath('text()')
        teachers_info = tree.xpath('//a[starts-with(@class, "s")]')
        teachers_info = zip(teachers_info[::2], teachers_info[1::2])
        for teacher in teachers_info:
            name = get_title(teacher[0])[0]
            url = f'http://www.osu.ru{get_url(teacher[0])[0]}'
            cathedra = get_title(teacher[1])[0]

            teacher_parser = TeacherPageParser()
            url = teacher_parser.parse(url, {})

            data.append(Teacher(url, name, cathedra))
        return data
