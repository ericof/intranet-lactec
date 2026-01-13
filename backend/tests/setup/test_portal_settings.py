"""Portal settings tests."""

from plone import api

import pytest


class TestPortalSettings:
    """Test that Portal configuration is correctly done."""

    @pytest.mark.parametrize(
        "key,expected",
        [
            ("plone.site_title", "Intranet da Lactec"),
            ("plone.email_from_name", "Intranet da Lactec"),
            ("plone.smtp_host", "localhost"),
            ("plone.smtp_port", 25),
            ("plone.available_timezones", ["America/Sao_Paulo"]),
            ("plone.portal_timezone", "America/Sao_Paulo"),
            ("plone.first_weekday", 6),
            ("plone.navigation_depth", 4),
            ("plone.twitter_username", "plone"),
            ("plone.available_languages", ["pt-br"]),
            ("plone.default_language", "pt-br"),
        ],
    )
    def test_setting(self, portal, key: str, expected: str | int | list[str]):
        """Test registry setting."""
        value = api.portal.get_registry_record(key)
        assert value == expected
