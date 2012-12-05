name="BOT_MATH_PLUGIN"
trigger="math"
reqlvl=0
help="""\
math [rand,eval]
  rand [arg1] [arg2]
  eval [expression]"""
##
##
import random
isMatch=lambda x,y: x.lower()==y.lower()

def plugin_main(usrobj,message,pBotproc):
  # "message"  - Message passed that activated this plugin
  # "pBotproc" - botprocessor class that called this plugin
  Splitmsg=message.split(" ")[1:]
  if len(Splitmsg)<1:
    return help
  if isMatch(Splitmsg[0],"rand"):
    if len(Splitmsg)>1:
      x=0
      try:
        y=int(Splitmsg[1])
      except:
        y=99
      if len(Splitmsg)>2:
        try:
          x=int(Splitmsg[2])
        except:
          x=99;y=0
        return "Rand(%d,%d)=%d"%(y,x,random.randrange(y,x))
      else:
        return "Rand(0,%d)=%d"%(y,random.randrange(x,y))
    else:
      return "Rand(0,99)=%d"%(y,random.randrange(0,99))
  elif isMatch(Splitmsg[0],"eval"):
    try:
      expr="".join(Splitmsg[1:])
      return "%s = %d"%(expr,eval(expr))
    except:
      return pBotproc.defaultError
  else:
    return help