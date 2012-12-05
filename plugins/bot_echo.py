name="BOT_ECHO_PLUGIN"
trigger="echo"
reqlvl=0
help="""\
echo [message]"""
##
##

isMatch=lambda x,y: x.lower()==y.lower()

def plugin_main(usrobj,message,pBotproc):
  # "message"  - Message passed that activated this plugin
  # "pBotproc" - botprocessor class that called this plugin
  return " ".join(message.split(" ")[1:])
  
  