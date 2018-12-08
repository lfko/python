'''
Created on Dec 3, 2018

@author: Florian Becker (s76343)

    purposed main entry class of the application

'''


def app_as_gui():
    """ 
        load the application with the tkinter gui
    """


def app_as_cli():
    """ 
        load the application on the cli
    """
    #import lfko.python.languaid.core.lang.verb.Verb as vb
    #import lfko.python.languaid.core.lang.translate as tr
    menuItems = [('translate a word', __translate__),
                 ('check a word', __check__)]

    # load a welcome message and the options menu
    welcome_txt = open('../res/welcome-txt.txt', 'r')
    print(welcome_txt.read())
    for i, item in enumerate(menuItems):
        print('>> (' + str(i) + ')', item[0])

    choice = input('>> ')

    try:
        if int(choice) < 0:
            raise ValueError(' wrong choice! ')

        # execute the selected menu entry - we read the function pointer, add
        # '()' and thus, it is an executable function call
        menuItems[int(choice)][1]()
    except(ValueError, IndexError):
        pass


def __translate__():
    """ """
    import lfko.python.languaid.core.lang.translate as tr

    print('translate called')

    while(True):
        word = input(
            '>> enter a word to translate (or "menu" to get back to the main menu) ').strip()

        if word == 'menu':
            break

        source = input('source language?').strip()
        target = input('target language?').strip()

        print('summary: {}, from {} to {}'.format(word, source, target))
        print('translation: ', tr.translate(word, source, target))

    # called if while() was broken
    app_as_cli()


def __check__():
    pass


if __name__ == '__main__':
    # app_as_gui()
    app_as_cli()
