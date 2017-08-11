#symbols.py: [PowerText] 
# _*_ coding:utf8 _*_

#TODO: Namespaces

from exceptions import UndefinedVariable, UndefinedFunction

class Symbols:
    __func      = 'functions'
    __vars      = 'variables'
    __local     = 'local'
    __localfunc = 'localfunctions'

    table = {
            __func      : {},
            __vars      : {},
            __local     : [],
            __localfunc : [],
    }

    def is_variable(self, name):
        return name in self.table[self.__vars].keys()

    def islocal(self):
        return len(self.table[self.__local]) > 0

    def islocalfunction(self):
        return len(self.table[self.__localfunc]) > 0

    def get_local_table(self):
        table = self.table[self.__local]
        return table[len(table)-1]

    def get_localfunc_table(self):
        table = self.table[self.__localfunc]
        return table[len(table) -1]

    def set_variable(self, name, value, is_global=False):
        if self.islocal() and not is_global:
            self.get_local_table()[name] = value
        else:
            self.table[self.__vars][name] = value
        return value

    def set_item(self, name, index, value):
        item = self.get_variable(name)
        item[index] = value
        return item

    def get_variable(self, name, force_global=False):
        if self.islocal() and not force_global:
            for symbols in reversed(self.table[self.__local]):
                if name in symbols:
                    return symbols[name]
        try: return self.table[self.__vars][name]
        except KeyError:
            raise UndefinedVariable(f'*** undefined variable: {name}')
            return None

    def del_variable(self, name):
        try: return self.table[self.__vars].pop(name)
        except KeyError:
            raise UndefinedVariable(f'*** undefined variable: {name}')

    def set_local(self):
        self.table[self.__local].append({})
        self.table[self.__localfunc].append({})

    def del_local(self):
        self.table[self.__local].pop()
        self.table[self.__localfunc].pop()

    def is_function(self, name):
        return name in self.table[self.__func].keys()

    def set_function(self, name, parameters, body):
        if self.islocalfunction():
            self.get_localfunc_table()[name] = [parameters, body]
        else:
            self.table[self.__func][name] = [parameters, body]

    def get_function(self, name):
        if self.islocalfunction():
            for symbols in reversed(self.table[self.__localfunc]):
                if name in symbols:
                    return symbols[name]
        try: return self.table[self.__func][name]
        except KeyError:
            raise UndefinedFunction(f'*** undefined function: {name}')
            return None

    def del_function(self, name):
        try: return self.table[self.__func].pop(name)
        except KeyError:
            raise UndefinedFunction(f'*** undefined function: {name}')
            return None
