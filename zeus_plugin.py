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


"""
Main application
"""
def main(args):
    if not args:
        usage()
    else:
        funcName = args[0]
        hookAddr = imm.getAddress(funcName)

        hook = HookFunc()
        hook.add(funcName,hookAddr)
        return funcName + " Hooked."

if __name__ == "__main__":
    main()

