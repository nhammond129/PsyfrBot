name="BOT_HELP_PLUGIN"
trigger="help"
reqlvl=0
help="""\
help [cmd]"""
##
##

isMatch=lambda x,y: x.lower()==y.lower()

def plugin_main(message,pBotproc):
  # "message"  - Message passed that activated this plugin
  # "pBotproc" - botprocessor class that called this plugin
  if len(message.split(" "))>1:
    Splitmsg=message.split(" ")[1:]
    for i in pBotproc.pluginManager.getPlugins():
      if isMatch(Splitmsg[0].lower(),i.trigger.lower()):
        return i.help
  return "COMMANDS: \n"+" ".join([pBotproc.commandSym+i.trigger for i in pBotproc.pluginManager.getPlugins()])