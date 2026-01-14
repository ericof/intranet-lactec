from lactec.intranet import _
from plone.autoform import directives
from plone.dexterity.content import Container
from plone.supermodel import model
from z3c.relationfield.schema import RelationChoice
from zope import schema
from zope.interface import implementer


class IPessoa(model.Schema):
    """Definição de uma Pessoa."""

    cargo = schema.Choice(
        title=_("Cargo"),
        vocabulary="lactec.intranet.vocabulary.cargos",
        required=False,
    )

    area = RelationChoice(
        title="Área", required=False, vocabulary="lactec.intranet.vocabulary.areas"
    )
    directives.widget(
        "area",
        frontendOptions={
            "widget": "select",
        },
    )


@implementer(IPessoa)
class Pessoa(Container):
    """Uma Pessoa no Lactec."""
