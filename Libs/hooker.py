import immlib
from immlib import LogBpHook

class HookFunc(LogBpHook):

    def __init__(self):
        LogBpHook.__init__(self)
        return

    def run(self,regs):
        return
