# -*- coding: utf-8 -*-
import pytest
from fixture.application_contacts import Application
from model.contact import Contact

@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

# =====================================================================================================================f

def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(firstname="test1", middlename="test2", lastname="test3", address="test4", email="test5")
    app.session.logout()


def test_add_empty_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(firstname="", middlename="", lastname="", address="", email="")
    app.session.logout()






