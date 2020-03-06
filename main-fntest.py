from ctypes import *
import sys
def main_checker(libraryDst):
    cdll.LoadLibrary(libraryDst)  
    hello = CDLL(libraryDst)
    print(libraryDst+" main return code: "+str(hello.main()))

if len (sys.argv) != 2 :
    print "Usage: python main-fntest.py [library_location/library]"
    print "Example: python main-fntest.py ~/libtest.so"
    sys.exit (1)

library_name = sys.argv[1]
main_checker(library_name)