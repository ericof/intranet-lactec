from lactec.intranet import _
from plone.dexterity.content import Container
from plone.supermodel import model
from zope import schema
from zope.interface import implementer


class IPessoa(model.Schema):
    """Definição de uma Pessoa."""

    cargo = schema.Choice(
        title=_("Cargo"),
        vocabulary="lactec.intranet.vocabulary.cargos",
        required=False,
    )


@implementer(IPessoa)
class Pessoa(Container):
    """Uma Pessoa no Lactec."""
