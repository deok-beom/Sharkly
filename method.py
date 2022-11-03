from bson.objectid import ObjectId

def guestbook_get(database):
    return list(database.guestbook.find())


def guestbook_post(database, name, comment, password):
    doc = {
        'name': name,
        'comment': comment,
        'password': password
    }
    database.guestbook.insert_one(doc)


def guestbook_patch(database, id, comment, password):
    comment_info = database.guestbook.find_one({'_id': ObjectId(id)})
    if comment_info['password'] == password:
        database.guestbook.update_one({'_id': ObjectId(id)}, {'$set': {'comment': comment}})
        return True
    else:
        return False


def guestbook_delete(database, id, password):
    comment_info = database.guestbook.find_one({'_id': ObjectId(id)})
    if comment_info['password'] == password:
        database.guestbook.delete_one({'_id': ObjectId(id)})
        return True
    else:
        return False

