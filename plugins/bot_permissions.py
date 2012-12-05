name="BOT_PERMISSIONS_PLUGIN"
trigger="permissions"
reqlvl=31337
help="""\
permissions [set,get]
  set [username] [lvl]
  get [username]"""
##
##

isMatch=lambda x,y: x.lower()==y.lower()

def plugin_main(usrobj,message,pBotproc):
  # "message"  - Message passed that activated this plugin
  # "pBotproc" - botprocessor class that called this plugin
  Splitmsg=message.split(" ")[1:]
  if len(Splitmsg)<1:
    return help
  if isMatch(Splitmsg[0],"set"):
    usr=pBotproc.getuser(Splitmsg[1])
    if usr==None:
      return "No such user \"%s\"."%Splitmsg[1]
    else:
      oldlvl=usr.level
      try:
        usr.level=int(Splitmsg[2])
        return "%s had their permission level changed from %d to %d."%(Splitmsg[1],oldlvl,usr.level)
      except ValueError:
        return "The permissions level of %s was unchanged due to invalid arg \"%s\""%Splitmsg[1:2]
  elif isMatch(Splitmsg[0],"get"):
    usr=pBotproc.getuser(Splitmsg[1])
    if usr==None:
      return "No such user \"%s\"."%Splitmsg[1]
    else:
      return usr.level
  else:
    return help
  
  