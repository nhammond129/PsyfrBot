PsyfrBot
========

Modular (plugin-based) bot framework in Python. 

Designed to be easily implemented with various protocols, and let extensions
written working with one protocol be easily transferrable to another.
For example, with chatango chats using ch.py:

<pre>
import ch
import _thread
from PsyfrBot import psyfrbot

BOTPRC=psyfrbot.botprocessor(commandSym=".")
BOTPRC.ignore("Hashbot")
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
</pre>