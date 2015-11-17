from Products.ZenModel.Device import Device
from Products.ZenRelations.RelSchema import ToManyCont, ToOne


class LogMatchDevice(Device):
    """
    LogMatch device subclass. In this case the reason for creating a subclass of
    device is to add a new type of relation. We want many "LogMatch"
    components to be associated with each of these devices.

    If you set the zPythonClass of a device class to
    ZenPacks.community.LogMatch.LogMatchDevice, any devices created or moved
    into that device class will become this class and be able to contain
    LogMatch components.
    """

    meta_type = portal_type = 'LogMatchDevice'

    #**************Custom data Variables here from modeling************************

    versionTag = ''
    versionDate = ''

    #**************END CUSTOM VARIABLES *****************************
    #*************  Those should match this list below *******************
    _properties = Device._properties + (
        {'id':'versionTag', 'type':'string', 'mode':''},
        {'id':'versionDate', 'type':'string', 'mode':''},
        )
    #****************

    # This is where we extend the standard relationships of a device to add
    # our "logMatchs" relationship that must be filled with components
    # of our custom "LogMatch" class.
    # ZenPacks.community.LogMatch.LogMatch.LogMatch (starting from the right) is the
    #  LogMatch class in the LogMatch file (strictly module) in the ZenPacks.community.LogMatch ZenPack
    _relations = Device._relations + (
        ('logMatchs', ToManyCont(ToOne,
            'ZenPacks.community.LogMatch.LogMatch.LogMatch',
            'logMatchDevice',
            ),
        ),
    )
