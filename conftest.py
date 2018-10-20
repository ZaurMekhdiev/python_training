# -*- coding: utf-8 -*-
import pytest
from fixture.application_group import Application
from fixture.application_contact import Application


@pytest.fixture(scope = "session")
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture
