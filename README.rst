============================
ZenPacks.community.LogMatch
============================


Description
===========
This ZenPack monitors logfiles using SNMP capabilities from the netSnmp UCD agent.


Features
========

Device and component object classes
-----------------------------------
* LogMatchDevice with new attributes of:

  - versionTag
  - versionDate

The 1.0.2 version of this ZenPack ignores the LogMatchDevice definition and
modifies the __init__.py to make the LogMatch a component of the os component of
the Device class.  The versionTag and versionDate attributes are added directly to
the Device class attributes.

* LogMatch component with new attributes:

  - logMatchName = ''
  - logMatchFilename = ''
  - logMatchRegEx = ''
  - logMatchCycle = 300
  - logMatchErrorFlag = 0
  - logMatchRegExCompilation = ''


where LogMatchDevice -> contains many LogMatch components


Modeler Plugins
---------------

* LogMatchDeviceMap which gathers:

  - versionTag
  - versionDate

* LogMatchMap which populates:

  - logMatchName
  - logMatchFilename
  - logMatchRegEx
  - logMatchCycle
  - logMatchErrorFlag
  - logMatchRegExCompilation

The 1.0.2 version of the ZenPack chnges the LogMatchMap modeler to ensure the LogMatch
components are added to a Device's os component.


Monitoring Templates
--------------------

* Component templates

  - LogMatch with an SNMP datasource to gather logMatchCurrentCounter (1.3.6.1.4.1.2021.16.2.1.7) with a GAUGE datapoint


MIBs
----
* UCD-SNMP-MIB


GUI modifications
-----------------

* The Overview display for a device of object class LogMatchDevice has the SNMP panel
  modified to remove the SNMP community name and to add versionTag and versionDate.

Usage
=====

It is suggested that a new Zenoss Device Class be created to hold devices of object class LogMatchDevice.
Set the zPythonPath zProperty of the new class to be ZenPacks.community.LogMatch.LogMatchDevice.

The community.snmp.LogMatchDeviceMap and community.snmp.LogMatchMap modeler plugins should also be
assigned to this Zenoss Device Class.

The 1.0.2 version of the ZenPack will need the modeler plugins assigning either to a relevant
class or to specifi device instances.


Requirements & Dependencies
===========================

* Zenoss Versions Supported:  4.x
* External Dependencies: 


* Installation Notes: 

  - Restart zenoss entirely after installation 



Download
========
Download the appropriate package for your Zenoss version from the list
below.

* Zenoss 4.0+ `Latest Package for Python 2.7`_

ZenPack installation
======================

This ZenPack can be installed from the .egg file using either the GUI or the
zenpack command line. 

To install in development mode, find the repository on github and use the *Download ZIP* button
(right-hand margin) to download a tgz file and unpack it to a local directory, say,
/code/ZenPacks .  Install from /code/ZenPacks with::
  zenpack --link --install ZenPacks.community.LogMatch
  Restart zenoss after installation.

Device Support
==============

This ZenPack has been tested against 
version 5.6.1 of the netSnmp agent.

Limitations and Troubleshooting
===============================



Change History
==============
* 1.0.0
   - Initial Release
* 1.0.1
   - Modified Overview display for LogMatchDevice devices to remove SNMP community and to add 
     versionTag and versionDate to the SNMP panel.
* 1.0.2
   - The 1.0.2 version of this ZenPack ignores the LogMatchDevice definition and
     modifies the __init__.py to make the LogMatch a component of the os component of
     the Device class.  The versionTag and versionDate attributes are added directly to
     the Device class attributes. The version is held in the device branch on github.

Screenshots
===========

See the screenshots directory.


.. External References Below. Nothing Below This Line Should Be Rendered

.. _Latest Package for Python 2.7: https://github.com/ZenossDevGuide/ZenPacks.community.LogMatch/blob/device/dist/ZenPacks.community.LogMatch-1.0.2-py2.7.egg?raw=true

Acknowledgements
================


