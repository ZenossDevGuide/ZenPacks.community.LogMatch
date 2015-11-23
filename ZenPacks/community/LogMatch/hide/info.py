# This file is the conventional place for "Info" adapters. Info adapters are
# a crucial part of the Zenoss API and therefore the web interface for any
# custom classes delivered by your ZenPack. Examples of custom classes that
# will almost certainly need info adapters include datasources, custom device
# classes and custom device component classes.

# Mappings of interfaces (interfaces.py) to concrete classes and the factory
# (these info adapter classes) used to create info objects for them are managed
# in the configure.zcml file.

from zope.component import adapts
from zope.interface import implements

from Products.Zuul.infos import ProxyProperty
from Products.Zuul.infos.component import ComponentInfo
from Products.Zuul.infos.device import DeviceInfo

from ZenPacks.community.LogMatch.LogMatch import LogMatch
from ZenPacks.community.LogMatch.LogMatchDevice import LogMatchDevice
from ZenPacks.community.LogMatch.interfaces import ILogMatchInfo
from ZenPacks.community.LogMatch.interfaces import ILogMatchDeviceInfo

class LogMatchInfo(ComponentInfo):
    implements(ILogMatchInfo)
    adapts(LogMatch)

    logMatchName = ProxyProperty("logMatchName")
    logMatchFilename = ProxyProperty("logMatchFilename")
    logMatchRegEx = ProxyProperty("logMatchRegEx")
    logMatchCycle = ProxyProperty("logMatchCycle")
    logMatchErrorFlag = ProxyProperty("logMatchErrorFlag")
    logMatchRegExCompilation = ProxyProperty("logMatchRegExCompilation")
    snmpindexblah  = ProxyProperty("snmpindex")

class LogMatchDeviceInfo(DeviceInfo):
    implements(ILogMatchDeviceInfo)
    adapts(LogMatchDevice)

    versionTag = ProxyProperty("versionTag")
    versionDate = ProxyProperty("versionDate")
