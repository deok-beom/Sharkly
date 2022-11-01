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
def guestbook_post():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']

    doc = {
        'name': name_receive,
        'comment': comment_receive
    }
    db.guestbook.insert_one(doc)

    return jsonify({'msg':'댓글 남기기 완료!'})

@app.route("/bsb", methods=["GET"])
def guestbook_get():
    guestbook_list = list(db.guestbook.find({}, {'_id':False}))
    return jsonify({'guestbook':guestbook_list})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)