import immlib
from immlib import BpHook
"""
Template 'inspired' (:D) from @corelan.be
"""

DESC = "Searches for Zeus/Zbot webinjects"

class HookFunc(BpHook):

    def __init__(self):
        BpHook.__init__(self)

    def run(self, regs):
        """ Runs """
        imm = immlib.Debugger()
        imm.log("Hook called")
        imm.updateLog()
        #imm.pause()
        #imm.stepIn() # enter malicious JMP
        #imm.log("Stepped in and paused")

"""
Main application
"""
def main(args):
    if not args:
        imm.log("Error args")
    else:
        imm = immlib.Debugger()
        #funcName = args[0]
        funcName = "HttpSendRequestA"

        #hookAddr = imm.getAddress(funcName)
        #hook = HookFunc()
        #hook.add(funcName,hookAddr)

        imm.setBreakpointOnName(funcName)
        # imm.getCurrentAddress()
        imm.stepIn()

        # search 1st tell-tale instructions
        results = imm.search(imm.assemble ("REP MOVS ANY,ANY"))
        for r in results:
            imm.log("Found 1st instruction, setting breakpoint")
            imm.setBreakpoint(r)

        results = imm.search(imm.assemble ("MOV ANY, ANY\n XOR ANY, ANY\n INC EAX\n DEC ESI"))
        for r in results:
            imm.log("Found 2st instruction, setting breakpoint")
            imm.setBreakpoint(r)

        """
        curFunc = imm.getCurrentAddress()
        blocks  = curFunc.getBasicBlocks()
        calls   = basicBlocks[0].getCalls() 

        for c in calls:
            oc   = imm.disasm(c)
            call = oc.getDisasm()
            if
        """

        imm.updateLog()
        return "Search for " + args[0] + "finished"
