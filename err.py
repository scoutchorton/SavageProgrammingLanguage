from random import randint
"""
ERROR CODES
00.0 - Test Code
     * Whoops. You're lucky to see this. +1 to you!
     * This is a test. This is a test. This is a test.
     * Easter egg!
01.# - Syntax
    .1 - Space in code
       * I bet you don't like walking over voids in the ground. Me either. Could ya' fix that for me?
       * We encountered a space here. Who do you think I am, NASA or something?
       * Hello ~spaces~, my old friend!
"""
def randItem(dic):
  return dic[randint(0, len(dic)-1)]
  

def errRet(errCod):
  errCods = {
    00.0: ["Test Error", 
    ["Whoops. You're lucky to see this. +1 to you!", "Testing, testing, 1, 2, 3, testing, testing.", "Easter egg!"]],
    01.1: ["Syntax - Space In Code",
    ["I bet you don't like walking over voids in the ground. Me either. Could ya' fix that for me?", "We encountered a space here. Who do you think I am, NASA or something?", "Hello darkness, err, spaces, my old friend!"]]
  }
  if not (errCod in errCods.keys()):
    print "ERR 00.0: " + errCods[00.0][0],
    print randItem(errCods[00.0][1])
  else:
    print "ERR " + str(errCod) + ": " + errCods[errCod][0] + ":",
    print randItem(errCods[errCod][1])