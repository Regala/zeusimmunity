import immlib
from immlib import LogBpHook

class HookFunc(LogBpHook):

    def __init__(self):
        LogBpHook.__init__(self)
        return

    def run(self,regs):

    def main(args):
        if not args:
        return "No arguments provided."

        # args[0] = "HttpSendRequestA"
        imm = immlib.Debugger()

        funcName = args[0]
        hookAddr = imm.getAddress(funcName)

        hook = HookFunc()
        hook.add(funcName,hookAddr)
        return funcName + " Hooked."
