# Lukewarmcat's Module Importer
import importlib;
modules = ["termcolorz"]

for x in modules:
        vars()[x] = importlib.import_module(f'.{x}', package='lib')

def rainbow(txt):
        rainbow = ['red', 'yellow', 'green', 'blue', 'magenta']
        rainbowArray = []
        arrayCounter = 0;
        text = txt
        text = list(text)

        for y in text:
                if arrayCounter > len(rainbow)-1:
                        arrayCounter = 0;

                rainbowArray.append(termcolorz.colored(y, rainbow[arrayCounter]))
                arrayCounter += 1

        return ''.join(rainbowArray);

if __name__ == "__main__":
    import sys
    sys.argv[0] = "";
    print(rainbow(' '.join(sys.argv).strip()))
