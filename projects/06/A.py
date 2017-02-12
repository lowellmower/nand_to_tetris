import re

REGX_A_COMMAND = r"^@(?P<value>\d+)$"

class ACommand:
    """
    ACommand is the class responsible for interpreting the A instructions from assembly
    and converting those to their respecitve binary forms. For a detailed spec see the
    README.md in the root of this project.

    Basic A instructions look like:
        ASSEMBLY: @9
        BINARY: 0000000000001001

    This binary representation then maps to the instruciton table provided along side
    this file at: instructions_table.md
    """
    def __init__(self, val):
        if val > 2**15-1:
            raise ValueError("%d is too large." % val)
        self.val = val
    def __str__(self):
        return "ACommand: %d" % self.val
    def opcode(self):
        return bin(self.val)[2:].zfill(16)

def accept(line):
    return True if re.match(REGX_A_COMMAND, line) else False

def new(line):
    line = line.strip()
    if not accept(line):
        raise SyntaxError("Not an A Command", (None, -1, 0, line))
    m = re.match(REGX_A_COMMAND, line)
    value = m.group("value")
    try:
        val = int(value)
    except ValueError:
        raise SyntaxError("Invalid A Command", (None, -1, 0, line))
    try:
        return ACommand(val)
    except ValueError:
        raise SyntaxError("Value for A Command is Invalid.", (None, -1, 0, value))
