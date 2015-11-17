from Products.ZenModel.DeviceComponent import DeviceComponent
from Products.ZenModel.ManagedEntity import ManagedEntity
from Products.ZenModel.ZenossSecurity import ZEN_CHANGE_DEVICE
from Products.ZenRelations.RelSchema import ToManyCont, ToOne

class LogMatch(DeviceComponent, ManagedEntity):
    meta_type = portal_type = "LogMatch"

    #**************Custom data Variables here from modeling************************
    logMatchName = ''
    logMatchFilename = ''
    logMatchRegEx = ''
    logMatchCycle = 300
    logMatchErrorFlag = 0
    logMatchRegExCompilation = ''
    #**************END CUSTOM VARIABLES *****************************
    #*************  Those should match this list below *******************
    _properties = ManagedEntity._properties + (
        {'id': 'logMatchName', 'type': 'string', 'mode': ''},
        {'id': 'logMatchFilename', 'type': 'string', 'mode': ''},
        {'id': 'logMatchRegEx', 'type': 'string', 'mode': ''},
        {'id': 'logMatchCycle', 'type': 'int', 'mode': ''},
        {'id': 'logMatchErrorFlag', 'type': 'int', 'mode': ''},
        {'id': 'logMatchRegExCompilation', 'type': 'string', 'mode': ''},
    )
    #****************

    _relations = ManagedEntity._relations + (
        ('logMatchDevice', ToOne(ToManyCont,
            'ZenPacks.community.LogMatch.LogMatchDevice.LogMatchDevice',
            'logMatchs',
            ),
        ),
    )

    # Custom components must always implement the device method. The method
    # should return the device object that contains the component.
    #    ie. follow the logMatchDevice relationship
    def device(self):
        return self.logMatchDevice()

    # Defining the "perfConf" action here causes the "Graphs" display to be
    # available for components of this type.
    #factory_type_information = ({
    #    'actions': ({
    #        'id': 'perfConf',
    #        'name': 'Template',
    #        'action': 'objTemplates',
    #        'permissions': (ZEN_CHANGE_DEVICE,),
    #    },),
    #},)

