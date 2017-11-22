# -*- coding: utf-8 -*-
import err
from interpreter import interpreter
print "#"*32 + "\n#SAVAGE PROGRAMMING INTERPRETER#\n" + "#"*32
print "Type \"run\" to run code in \"code\" file, or \"run file\" to run code from an alternate file."
while 1:
  p = raw_input("> ")
  if p.lower() == "run":
    interpreter('code').run()
  elif p.split(" ")[0] == "run":
    interpreter(p.split[1]).run()
