from AccessControl import Unauthorized
from lactec.intranet.content.area import Area
from plone import api
from plone.dexterity.fti import DexterityFTI
from zope.component import createObject

import pytest


CONTENT_TYPE = "Area"


@pytest.fixture
def area_payload() -> dict:
    """Return a payload to create a new area."""
    return {
        "type": "Area",
        "id": "ti",
        "title": "Tecnologia da Informação",
        "description": ("Área responsável por TI"),
        "email": "ti@lactec.com.br",
        "telefone": "(61) 3210.1234",
    }


class TestArea:
    @pytest.fixture(autouse=True)
    def _setup(self, get_fti, portal):
        self.fti = get_fti(CONTENT_TYPE)
        self.portal = portal

    def test_fti(self):
        assert isinstance(self.fti, DexterityFTI)

    def test_factory(self):
        factory = self.fti.factory
        obj = createObject(factory)
        assert obj is not None
        assert isinstance(obj, Area)

    @pytest.mark.parametrize(
        "behavior",
        [
            "lactec.intranet.behavior.contato",
            "lactec.intranet.behavior.endereco",
            "plone.basic",
            "plone.constraintypes",
            "plone.excludefromnavigation",
            "plone.namefromtitle",
            "plone.shortname",
            "plone.versioning",
            "volto.blocks",
            "volto.preview_image",
        ],
    )
    def test_has_behavior(self, get_behaviors, behavior):
        assert behavior in get_behaviors(CONTENT_TYPE)

    @pytest.mark.parametrize(
        "role,allowed",
        [
            ["Manager", True],
            ["Site Administrator", True],
            ["Editor", False],
            ["Reviewer", False],
            ["Contributor", False],
            ["Reader", False],
        ],
    )
    def test_create(self, area_payload, role: str, allowed: bool):
        with api.env.adopt_roles([role]):
            if allowed:
                content = api.content.create(container=self.portal, **area_payload)
                assert content.portal_type == CONTENT_TYPE
                assert isinstance(content, Area)
            else:
                with pytest.raises(Unauthorized):
                    api.content.create(container=self.portal, **area_payload)

    def test_subscriber_added_with_description_value(self, area_payload):
        container = self.portal
        with api.env.adopt_roles(["Manager"]):
            area = api.content.create(
                container=container,
                **area_payload,
            )
        assert area.exclude_from_nav is False

    def test_subscriber_added_without_description_value(self, area_payload):
        from copy import deepcopy

        container = self.portal
        with api.env.adopt_roles(["Manager"]):
            payload = deepcopy(area_payload)
            payload["description"] = ""
            area = api.content.create(container=container, **payload)
        assert area.exclude_from_nav is True

    def test_subscriber_added_create_group(self, area_payload):
        container = self.portal
        with api.env.adopt_roles(["Manager"]):
            area = api.content.create(
                container=container,
                **area_payload,
            )
        uid = api.content.get_uuid(area)
        g_id = f"{uid}-editores"
        grupo = api.group.get(g_id)
        assert grupo is not None
        assert grupo.getProperty("title") == f"Área {area.title}: Editores"
        local_roles = api.group.get_roles(group=grupo, obj=area)
        assert "Editor" in local_roles

    def test_subscriber_modified(self, area_payload):
        from zope.event import notify
        from zope.lifecycleevent import ObjectModifiedEvent

        # Criamos normalmente a área, com uma descrição inicial
        container = self.portal
        with api.env.adopt_roles(["Manager"]):
            area = api.content.create(
                container=container,
                **area_payload,
            )
        # Descrição inicial não vazia, exclude_from_nav deve ser False
        assert area.exclude_from_nav is False
        # Agora modificamos a descrição para vazia
        area.description = ""
        # Disparamos o evento de modificação
        notify(ObjectModifiedEvent(area))
        # Agora exclude_from_nav deve ser True
        assert area.exclude_from_nav is True
        # Modificamos a descrição para um valor não vazio
        area.description = "Nova descrição da área"
        # Disparamos o evento de modificação novamente
        notify(ObjectModifiedEvent(area))
        # Agora exclude_from_nav deve ser False novamente
        assert area.exclude_from_nav is False
