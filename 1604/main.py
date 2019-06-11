import time
rid = 0
cid = 0
class Record():
    __slots__ = ["__author_name", '__text', '__private', '__data', '__comments', '__deleted', '__id']
    def __init__(self, author_name, text, private=False):
        global rid
        self.__author_name = author_name
        self.__text = text
        self.__private = private
        self.__data = time.time()
        self.__comments = []
        self.__deleted = False
        self.__id = rid
        rid += 1

    def save_to_db(self):
        pass

    def print_record(self):
        if self.__deleted == False:
            print(f"{self.__id}: {self.__author_name}:  {self.__text}")

    def update_record(self, text):
        self.__text = text

    def delete_record(self):
        pass

    @property
    def comments(self):
        return self.__comments

    @comments.setter
    def comments(self, new):
        self.__comments.append(new)

    @property
    def id(self):
        return self.__id

class Comment():
    __slots__ = ['__author_name', '__text', '__published', '__rid', '__data', '__reply', '__id']
    def __init__(self, author_name, text, rid, published=False, reply=None):
        global cid
        self.__author_name = author_name
        self.__text = text
        self.__rid = rid
        self.__published = published
        self.__data = time.time()
        self.__reply = reply
        self.__id = cid
        cid += 1

    def save_to_db(self):
        print (__name__)

    def print_commment(self):
        print(f"{self.__id}: {self.__author_name}:  {self.__text}")

    def update_comment(self, text):
        self.__text = text

    def delete_comment(self):
        pass

    @property
    def id(self):
        return self.__id

records = []
#comments = []

run = True

while run:
    try:
        x = input("Введите команду (help): ")
        if x == 'help':
            print("""
Список команд:
allrec - вывод всех записей
recadd( имя автора, текст записи ) - добавление записи
recupd( id записи, новый текст записи ) - обновление записи
comadd( имя автора, текст комментария, id записи ) - добавление комментария
comupd( id коммента, новый текст ) - обновление комментария
reccom( id записи ) - вывод всех комментариев
exit - выход из программы
            """)
        elif x == 'exit':
            run = False
        elif x == 'allrec':
            for record in records:
                record.print_record()
            if records == []:
                print('Список записей пуст')
        elif x[0:6:] == 'recadd':
            if x[6] != '(' or x[len(x)-1] != ')':
                print('Где скобочки?')
            else:
                x1 = x[7::].split(',')
                if len(x1) > 1:
                    records.append(Record(x1[0], x1[1][0:len(x1[1])-1:]))
        elif x[0:6:] == 'recupd':
            if x[6] != '(' or x[len(x)-1] != ')':
                print('Где скобочки?')
            else:
                x1 = x[7::].split(',')
                if len(x1) > 1:
                    for record in records:
                        if record.id == int(x1[0]):
                            record.update_record(x1[1][0:len(x1[1])-1:])
                            record.print_record()
        elif x[0:6:] == 'comadd':
            if x[6] != '(' or x[len(x)-1] != ')':
                print('Где скобочки?')
            else:
                x1 = x[7::].split(',')
                if len(x1) > 1 and len(records)-1 >= int(x1[2][0:len(x1[2])-1:]):
                    #comments.append()
                    records[int(x1[2][0:len(x1[2])-1:])].comments = Comment(x1[0], x1[1], int(x1[2][0:len(x1[2])-1:]))
                else:
                    print('нет такой записи')
        elif x[0:6:] == 'comupd':
            if x[6] != '(' or x[len(x)-1] != ')':
                print('Где скобочки?')
            else:
                x1 = x[7::].split(',')
                if len(x1) > 1:
                    for record in records:
                        for comment in record.comments:
                            if comment.id == int(x1[0]):
                                comment.update_comment(x1[1][0:len(x1[1])-1:])
                                #comments[int(x1[0])].update_comment(x1[1][0:len(x1[1])-1:])
                                comment.print_commment()
        elif x[0:6:] == 'reccom':
            if x[6] != '(' or x[len(x)-1] != ')':
                print('Где скобочки?')
            else:
                x1 = x[7:len(x)-1:]
                if len(x1) > 0:
                    for record in records:
                        if record.id == int(x1):
                            for comment in record.comments:
                                comment.print_commment()
        else:
            print('Неизвестная команда')

    except Exception as e:
        print('Что-то не то: ', e)
