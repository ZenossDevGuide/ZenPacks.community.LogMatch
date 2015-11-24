Ext.onReady(function() {
    var DEVICE_SNMP_ID = 'deviceoverviewpanel_snmpsummary';
    Ext.ComponentMgr.onAvailable(DEVICE_SNMP_ID, function(){
        var overview = Ext.getCmp(DEVICE_SNMP_ID);
 
        /* overview.addListener("afterrender", function(){ */
            overview.removeField('snmpCommunity');
 
            overview.addField({
                name: 'versionTag',
                xtype: 'displayfield',
                fieldLabel: _t('Version Tag')
            });
            overview.addField({
                name: 'versionDate',
                xtype: 'displayfield',
                fieldLabel: _t('Version Date')
            });
        /*}); */
    });
});

