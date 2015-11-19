/*
 * Based on the configuration in ../../configure.zcml this JavaScript will only
 * be loaded when the user is looking at a Device in the web interface.
 */

(function(){

var ZC = Ext.ns('Zenoss.component');

/*
 * Custom component grid panel. This controls the grid that gets displayed for
 * components of the type set in "componenType".
 * Note that the sample Ext.define('Zenoss.component.ExampleComponentGridPanel'    ),
 *     IS WRONG!!!! It should be
 *     Zenoss.component.ExampleComponentPanel         no "Grid" in this name
 *     The       extend: 'Zenoss.component.ComponentGridPanel',       IS CORRECT
 */
ZC.LogMatchPanel = Ext.extend(ZC.ComponentGridPanel, {
    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
            autoExpandColumn: 'logMatchFilename',
            componentType: 'LogMatch',
            sortInfo: {
                field: 'logMatchName',
                direction: 'ASC'
            },
            fields: [
                {name: 'uid'},
                {name: 'name'},
                {name: 'severity'},
                {name: 'logMatchName'},
                {name: 'logMatchFilename'},
                {name: 'logMatchRegEx'},
                {name: 'logMatchCycle'},
                {name: 'logMatchErrorFlag'},
                {name: 'logMatchRegExCompilation'},
                {name: 'locking'},
                {name: 'snmpindexblah'},
                {name: 'usesMonitorAttribute'},
                {name: 'monitor'},
                {name: 'monitored'}
            ],
            columns: [{
                id: 'severity',
                dataIndex: 'severity',
                header: _t('Events'),
                renderer: Zenoss.render.severity,
                sortable: true,
                width: 50
            },{
                id: 'logMatchName',
                dataIndex: 'logMatchName',
                header: _t('LogMatch Name'),
                sortable: true,
                width: 100
            },{
                id: 'logMatchFilename',
                flex: 1,
                dataIndex: 'logMatchFilename',
                header: _t('LogMatch File Name'),
                sortable: true,
                width: 400
            },{
                id: 'logMatchRegEx',
                dataIndex: 'logMatchRegEx',
                header: _t('LogMatch RegEx'),
                sortable: true,
                width: 200
            },{
                id: 'logMatchErrorFlag',
                dataIndex: 'logMatchErrorFlag',
                header: _t('LogMatch Errors'),
                sortable: true,
                width: 100
            },{
                id: 'monitored',
                dataIndex: 'monitored',
                header: _t('Monitored'),
                renderer: Zenoss.render.checkbox,
                sortable: true,
                width: 65
            },{
                id: 'locking',
                dataIndex: 'locking',
                header: _t('Locking'),
                renderer: Zenoss.render.locking_icons,
                width: 65
            },{
                id: 'snmpindexblahblah',
                dataIndex: 'snmpindexblah',
                header: _t('SNMP Index'),
                sortable: true,
                width: 70
            }]
        });
        ZC.LogMatchPanel.superclass.constructor.call(this, config);
    }
});

Ext.reg('LogMatchPanel', ZC.LogMatchPanel);

/*
 * Friendly names for the components. First parameter is the meta_type in your
 * custom component class. Second parameter is the singular form of the
 * friendly name to be displayed in the UI. Third parameter is the plural form.
 */

ZC.registerName('LogMatch', _t('Log Match File'), _t('Log Match Files'));


})();
