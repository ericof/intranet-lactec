from lactec.intranet import logger
from lactec.intranet.content.area import Area
from plone import api
from Products.PlonePAS.tools.groupdata import GroupData
from zope.lifecycleevent import ObjectAddedEvent


def _update_excluded_from_nav(obj: Area):
    """Update excluded_from_nav in the Area object."""
    description = obj.description
    obj.exclude_from_nav = not bool(description)
    logger.info(f"Atualizado o campo excluded_from_nav para {obj.title}")


def _cria_grupo_usuarios(obj: Area):
    """Cria um grupo de usuários para a nova área."""
    uid = api.content.get_uuid(obj)
    g_id = f"{uid}-editores"
    titulo = f"Área {obj.title}: Editores"
    payload = {
        "groupname": g_id,
        "title": titulo,
        "description": f"Grupo de editores da área {obj.title}",
    }
    grupo: GroupData = api.group.create(**payload)
    logger.info(f"Criado o grupo {titulo} para a área {obj.title}")
    api.group.grant_roles(group=grupo, roles=["Editor"], obj=obj)
    logger.info(f"Grupo {titulo} recebeu papel de editor em {obj.absolute_url()}")


def added(obj: Area, event: ObjectAddedEvent):
    """Post creation handler for Area."""
    _update_excluded_from_nav(obj)
    _cria_grupo_usuarios(obj)
