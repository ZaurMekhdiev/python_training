# -*- coding: utf-8 -*-
import pytest
from fixture.application_group import Application
from model.group import Group




@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


#=======================================================================================================================
def test_add_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="test", header="test", footer="test"))
    app.logout()

def test_add_empty_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.logout()
