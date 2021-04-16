from dataclasses import dataclass
from typing import Dict
from lxml import html, etree

from src.parsers.parser import Parser

import requests


@dataclass()
class TeacherPageParser(Parser):

    def _open_file(self, path: str, params: Dict[str, str]) -> 'file':
        re = requests.get(f'{path}')
        return re

    def _extract_data(self, file):
        return file.content

    def _parse_data(self, raw_data) -> []:
        tree = html.fromstring(raw_data)
        get_url = etree.XPath('@href')
        teachers_info = tree.xpath('//a[contains(text(), "Расписание преподавателя")]')[0]
        return get_url(teachers_info)[0]
