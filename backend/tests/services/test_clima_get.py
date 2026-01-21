from pathlib import Path
from plone import api
from Products.CMFPlone.Portal import PloneSite

import json
import pytest
import transaction


LOCAL_PATH = Path(__file__).parent


@pytest.fixture(scope="session")
def openmeteo_response():
    raw_data = (LOCAL_PATH / "openmeteo.json").read_text()
    return json.loads(raw_data)


@pytest.fixture
def patch_openmeteo(monkeypatch, openmeteo_response):
    from lactec.intranet.services.clima import openmeteo

    def mockreturn(params):
        return openmeteo_response

    monkeypatch.setattr(openmeteo, "_obtem_dados_open_meteo", mockreturn)


class TestServiceClimaGet:
    portal: PloneSite

    @pytest.fixture(autouse=True)
    def _setup(self, portal, patch_openmeteo):
        self.portal = portal
        with api.env.adopt_roles(["Manager"]):
            self.document = api.content.create(
                container=portal,
                type="Document",
                id="colaboradores",
                title="Pasta de Colaboradores",
            )
        transaction.commit()
        self.endpoint = "/@clima"

    def test_get_status_code(self, manager_request):
        response = manager_request.get(self.endpoint)
        assert response.status_code == 200

    @pytest.mark.parametrize(
        "key,expected",
        [
            ["@id", True],
            ["events", True],
            ["temperature", True],
            ["weather", True],
        ],
    )
    def test_get_keys(self, manager_request, key: str, expected: bool):
        response = manager_request.get(self.endpoint)
        data = response.json()
        assert (key in data) is expected

    def test_fails_anon_user(self, anon_request):
        """Usuário anônimo não deve ter acesso ao serviço de clima."""
        response = anon_request.get(self.endpoint)
        assert response.status_code == 401

    def test_only_accessible_on_root(self, manager_request):
        """Usuário anônimo não deve ter acesso ao serviço de clima."""
        url = f"/colaboradores{self.endpoint}"
        response = manager_request.get(url)
        assert response.status_code == 404
