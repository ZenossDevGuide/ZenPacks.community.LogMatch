# Nothing is required in this __init__.py, but it is an excellent place to do
# many things in a ZenPack.
#
# The example below which is commented out by default creates a custom subclass
# of the ZenPack class. This allows you to define custom installation and
# removal routines for your ZenPack. If you don't need this kind of flexibility
# you should leave the section commented out and let the standard ZenPack
# class be used.
#
# Code included in the global scope of this file will be executed at startup
# in any Zope client. This includes Zope itself (the web interface) and zenhub.
# This makes this the perfect place to alter lower-level stock behavior
# through monkey-patching.

import Globals
from Products.ZenUtils.Utils import unused
unused(Globals)
from Products.ZenModel.ZenPack import ZenPack as ZenPackBase
from Products.ZenRelations.RelSchema import ToManyCont, ToOne
from Products.ZenModel.OperatingSystem import OperatingSystem

from Products.ZenModel.Device import Device
from Products.Zuul.infos import ProxyProperty
from Products.Zuul.infos.device import DeviceInfo

# Monkey patch the logMatchs relationship on to the existing OperatingSystem relationships
#  and versionTag and versionDate on to Device
OperatingSystem._relations += (("logMatchs", ToManyCont(ToOne, "ZenPacks.community.LogMatch.LogMatch", "os")), )
Device.versionTag = ''
Device.versionDate = ''
# Make a device's version attributes available through the API.
# We need the DeviceInfo info class extending.
DeviceInfo.versionTag = ProxyProperty('versionTag')
DeviceInfo.versionDate = ProxyProperty('versionDate')

# Also need the interfaces information by extending IDeviceInfo
from Products.Zuul.form import schema
from Products.ZenModel.ZVersion import VERSION as ZENOSS_VERSION
from Products.ZenUtils.Version import Version
if Version.parse('Zenoss %s' % ZENOSS_VERSION) >= Version.parse('Zenoss 4'):
    SingleLineText = schema.TextLine
    MultiLineText = schema.Text
else:
    SingleLineText = schema.Text
    MultiLineText = schema.TextLine

from Products.Zuul.interfaces.device import IDeviceInfo
from Products.Zuul.utils import ZuulMessageFactory as _t
IDeviceInfo.versionTag = SingleLineText(title=_t(u"Version Tag"))
IDeviceInfo.versionDate = SingleLineText(title=_t(u"Version Date"))

class ZenPack(ZenPackBase):

     def install(self, dmd):
         ZenPackBase.install(self, dmd)

         # Put your customer installation logic here.
         for d in self.dmd.Devices.getSubDevices():
             d.os.buildRelations()

     def remove(self, dmd, leaveObjects=False):
         if not leaveObjects:
             # When a ZenPack is removed the remove method will be called with
             # leaveObjects set to False. This means that you likely want to
             # make sure that leaveObjects is set to false before executing
             # your custom removal code.
             OperatingSystem._relations = tuple([x for x in OperatingSystem._relations if x[0] not in ['logMatchs']])
             for d in self.dmd.Devices.getSubDevices():
                 d.os.buildRelations()

         ZenPackBase.remove(self, dmd, leaveObjects=leaveObjects)
