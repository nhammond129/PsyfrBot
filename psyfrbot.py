import _thread
import shelve
import pluginsys

isMatch=lambda x,y:x.lower()==y.lower()

class user:
  def __init__(self,lvl):
    self.level=lvl

class botprocessor:
  def __init__(self,
      commandSym="!", #Command symbol, like "!dothings"
      configlocation="config.cfg",
      userslocation="users.dat",
      defaultError="Exception occurred or no match detected.",
      respondFunc=None):
    self._respondFunc=respondFunc
    self.defaultError=defaultError
    self.commandSym=commandSym
    self._configloc=configlocation
    self._usersloc=userslocation
    self.pluginManager=pluginsys.pluginManager()
    self.users={}
    self.config={}
  
  def saveconfig(self):
    conffile=shelve.open(self._configloc)
    for i in self.config:
      self.conffile[i]=self.config[i]
    conffile.close()
  
  def loadconfig(self):
    conffile=shelve.open(self._configloc)
    for i in conffile:
      self.config[i]=conffile[i]
    conffile.close()
  
  def saveusers(self):
    usrfile=shelve.open(self._usersloc)
    for i in self.users:
      usrfile[i]=self.users[i]
    usrfile.close()
    
  def loadusers(self):
    usrfile=shelve.open(self._usersloc)
    for i in usrfile:
      self.users[i]=usrfile[i]
    usrfile.close()
  
  def Save(self):
    self.saveconfig()
    self.saveusers()
    
  def Load(self):
    self.loadconfig()
    self.loadusers()
  
  def getuser(self,usrname):
    usrname=usrname.lower()
    if usrname in self.users.keys():
      return self.users[usrname]
    else:
      return None
    
  def adduser(self,usrname,lvl=0):
    usrname=usrname.lower()
    if self.getuser(usrname):
      return None
    else:
      self.users[usrname]=user(lvl)
    
  def messageparser(self,message):
    #overriding encouraged
    return message.split(" ")
    
  def get_response(self,message,usrname):
    #probably want to override if messageparser is overridden.
    SplitMsg=self.messageparser(message)
    self.adduser(usrname)
    for plugin in self.pluginManager.getPlugins():
      if isMatch(self.commandSym+plugin.trigger,SplitMsg[0]):
        if self.getuser(usrname).level>=plugin.reqlvl:
          returned=plugin.plugin_main(message,self)
          if returned==None:
            return self.defaultError
          else:
            return returned
        else:
          return "Invalid permission rank."
    return self.defaultError
    
  def reply(self,message,usrname):
    if self._respondFunc==None:
      return None
    else:
      _thread.start_new_thread(
        self._respondFunc,(self.get_response(message,usrname),)
      )
      
if __name__=="__main__":
  BOTPRC=botprocessor(respondFunc=print)
  BOTPRC.pluginManager.loadPlugins()
  BOTPRC.adduser("Nullspeaker",lvl=31337)
  #BOTPRC.saveusers()
  NAME="Nullspeaker"
  while True:
    x=input("")
    BOTPRC.reply(x,NAME)
