from lactec.intranet import logger
from lactec.intranet.services.clima import openmeteo
from plone import api
from plone.restapi.services import Service


class ClimaGet(Service):
    @property
    def coordinates(self) -> tuple:
        """Retorna latitude e longitude da Lactec."""
        return (-25.426272575902576, -49.267394509700075)

    @property
    def timezone(self) -> str:
        return api.portal.get_registry_record("plone.portal_timezone")

    def reply(self):
        portal = api.portal.get()
        portal_url = portal.absolute_url()
        latitude, longitude = self.coordinates
        timezone = self.timezone
        logger.info("Acessa dados do clima")
        dados = openmeteo.dados_clima(latitude, longitude, timezone)
        dados["@id"] = f"{portal_url}/@clima"
        logger.info("Retorna dados do clima")
        return dados
