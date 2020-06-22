import time
import xml.etree.ElementTree as ET
from datetime import datetime
from typing import List


class Languages:

    def __init__(self, languages: List[str] = None):
        self.__root = ET.Element('languages')
        if languages:
            for lang in languages:
                self.add_language(lang)

    def add_language(self, lang: str):
        ET.SubElement(self.__root, 'language').text = lang

    def element(self):
        return self.__root


class PaperInfo:

    def __init__(self, type: str = None, paperID: str = None,
                 callNumber: str = None, title: str = None,
                 titleCollection: str = None, subTitle: str = None,
                 printer: str = None, publisher: str = None,
                 day: str = None, month: str = None, year: str = None,
                 issueNumber: str = None, pages: str = None,
                 yearNumber: str = None, languages: List[str] = None):
        self.__root = ET.Element('paperInfo')
        ET.SubElement(self.__root, 'type').text = type
        ET.SubElement(self.__root, 'paperID').text = paperID
        ET.SubElement(self.__root, 'callNumber').text = callNumber
        ET.SubElement(self.__root, 'title').text = title
        ET.SubElement(self.__root, 'titleCollection').text = titleCollection
        ET.SubElement(self.__root, 'subTitle').text = subTitle
        ET.SubElement(self.__root, 'printer').text = printer
        ET.SubElement(self.__root, 'publisher').text = publisher
        ET.SubElement(self.__root, 'day').text = day
        ET.SubElement(self.__root, 'month').text = month
        ET.SubElement(self.__root, 'year').text = year
        ET.SubElement(self.__root, 'issueNumber').text = issueNumber
        ET.SubElement(self.__root, 'pages').text = pages
        ET.SubElement(self.__root, 'yearNumber').text = yearNumber
        self.__languages = Languages(languages)
        self.__root.append(self.__languages.element())

    def element(self):
        return self.__root


class Document:

    def __init__(self, id: str = None, paperInfo: PaperInfo = None):
        self.__root = ET.Element('document')
        self.__id = ET.SubElement(self.__root, 'id')
        self.set_id(id)
        self.__paper_info = paperInfo if paperInfo else PaperInfo()
        self.__root.append(self.__paper_info.element())

    def set_id(self, id: str):
        self.__id.text = id

    def element(self):
        return self.__root


class Inventory:

    def __init__(self, project: str):
        self.__creation_date = datetime.fromtimestamp(time.time()).strftime("%Y-%m-%dT%H:%M:%SZ")
        self.__project = project
        self.__root = ET.Element('inventory')
        self.__xml = ET.ElementTree(self.__root)
        ET.SubElement(self.__root, 'creationDate').text = self.__creation_date
        ET.SubElement(self.__root, 'project').text = self.__project
        self.__documents = ET.SubElement(self.__root, 'documents')

    def add_document(self, id: str = None, paperInfo: PaperInfo = None):
        doc = Document(id, paperInfo)
        self.__documents.append(doc.element())

    def write(self, filename):
        self.__xml.write(filename)
