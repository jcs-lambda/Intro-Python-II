import readline

readline.parse_and_bind('tab: complete')

def com(text,state):
    r = ['yep', None]
    return r[state]

readline.set_completer(com)

input('> ')
    