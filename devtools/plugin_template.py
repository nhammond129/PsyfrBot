name="BOT_*****_PLUGIN"
trigger="*****"
reqlvl=*****
help="""\
***** [*****]"""
##
##

isMatch=lambda x,y: x.lower()==y.lower()

def plugin_main(message,pBotproc):
  # "message"  - Message passed that activated this plugin
  # "pBotproc" - botprocessor class that called this plugin
  Splitmsg=message.split(" ")[1:]
  if len(Splitmsg)<1:
    return help
  if isMatch(Splitmsg[0],"ARG1"):
    pass
  elif isMatch(Splitmsg[0],"ARG2"):
    pass
  elif isMatch(Splitmsg[0],"ARG3"):
    pass
  
  