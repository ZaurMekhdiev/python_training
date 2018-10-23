from model.group import Group


def test_modify_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modify(Group(name="test333", header="test333", footer="test333"))
    app.session.logout()