from Products.ZenModel.DeviceComponent import DeviceComponent
from Products.ZenModel.ManagedEntity import ManagedEntity
from Products.ZenModel.OSComponent import OSComponent
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

    # The logMatchs relationship does not exist in the default Products.ZenModel.OperatingSystem
    # It is monkey-patched in the __init__.py of this zenpack
    _relations = OSComponent._relations + (
        ('os', ToOne(ToManyCont,
            'Products.ZenModel.OperatingSystem', 'logMatchs')),
    )

    #_relations = ManagedEntity._relations + (
    #    ('logMatchDevice', ToOne(ToManyCont,
    #        'ZenPacks.community.LogMatch.LogMatchDevice.LogMatchDevice',
    #        'logMatchs',
    #        ),
    #    ),
    #)

    # Custom components must always implement the device method. The method
    # should return the device object that contains the component.
    #    ie. follow the logMatchDevice relationship
    #def device(self):
    #    return self.logMatchDevice()

    def device(self):
        os = self.os()
        if os: return os.device()


