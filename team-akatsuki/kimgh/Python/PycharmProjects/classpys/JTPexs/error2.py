class Error(Exception):
    def __str__(self):
        return "에헤이"

def say_nick(nick):
    if nick == '밥보':
        raise Error()
    print(nick)


try:
    say_nick("바보바보")
    say_nick("밥보")
except Error as e:
    print(e)