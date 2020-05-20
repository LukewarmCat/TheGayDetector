from distutils.util import strtobool

def q(question):
        x = f'{question} [y/n]'
        print(x)
        while True:
                try:
                        return strtobool(input().lower())
                except ValueError:
                        print(x)
