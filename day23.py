import re
import queue

class Program(object):
    SET = re.compile(r'set ([\w-]+)\s*([\w-]+)')
    SUB = re.compile(r'sub ([\w-]+)\s*([\w-]+)')
    MUL = re.compile(r'mul ([\w-]+)\s*([\w-]+)')
    JNZ = re.compile(r'jnz ([\w-]+)\s*([\w-]+)')

    def __value_of(self, expression):
        try:
            return int(expression)
        except Exception:
            if expression in self.registers:
                return self.registers[expression]
            else:
                return 0

    def __init__(self):
        self.registers = {}
        self.instructions = []
        self.mul_called = 0
        self.ip = 0
        self.registers['a'] = 1

        with open('input23.txt') as f:
        # with open('test18_2.txt') as f:
            for line in f.readlines():
                self.instructions.append(line)

    def is_terminated(self):
        return self.ip < 0 or self.ip >= len(self.instructions)

    def execute(self):
        if self.is_terminated():
            return False

        line = self.instructions[self.ip]

        m = re.match(Program.SET, line)
        if m:
            self.registers[m.group(1)] = self.__value_of(m.group(2))
            self.ip += 1
            return True

        m = re.match(Program.SUB, line)
        if m:
            self.registers[m.group(1)] = self.__value_of(m.group(1)) - self.__value_of(m.group(2))
            self.ip += 1
            return True
        
        m = re.match(Program.MUL, line)
        if m:
            self.mul_called += 1
            self.registers[m.group(1)] = self.__value_of(m.group(1)) * self.__value_of(m.group(2))
            self.ip += 1
            return True

        m = re.match(Program.JNZ, line)
        if m:
            if self.__value_of(m.group(1)) != 0:
                self.ip += self.__value_of(m.group(2))
            else:
                self.ip += 1
            return True
        print('unmatched line: %s' % line)

p = Program()
terminated = False

while not terminated:
    p.execute()
    terminated = p.is_terminated()

print(p.mul_called)
print(p.registers['h'])