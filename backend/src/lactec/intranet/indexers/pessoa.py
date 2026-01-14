from lactec.intranet.content.pessoa import IPessoa
from lactec.intranet.content.pessoa import Pessoa
from plone import api
from plone.indexer import indexer
from z3c.relationfield.relation import RelationValue


@indexer(IPessoa)
def area_indexer(obj: Pessoa) -> str | None:
    """Retorna o UUID da área de uma Pessoa, se ela estiver definida."""
    area_rel: RelationValue | None = obj.area
    if area_rel:
        area = area_rel.to_object
        uuid: str = api.content.get_uuid(area)
        return uuid


@indexer(IPessoa)
def cargo_indexer(obj: Pessoa) -> str | None:
    """Retorna o cargo de uma Pessoa, se ele estiver definido."""
    return obj.cargo if obj.cargo else None
