# Итератор для удаления дубликатов
class Unique(object):
    def __init__(self, items, **kwargs):
        # Нужно реализовать конструктор
        # В качестве ключевого аргумента, конструктор должен принимать bool-параметр ignore_case,
        # в зависимости от значения которого будут считаться одинаковые строки в разном регистре
        # Например: ignore_case = True, Aбв и АБВ разные строки
        #           ignore_case = False, Aбв и АБВ одинаковые строки, одна из них удалится
        # По-умолчанию ignore_case = False
        if (type(items))==list:
            self.items=iter(items)
        else:
             self.items=items
        self.index=0
        self.ignore_case=kwargs.get('ignore_case',False)
        self.was=[]
    def __next__(self):
        # Нужно реализовать __next__
        for i in self.items:
            if (self.ignore_case==True and type(i)==str):
                if (self.was.count(i.lower())==0):
                    self.was.append(i.lower())
                    return i
                else:
                    continue
            else:
                if (self.was.count(i)==0):
                    self.was.append(i)
                    return i
                else:
                    continue
        raise StopIteration
    def __iter__(self):
        return self
