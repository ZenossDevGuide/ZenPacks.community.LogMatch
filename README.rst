============================
ZenPacks.community.LogMatch
============================


Description
===========
This ZenPack monitors logfiles using SNMP capabilities from the netSnmp UCD agent.

This version of the ZenPack uses zenpacklib.

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



Features
========

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

Screenshots
===========

See the screenshots directory.


.. External References Below. Nothing Below This Line Should Be Rendered

.. _Latest Package for Python 2.7: https://github.com/ZenossDevGuide/ZenPacks.community.LogMatch/blob/master/dist/ZenPacks.community.LogMatch-1.0.1-py2.7.egg?raw=true

Acknowledgements
================


