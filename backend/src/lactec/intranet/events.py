from lactec.intranet.interfaces import IIntranetAreaGroupCreatedEvent
from zope.interface import implementer


@implementer(IIntranetAreaGroupCreatedEvent)
class IntranetAreaGroupCreatedEvent:
    """Event triggered when a new intranet area group is created."""

    def __init__(self, group):
        """Initialize the event with the created group.

        :param group: The created group object.
        """
        self.group = group
