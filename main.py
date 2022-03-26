#Parsing f1-news.ru

import parser_class

parser = parser_class.Parser(
    'https://www.f1news.ru/', 'f1news'
)

parser.run()



