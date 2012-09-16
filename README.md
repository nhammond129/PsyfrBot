import ch
import _thread
from PsyfrBot import psyfrbot

BOTPRC=psyfrbot.botprocessor(commandSym=".")
BOTPRC.ignore("Hashbot") # Replace it with whatever your bot identifies as so it doesn't reply to itself.
BOTPRC.pluginManager.loadPlugins()
BOTPRC.loadconfig()
BOTPRC.loadusers()
BOTPRC.adduser("Nullspeaker",lvl=31337)

class botClass(ch.RoomManager):
  def onMessage(self, room, user, message):
    print(user.name+":"+message.body)
    # I know this is identical to BOTPRC.reply, but I'm nervous about
    #  having multiple rooms. 
    _thread.start_new_thread(
        room.message,(BOTPRC.get_response(message.body,user.name),)
      )
  
  def onFloodWarning(self, room):
    room.reconnect()

botClass.easy_start()
BOTPRC.saveconfig()
BOTPRC.saveusers()