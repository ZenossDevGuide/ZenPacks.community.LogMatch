# Module-level documentation will automatically be shown as additional
# information for the modeler plugin in the web interface.
"""
LogMatchDeviceMap
An SNMP plugin that gathers data for LogMatch components.
"""

# When configuring modeler plugins for a device or device class, this plugin's
# name would be community.snmp.LogMatchDeviceMap because its filesystem path within
# the ZenPack is modeler/plugins/community/snmp/LogMatchDeviceMap.py. The name of the
# class within this file MUST - repeat MUST -  match the filename.

# SnmpPlugin is the base class that provides lots of help in modeling data
# that's available over SNMP.
from Products.DataCollector.plugins.CollectorPlugin import SnmpPlugin, GetMap

class LogMatchDeviceMap(SnmpPlugin):

    snmpGetMap = GetMap({
        '.1.3.6.1.4.1.2021.100.2.0': 'versionTag',
        '.1.3.6.1.4.1.2021.100.3.0': 'versionDate',
        })

    def process(self, device, results, log):
        log.info("Modeler %s processing data for device %s",
            self.name(), device.id)

        # Results is a tuple with two items. The first (0) index contains a
        # dictionary with the results of the "snmpGetMap" queries. The second
        # (1) index contains a dictionary with the results of the
        # "snmpGetTableMaps" queries.
        # NB. For this modeler, table is null
        getdata, tabledata = results

        # getdata contents. Note the empty dictionary at the end repesenting no tabledata
        # results = ({'.1.3.6.1.4.1.2021.100.3.0': '$Date: 2010-01-24 09:41:03 -0200 (Sun, 24 Jan 2010) $', '.1.3.6.1.4.1.2021.100.2.0': '5.6.1'}, {})

        # if no getdata then return logging a warning
        if not getdata:
            log.warn( 'No SNMP response from %s for the %s plugin ', device.id, self.name() )
            log.warn( "Get Data= %s", tabledata )
            return
        # Populate the device attributes versionTag and versionDate with the matching values
        #   retrieved in the getdata dictionary.

        om = self.objectMap(getdata)
        return om

