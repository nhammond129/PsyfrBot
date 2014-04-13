name="BOT_PLUGIN_MANAGER"
trigger="plugman"
reqlvl=31337
help="""\
plugman [(l)ist,(r)eload]
  list [(a)vailable,(l)oaded]"""
##
##

isMatch=lambda x,y: x.lower()==y.lower()

def plugin_main(usrobj,message,pBotproc):
  # "message"  - Message passed that activated this plugin
  # "pBotproc" - botprocessor class that called this plugin
  # "usrobj"   - User class that pasted the message calling this plugin
  Splitmsg=message.split(" ")[1:]
  if len(Splitmsg)<1:
    return help
  if isMatch(Splitmsg[0],"reload"):
    pBotproc.pluginManager.reloadPlugins()
    return "Reloaded plugins."
  elif isMatch(Splitmsg[0],"list") or isMatch(Splitmsg[0],"l"):
    if len(Splitmsg)>1:
      if isMatch(Splitmsg[1],"a") or isMatch(Splitmsg[1],"available"):
        return "Available Plugins:"+(
          " ".join(pBotproc.pluginManager.getAvailablePlugins())
        )
      elif isMatch(Splitmsg[1],"l") or isMatch(Splitmsg[1],"loaded"):
        return "Loaded Plugins:"+(
          " ".join(pBotproc.pluginManager.listPlugins())
        )
      else:
        return "Unknown namespace \"%s\""%Splitmsg[1]
    else:
      return "Loaded Plugins:"+(
        " ".join(pBotproc.pluginManager.listPlugins())
      )
  else:
    return help
      
    
  
  
  