import immlib
import getopt
import immutils
from immutils import *
imm = immlib.Debugger()

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
        imm.Log("Number of arguments : %d " % len(args))
        cnt=0
        while (cnt < len(args)):
            imm.Log(" Argument %d : %s" % (cnt+1,args[cnt]))
            if (args[cnt] == "world"):
                imm.Log("  You said %s !" % (args[cnt]),focus=1, highlight=1)
            cnt=cnt+1
