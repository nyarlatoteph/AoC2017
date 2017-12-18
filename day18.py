import re
import queue

class Program(object):
    SND = re.compile(r'snd ([\w-]+)')
    RCV = re.compile(r'rcv ([\w-]+)')
    SET = re.compile(r'set ([\w-]+)\s*([\w-]+)')
    ADD = re.compile(r'add ([\w-]+)\s*([\w-]+)')
    MUL = re.compile(r'mul ([\w-]+)\s*([\w-]+)')
    MOD = re.compile(r'mod ([\w-]+)\s*([\w-]+)')
    JGZ = re.compile(r'jgz ([\w-]+)\s*([\w-]+)')

    def __value_of(self, expression):
        try:
            return int(expression)
        except Exception:
            if expression in self.registers:
                return self.registers[expression]
            else:
                return 0

    def __init__(self, program_id):
        self.registers = {}
        self.recovered = 0
        self.frequency = 0
        self.instructions = []
        self.ip = 0
        self.outgoing_queue = queue.Queue()
        self.incoming_queue = queue.Queue()
        self.sent = 0
        self.registers['p'] = program_id

        with open('input18.txt') as f:
        # with open('test18_2.txt') as f:
            for line in f.readlines():
                self.instructions.append(line)

    def is_terminated(self):
        return self.ip < 0 or self.ip >= len(self.instructions)

    def execute(self):
        if self.is_terminated():
            return False

        line = self.instructions[self.ip]

        m = re.match(Program.SND, line)
        if m:
            # self.frequency = self.__value_of(m.group(1))
            self.outgoing_queue.put(self.__value_of(m.group(1)))
            self.ip += 1
            self.sent += 1
            return True

        m = re.match(Program.RCV, line)
        if m:
            # if self.__value_of(m.group(1)) > 0:
            #     self.recovered = self.frequency
            #     return False
            if not self.incoming_queue.empty():
                self.registers[m.group(1)] = self.incoming_queue.get()
                self.ip += 1
                return True
            return False

        m = re.match(Program.SET, line)
        if m:
            self.registers[m.group(1)] = self.__value_of(m.group(2))
            self.ip += 1
            return True

        m = re.match(Program.ADD, line)
        if m:
            self.registers[m.group(1)] = self.__value_of(m.group(1)) + self.__value_of(m.group(2))
            self.ip += 1
            return True
        
        m = re.match(Program.MUL, line)
        if m:
            self.registers[m.group(1)] = self.__value_of(m.group(1)) * self.__value_of(m.group(2))
            self.ip += 1
            return True

        m = re.match(Program.MOD, line)
        if m:
            self.registers[m.group(1)] = self.__value_of(m.group(1)) % self.__value_of(m.group(2))
            self.ip += 1
            return True

        m = re.match(Program.JGZ, line)
        if m:
            if self.__value_of(m.group(1)) > 0:
                self.ip += self.__value_of(m.group(2))
            else:
                self.ip += 1
            return True
        print('unmatched line: %s' % line)


p0 = Program(0)
p1 = Program(1)
deadlock = False
terminated = False

while not deadlock and not terminated:
    p1.incoming_queue = p0.outgoing_queue
    p0.incoming_queue = p1.outgoing_queue
    a = p0.execute()
    b = p1.execute()
    terminated = p0.is_terminated() and p1.is_terminated()
    deadlock = not a and not b

print(deadlock, terminated, p1.sent)
# print(p.recovered)