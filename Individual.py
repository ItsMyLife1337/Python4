# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Напишите рекурсивную функцию, проверяющую правильность расстановки скобок в строке.
При правильной расстановке выполняются условия:
количество открывающих и закрывающих скобок равно;
внутри любой пары открывающая – соответствующая закрывающая скобка =>
=> скобки расставлены правильно.
"""


def brackets_check(s, meetings=0):
    if meetings < 0:
        return False
    if s:
        if s[0] == '(':
            meetings += 1
        elif s[0] == ')':
            meetings -= 1
        return brackets_check(s[1:], meetings)
    return meetings == 0


if __name__ == '__main__':
    if brackets_check(input('Введите строку: ')):
        print('Скобки расставлены правильно.')
    else:
        print('Неправильная расстановка!')
