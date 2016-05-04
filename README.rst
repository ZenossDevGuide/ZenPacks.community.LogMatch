============================
ZenPacks.community.LogMatch
============================


Description
===========
This ZenPack monitors logfiles using SNMP capabilities from the netSnmp UCD agent.

This version of the ZenPack uses zenpacklib and is version 1.0.3.

zenpacklib usage
----------------

This ZenPack is built with the zenpacklib library so does not have explicit code definitions for
device classes, device and component objects or zProperties.  Templates are also created through zenpacklib.
These elements are all created through the zenpack.yaml file in the main directory of the ZenPack.
See http://zenpacklib.zenoss.com/en/latest/index.html for more information on zenpacklib.

Note that if templates are changed in the zenpack.yaml file then when the ZenPack is reinstalled, the
existing templates will be renamed in the Zenoss ZODB database and the new template from the YAML file
will be installed; thus a backup is effectively taken.  Old templates should be deleted in the Zenoss GUI
when the new version is proven.

Note that the zenpacklib.py file in the main directory of the ZenPack has been modified slightly. The 
default version places all rrd performance data files directly under a directory named after the device, with 
subdirectories for instances of components. The original ZenPack (and the older standard default behaviour) 
was to create a directory hierarchy with an extra subdirectory for relationships.

    * Old: fred.class.example.org/esxiVm/myVm1/cpuUsage.rrd
    * New: fred.class.example.org/myVm1/cpuUsage.rrd

To be able to preserve performance data, zenpacklib.py has been modified in the rrdPath method to restore 
the old behaviour. If zenpacklib.py is changed or upgraded for any reason, this same change must be made 
to preserve the data paths.


Features
========

Zenoss Device Classes
---------------------

zenpacklib creates */Server/Linux/LogMatch* with:

* zPythonClass: ZenPacks.community.LogMatch.LogMatchDevice
* zCollectorPlugins: ['zenoss.snmp.NewDeviceMap', 'zenoss.snmp.DeviceMap', 'HPDeviceMap', 'DellDeviceMap', 'zenoss.snmp.InterfaceMap', 'zenoss.snmp.RouteMap', 'zenoss.snmp.IpServiceMap', 'zenoss.snmp.HRFileSystemMap', 'zenoss.snmp.HRSWRunMap', 'zenoss.snmp.CpuMap', 'HPCPUMap', 'DellCPUMap', 'DellPCIMap', 'zenoss.snmp.SnmpV3EngineIdMap', 'community.snmp.LogMatchDeviceMap', 'community.snmp.LogMatchMap']


Device and component object classes
-----------------------------------
* LogMatchDevice with new attributes of:

  - versionTag
  - versionDate



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


Monitoring Templates
--------------------

* Component templates

  - LogMatch with an SNMP datasource to gather logMatchCurrentCounter (1.3.6.1.4.1.2021.16.2.1.7) with a GAUGE datapoint
  - LogMatchFile with an SNMP datasource to gather logMatchCurrentCounter (1.3.6.1.4.1.2021.16.2.1.7) with a GAUGE datapoint
    to demonstrate which component template is bound automatically without a monitoring_template keyword.


MIBs
----
* UCD-SNMP-MIB


GUI modifications
-----------------

* The Overview display for a device of object class LogMatchDevice has the SNMP panel
  modified to remove the SNMP community name and to add versionTag and versionDate.
  With zenpacklib, this is achieved by Javascript in resources/LogMatchDevice.js .

Usage
=====


Requirements & Dependencies
===========================

* Zenoss Versions Supported:  4.x
* External Dependencies: 

  - The zenpacklib package that this ZenPack is built on, requires PyYAML.  This is installed as standard with Zenoss 5 and with Zenoss 4 with SP457.
    To test whether it is installed, as the zenoss user, enter the python environment and import yaml::

        python
        import yaml
        yaml

        <module 'yaml' from '/opt/zenoss/lib/python2.7/site-packages/PyYAML-3.11-py2.7-linux-x86_64.egg/yaml/__init__.py'>

    If pyYAML is not installed, install it, as the zenoss user, with::

        easy_install PyYAML

    and then rerun the test above.


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

This ZenPack has been tested against version 5.6.1 of the netSnmp agent.

The SNMP agent on monitored devices must support net-SNMP with the UCD MIB.
To configure an agent, add the following line to snmpd.conf (usually in /etc/snmp). You
will need root privilege::
  logmatch fred1_daily /opt/zenoss/local/fredtest/fred1.log_%Y%m%d 300 test

This will monitor a file under /opt/zenoss/local/fredtest whose name is fred1.log_20160504 
every 5 minutes, looking for lines containing test, where the last part of the filename is
the date in yyyymmdd format.

The snmpd daemon must be restarted before the change will be activated, with::
  service snmpd restart                           or
  /etc/init.d/snmpd restart


To test using snmpwalk for a device zenny1.class.example.org, using SNMP V2 with a community
of public, try::
  snmpwalk -v 2c -c public zenny1.class.example.org 1.3.6.1.4.1.2021.16

After at least 5 minutes, a graph should be produced for each entry with the count of lines
in the specified file containing the specified search string.


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
   - Modified Overview display for LogMatchDevice devices to remove SNMP community and to add 
* 1.0.3
   - Starting from Version 1.0.1, this version converts the ZenPack to using zenpacklib, including the
     device Overview panel.  zenpacklib.py is modified to preserve the original 1.0.1 rrd data paths.


Screenshots
===========

See the screenshots directory.


.. External References Below. Nothing Below This Line Should Be Rendered

.. _Latest Package for Python 2.7: https://github.com/ZenossDevGuide/ZenPacks.community.LogMatch/blob/zenpacklib/dist/ZenPacks.community.LogMatch-1.0.3-py2.7.egg?raw=true

Acknowledgements
================


