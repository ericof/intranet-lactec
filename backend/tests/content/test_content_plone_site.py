from AccessControl.users import nobody
from plone import api
from plone.dexterity.fti import DexterityFTI

import pytest


CONTENT_TYPE = "Plone Site"


class TestPloneSite:
    @pytest.fixture(autouse=True)
    def _setup(self, get_fti, portal):
        self.fti = get_fti(CONTENT_TYPE)
        self.portal = portal

    def test_fti(self):
        assert isinstance(self.fti, DexterityFTI)

    @pytest.mark.parametrize(
        "behavior",
        [
            "voltolighttheme.header",
            "voltolighttheme.theme",
            "voltolighttheme.footer",
            "plonegovbr.socialmedia.settings",
            "volto.preview_image_link",
            "plone.dublincore",
            "plone.relateditems",
            "plone.locking",
            "plone.excludefromnavigation",
            "volto.blocks",
        ],
    )
    def test_has_behavior(self, get_behaviors, behavior):
        assert behavior in get_behaviors(CONTENT_TYPE)


class TestPloneSiteContent:
    """Testa que o Plone Site está configurado corretamente."""

    def test_workflow_state(self, portal):
        """Validar se o estado de workflow está correto."""
        expected = "internal"
        # Obtem estado de workflow do Plone Site
        value = api.content.get_state(portal)
        assert value == expected, (
            f"Estado de workflow é {value}, esperávamos {expected}"
        )

    @pytest.mark.parametrize(
        "permission,expected",
        [
            ["Access contents information", False],
            ["Modify portal content", False],
            ["View", False],
        ],
    )
    def test_anonymous_permissions(self, portal, permission: str, expected: bool):
        with api.env.adopt_user(user=nobody):
            user = api.user.get_current()
            has_permission = api.user.has_permission(permission, user=user, obj=portal)
            assert has_permission is expected, (
                f"Erro: Permissão {permission} para usuário Anônimo: {has_permission}"
            )
