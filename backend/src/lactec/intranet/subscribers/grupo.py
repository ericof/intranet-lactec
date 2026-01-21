from lactec.intranet import logger
from lactec.intranet.events import IntranetAreaGroupCreatedEvent


def created(event: IntranetAreaGroupCreatedEvent):
    """Handle the IntranetAreaGroupCreatedEvent event."""
    group = event.group
    # Implement your logic here, e.g., logging or additional setup
    logger.info(
        f"Grupo criado: {group.getId()} com título: {group.getProperty('title')}"
    )
