# Module-level documentation will automatically be shown as additional
# information for the modeler plugin in the web interface.
"""
LogMatchMap
An SNMP plugin that gathers data for LogMatch components.
"""

# When configuring modeler plugins for a device or device class, this plugin's
# name would be community.snmp.LogMatchMap because its filesystem path within
# the ZenPack is modeler/plugins/community/snmp/LogMatchMap.py. The name of the
# class within this file MUST - repeat MUST -  match the filename.

# SnmpPlugin is the base class that provides lots of help in modeling data
# that's available over SNMP.
from Products.DataCollector.plugins.CollectorPlugin import SnmpPlugin, GetTableMap

class LogMatchMap(SnmpPlugin):

    # Strictly it is a DEVICE that is being queried for SNMP data so we need to
    #   specify the relationship on the device that this modeler is going to populate
    # We also need to specify the full module path that specifies the component object
    #   that we want to instantiate.

    relname = "logMatchs"
    modname = "ZenPacks.community.LogMatch.LogMatch"

    # snmpGetTableMaps and GetTableMap should be used to request SNMP tables.
    # The parameters are:
    #     1) The name of the structure that you want to store the results in.
    #         This can be anything but, by convention, is the name of the MIB table
    #     2) The base OID for the table. The "entry" OID or more specifically the 
    #       largest possible OID prefix that doesn't change when walking the table. 
    #     3) A dictionary that maps columns in the table to names that will be used 
    #          to access them in the results. These names should exactly match the
    #          attributes of the LogMatch component.
    snmpGetTableMaps = (
        GetTableMap('logMatchTable', 
                    '.1.3.6.1.4.1.2021.16.2.1', 
                    {
                        '.1': '_logMatchIndex',
                        '.2': 'logMatchName',
                        '.3': 'logMatchFilename',
                        '.4': 'logMatchRegEx',
                        '.11': 'logMatchCycle',
                        '.100': 'logMatchErrorFlag',
                        '.101': 'logMatchRegExCompilation',
                    }
            ),

        # More GetTableMap definitions can be added to this tuple to query
        # more SNMP tables.
        )

    def process(self, device, results, log):
        log.info("Modeler %s processing data for device %s",
            self.name(), device.id)

        # Results is a tuple with two items. The first (0) index contains a
        # dictionary with the results of the "snmpGetMap" queries. The second
        # (1) index contains a dictionary with the results of the
        # "snmpGetTableMaps" queries.
        # NB. For this modeler, getdata is null
        getdata, tabledata = results

        # tabledata contents..
        # {'logMatchTable': {'1': 
        #          {'logMatchRegExCompilation': 'Success', 'logMatchRegEx': 'test', 
        #         'logMatchCycle': 300, 'logMatchErrorFlag': 0, 'logMatchName': 'fred1_daily', 
        #         'logMatchFilename': '/opt/zenoss/local/fredtest/fred1.log_20151110', 
        #         'logMatchIndex': 1},
        #     '2':
        #          {'logMatchRegExCompilation': 'Success', 'logMatchRegEx': 'without', 
        #         'logMatchCycle': 180, 'logMatchErrorFlag': 0, 'logMatchName': 'fred2_daily', 
        #         'logMatchFilename': '/opt/zenoss/local/fredtest/fred2.log_20151110', 
        #         'logMatchIndex': 1},
        # } }

        # tabledata may have several dictionaries of tables; we want the logMatchTable dict
        logMatchTable = tabledata.get('logMatchTable')
        log.debug('logMatchTable is %s ' % (logMatchTable))
        # if no tabledata then return logging a warning
        if not logMatchTable:
            log.warn( 'No SNMP response from %s for the %s plugin ', device.id, self.name() )
            log.warn( "Table Data= %s", tabledata )
            return

        # Create a relationship map - relname above specifies the logMatch relationship
        rm = self.relMap()
        # For each entry in the SNMP table, we need to create a LogMatch component
        for oid, data in logMatchTable.items():
            # Use try / except to prevent nasty failures
            try:
                # Next line instantiates a LogMatch component object, populating the
                #   component object's attributes with the matching values from the LogMatchTable
                #   logMatchName, logMatchFilename, etc
                #   modname (specified above) defines the object class for the component
                om = self.objectMap(data)
                # Any attribute can then be overwritten, if required.  id is an inherited 
                #   attribute but we want to ensure uniqueness
                om.id = self.prepId(om.logMatchName)
                # snmpindex is also an inherited attribute. Set it to the index
                om.snmpindex = oid
                # Append this object instance to the relationship map 
                rm.append(om)
            # If something goes wrong, fail nicely with a logged warning and then
            #   continue aroound the loop again
            except (KeyError, IndexError, AttributeError, TypeError), errorInfo:
                log.warn( ' Error in %s modeler plugin %s' % ( self.name(), errorInfo))
                continue
        return rm

        # The process method of the modeler plugin class below is expected to
        # return output in one of the following forms.
        #
        #   1. A single ObjectMap instance
        #   2. A single RelationshipMap instance
        #   3. A list of ObjectMap and RelationshipMap instances
        #   4. None
        #
        # If your modeler plugin encounters a bad state and you don't want to
        # affect Zenoss' model of the device you should return None.
