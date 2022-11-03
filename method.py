def guestbook_get(database):
    return list(database.guestbook.find({}))


def guestbook_post(database, name, comment, password):
    name_receive = name
    comment_receive = comment
    password_receive = password

    doc = {
        'name': name_receive,
        'comment': comment_receive,
        'password': password_receive
    }
    database.guestbook.insert_one(doc)


def guestbook_patch(database, name, comment, password):
    name_receive = name
    comment_receive = comment
    password_receive = password

    comment_info = database.guestbook.find_one({'name': name_receive})
    if comment_info['password'] == password_receive:
        database.guestbook.update_one({'name': name_receive}, {'$set': {'comment': comment_receive}})
        return True
    else:
        return False


def guestbook_delete(database, name, password):
    name_receive = name
    password_receive = password

    comment_info = database.guestbook.find_one({'name': name_receive})
    if comment_info['password'] == password_receive:
        database.guestbook.delete_one({'name': name_receive})
        return True
    else:
        return False

