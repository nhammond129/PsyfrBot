import _thread
import shelve
import sys
import os
import traceback
from datetime import datetime

def FancyExceptionThrower(func,*args, **kwargs):
  def wrapper(*args, **kwargs):
    try:
      func(*args, **kwargs)
    except Exception as exc:
      traceback.print_exc()
      print("Exception occurred in %s"%func.__name__)
      if len(args)>0:
        print("with args: {\n  "+"\n  ".join([repr(i) for i in args])+"\n}")
      if len(kwargs)>0:
        print("with kwargs: {\n  "+
          "\n  ".join(["%s = %s"%(i,repr(j)) for i,j in kwargs.items()])
          +"\n}")
      input("Awaiting dismissal...")
      sys.exit(1)
  return wrapper

# There's a better way to do this, yes?
#  If so, someone please fork and request a pull/open an issue with the fix.
osp=sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import pluginsys
sys.path=osp

isMatch=lambda x,y:x.lower()==y.lower()

class user:
  @FancyExceptionThrower
  def __init__(self,lvl):
    self.level=lvl

class botprocessor:
  @FancyExceptionThrower
  def __init__(self,
      commandSym="!", #Command symbol, like "!dothings"
      configlocation="config.cfg",
      userslocation="users.dat",
      defaultError="Exception occurred or no match detected.",
      respondFunc=None,
      doLogging=True):
    self._respondFunc=respondFunc
    self.defaultError=defaultError
    self.commandSym=commandSym
    self.doLogging=doLogging
    self._ignore=[]
    self._configloc=configlocation
    self._usersloc=userslocation
    self.pluginManager=pluginsys.pluginManager()
    self.users={}
    self.config={}
    
  @FancyExceptionThrower
  def ignore(self,name):
    if name.lower() not in self._ignore:
      self._ignore.append(name.lower())
  
  @FancyExceptionThrower
  def saveconfig(self):
    conffile=shelve.open(self._configloc)
    for i in self.config:
      self.conffile[i]=self.config[i]
    conffile.close()
  
  @FancyExceptionThrower
  def loadconfig(self):
    conffile=shelve.open(self._configloc)
    for i in conffile:
      self.config[i]=conffile[i]
    conffile.close()
  
  @FancyExceptionThrower
  def saveusers(self):
    usrfile=shelve.open(self._usersloc)
    for i in self.users:
      usrfile[i]=self.users[i]
    usrfile.close()
  
  @FancyExceptionThrower
  def loadusers(self):
    usrfile=shelve.open(self._usersloc)
    for i in usrfile:
      self.users[i]=usrfile[i]
    usrfile.close()
    
  @FancyExceptionThrower
  def MsgLog(self,msg):
    logF=open("logs/"+"LOG_"+datetime.now().strftime("%b-%d-%Y").upper()+".txt","a+")
    logF.write(datetime.now().strftime("{%H:%M:%S} ")+msg+"\n")
    logF.flush()
    logF.close()
  
  @FancyExceptionThrower
  def Save(self):
    self.saveconfig()
    self.saveusers()
  
  @FancyExceptionThrower
  def Load(self):
    self.loadconfig()
    self.loadusers()
  
  @FancyExceptionThrower
  def getuser(self,usrname):
    usrname=usrname.lower()
    if usrname in self.users.keys():
      return self.users[usrname]
    else:
      return None
      
  @FancyExceptionThrower
  def adduser(self,usrname,lvl=0):
    usrname=usrname.lower()
    if self.getuser(usrname):
      return None
    else:
      self.users[usrname]=user(lvl)
  
  @FancyExceptionThrower
  def messageparser(self,message):
    #overriding encouraged
    return message.split(" ")
  
  @FancyExceptionThrower
  def get_response(self,message,usrname):
    #probably want to override if messageparser is overridden.
    if self.doLogging:
      self.MsgLog("["+usrname+"]: "+message)
    if not message.startswith(self.commandSym):
      return None
    SplitMsg=self.messageparser(message)
    self.adduser(usrname)
    if usrname.lower() in self._ignore and self.getuser(usrname).level!=31337:
      return None
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
  
  @FancyExceptionThrower
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
  print("Ready.\n  Try starting with '!help'")
  while True:
    x=input("")
    print(BOTPRC.get_response(x,NAME))
