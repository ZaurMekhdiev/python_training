from model.contact import Contact


def test_modify_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify(Contact(firstname="test333", middlename="test333", lastname="test333", address="test333",
                               email="test333"))
    app.session.logout()