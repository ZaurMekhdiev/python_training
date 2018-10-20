# -*- coding: utf-8 -*-
import pytest
from application_contacts import Application
from contact import Contact





@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


#=======================================================================================================================
def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(firstname="test1", middlename="test2", lastname="test3", address="test4", email="test5")
    app.logout()

def test_add_empty_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(firstname="", middlename="", lastname="", address="", email="")
    app.logout()






