from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('mongodb+srv://baek940dog:sparta@cluster0.jsve0rd.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def home():
    return render_template('main.html')

@app.route('/bsb.html')
def bsb_page():
    return render_template('bsb.html')

@app.route("/bsb", methods=["POST"])
def bsb_guestbook_post():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']
    password_receive = request.form['password_give']

    doc = {
        'name': name_receive,
        'comment': comment_receive,
        'password': password_receive
    }
    db.guestbook.insert_one(doc)
    return jsonify({'msg':"성공"})

@app.route("/bsb", methods=["GET"])
def bsb_guestbook_get():
    guestbook_list = list(db.guestbook.find({}, {'_id':False}))
    return jsonify({'guestbook':guestbook_list})

@app.route("/bsb", methods=["PATCH"])
def bsb_guestbook_patch():
    name_receive = request.form['name_give'].strip()
    comment_receive = request.form['comment_give']
    password_receive = request.form['password_give']

    commentInfo = db.guestbook.find_one({'name': name_receive})
    if commentInfo['password'] == password_receive:
        db.guestbook.update_one({'name': name_receive}, {'$set': {'comment': comment_receive}})
        return jsonify({'msg':"성공"})
    else:
        return jsonify({'msg':"비밀번호가 일치하지 않습니다"})

@app.route("/bsb", methods=["DELETE"])
def bsb_guestbook_delete():
    name_receive = request.form['name_give'].strip()
    password_receive = request.form['password_give']

    commentInfo = db.guestbook.find_one({'name': name_receive})
    if commentInfo['password'] == password_receive:
        db.guestbook.delete_one({'name': name_receive})
        return jsonify({'msg':"성공"})
    else:
        return jsonify({'msg':"비밀번호가 일치하지 않습니다"})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)