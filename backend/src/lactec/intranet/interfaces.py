"""Module where all interfaces, events and exceptions live."""

from zope.interface import Interface
from zope.publisher.interfaces.browser import IDefaultBrowserLayer


class IBrowserLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


class IIntranetEvent(Interface):
    """Interface for intranet events."""


class IIntranetAreaGroupCreatedEvent(IIntranetEvent):
    """Event triggered when a new intranet area group is created."""

    def __init__(self, group):
        """Initialize the event with the created group.

        :param group: The created group object.
        """
