'''import climage module to display images on terminal'''
# -*- coding: latin-1 -*-
from climage import convert


def main():
    '''Take in PNG and output as ANSI to terminal'''
    output = convert('linky.png', is_unicode=True)
    print(output)

if __name__ == "__main__":
    main()
