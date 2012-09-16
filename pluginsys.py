import os
import sys

class pluginManager():
  def __init__(self,pluginsdir="plugins"):
    self.plugins={}
    self._pluginsdir=pluginsdir
    
  def getAvailablePlugins(self):
    for filen in os.listdir(self._pluginsdir):
      nam,ext=os.path.splitext(filen)
      if ext.endswith(".py") and not nam.startswith("__"):
        yield nam
  
  def loadPlugins(self):
    oldsyspath=sys.path
    sys.path.append(self._pluginsdir)
    for plugin in self.getAvailablePlugins():
      plug=__import__(plugin)
      self.plugins[plug.name]=plug
    sys.path=oldsyspath
  
  def purgePlugins(self):
    self.plugins={}
  
  def reloadPlugins(self):
    for i in self.plugins.values():
      reload(i)
    self.purgePlugins()
    self.loadPlugins()
  
  def listPlugins(self):
    for plg in self.plugins.keys():
      yield plg
  
  def getPlugins(self):
    for plg in self.plugins.values():
      yield plg
  
  def callPlugin(self,pluginName,args):
    self.plugins[pluginName.upper()].plugin_main(*args,**kwargs)