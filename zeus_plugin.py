import immlib
import getopt
import immutils
from immutils import *
from hooker import *
imm = immlib.Debugger()
"""
imm must be on this line
"""

logfile="zeus.log"

"""
Template 'inspired' (:D) from @corelan.be
"""

"""
Helper Functions
"""

def usage():
    imm.Log("  ** No arguments specified ** ")
    imm.Log("  Usage : ")
    imm.Log("       blah blah")

"""
FILE=open(filename,"a")  #this will append to the file
FILE.write("Blah blah" + "\n")
FILE.close()
"""

def clearFile(file):
    FILE = open(file,"w")
    FILE.write("")
    FILE.close()
    return ""

def writeFile(info, filename):
    info = info.replace('\n',' - ')
    FILE = open(filename,"a")
    FILE.write(info+"\n")
    FILE.close()
    return ""


def search(query):
    results = imm.Search(imm.Assemble (query))

"""
Main application
"""
def main(args):
    if not args:
        usage()
    else:
        funcName = args[0]

        #hookAddr = imm.getAddress(funcName)
        #hook = HookFunc()
        #hook.add(funcName,hookAddr)

        imm.setBreakpointOnName(funcName)
        # imm.getCurrentAddress()
        imm.stepIn()

        # search 1st tell-tale instructions
        results = imm.Search(imm.Assemble ("REP MOVS ANY, ANY"))
        for r in results:
            imm.log("Found 1st instruction, setting breakpoint")
            imm.setBreakpoint(r)

        results = imm.Search(imm.Assemble ("MOV ANY, ANY\n XOR ANY, ANY\n INC EAX\n DEC ESI"))
        for r in results:
            imm.log("Found 2st instruction, setting breakpoint")
            imm.setBreakpoint(r)

        # while
         # execute
         # log

        # set breakpoint at the end of instruction

        """
        curFunc = imm.getCurrentAddress()
        blocks  = curFunc.getBasicBlocks()
        calls   = basicBlocks[0].getCalls()

        for c in calls:
            oc   = imm.disasm(c)
            call = oc.getDisasm()
            if
        """

        return "Search for " + args[0] + "finished"

if __name__ == "__main__":
    main()
