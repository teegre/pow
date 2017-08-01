#! /usr/bin/env python
import traceback
import readline
import powast
from exceptions import *
from powrser import parser

def main():
    noeval = False
    tb = False
    trace = False
    while True:
        try:
            stop = False
            parser.lineno = 1
            s = input('[→] ')
            if s == 'noeval':
                noeval = not noeval
                print('noeval:', powast.Bool(noeval))
                continue
            elif s == 'traceback':
                tb = not tb
                print('traceback:', powast.Bool(tb))
                continue
            elif not s:
                continue
            if s.endswith(':'):
                while True:
                    try:
                        m = input('... ')
                        if not m: break
                        else: s += m + '\n'
                    except KeyboardInterrupt:
                        print()
                        stop = True
                        break
                    except EOFError:
                        print()
                        continue
            if stop: continue
            else: s += '\n'
        except EOFError:
            print()
            break
        except KeyboardInterrupt:
            print()
            continue
        if not s: continue
        try:
            result = None
            instructions = parser.parse(s)
            if instructions is not None and not noeval:
                result = instructions.eval()
                if result is not None and not isinstance(result, powast.Exit):
                    for r in result:
                        if r is not None: print(powast.ttype(r))
            elif instructions is not None:
                for instruction in instructions:
                    print(instruction)
        except Exception as e:
            print(e)
            if tb: traceback.print_exc()
            parser.restart()
    return 1

if __name__ == '__main__':
    readline.parse_and_bind('"[" "\C-v[]\e[D"')
    readline.parse_and_bind('"(" "\C-v()\e[D"')
    readline.parse_and_bind('":" "\C-v:\C-d\e[D\C-f"')
    from time import sleep
    print(); sleep(0.0625)
    print('█████████████ █████████████ ███   ███   ███'); sleep(0.0625)
    print('██         ██ ██         ██ ███   ███   ███'); sleep(0.0625)
    print('█████████████ █████████████ ███████████████'); sleep(0.0625)
    print('██[PowerText] version 0.0.2  ---  (07-2017)'); sleep(0.0625)
    print('REPL: hello?')
    main()
    print('REPL: bye?')
