# 1. Реализовать класс Stack
class Stack:
    def __init__(self):
        self.items = []


    def isEmpty(self):
        """
        проверка стека на пустоту.
        :return: True или False
        """
        return self.items == []


    def push(self, item):
        """
        добавляет новый элемент на вершину стека.
        :return: None
        """
        self.items.append(item)

    def pop(self):
        """
        удаляет верхний элемент стека. Стек изменяется.
        :return: верхний элемент стэка
        """
        return self.items.pop()

    def peek(self):
        """
         возвращает верхний элемент стека, но не удаляет его. Стек не меняется.
        :return: верхний элемент стэка
        """
        return self.items[len(self.items) - 1]

    def size(self):
        """
        :return: возвращает количество элементов в стеке.
        """
        return len(self.items)


# 2. Используя стек из задания 1 необходимо решить задачу на проверку сбалансированности скобок. \
#     Сбалансированность скобок означает, что каждый открывающий символ имеет соответствующий ему закрывающий,\
#     и пары скобок правильно вложены друг в друга.
def balance(text):
    """
    Сбалансированность скобок на инпуте
    :param text: набор скобок
    :return: Текст - сбалансированно или не сбалансированно
    """
    barrel = Stack()
    balanced = True
    open_error = False
    count = 0
    while count < len(text) and balanced:
        item = text[count]
        if item == '(':
            barrel.push(item)
        elif item == '[':
            barrel.push(item)
        elif item == '{':
            barrel.push(item)
        else:
            if count > 0:
                if barrel.isEmpty():
                    balanced = False
                else:
                    barrel.pop()
            else:
                open_error = True
                balanced = False
                # print('Не сбалансировано')
        count = count + 1
    if balanced and barrel.isEmpty():
        print('Сбалансировано')
    elif open_error:
        print('Не сбалансировано')
    else:
        print('Не сбалансировано')


if __name__ == '__main__':
    balance('}{}')