from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
import method

app = Flask(__name__)

client_song = MongoClient('mongodb+srv://SongJiEun:tmvkfmxk@cluster0.6burhgx.mongodb.net/?retryWrites=true&w=majority')
db_song = client_song.dbname
client_sung = MongoClient('mongodb+srv://text:sparta@cluster0.csxr5oe.mongodb.net/@cluster0?retryWrites=true&w=majority')
db_sung = client_sung.dbname
client_jeon = MongoClient('mongodb+srv://test:sparta@cluster0.ntm0kz7.mongodb.net/cluster0?retryWrites=true&w=majority')
db_jeon = client_jeon.dbname
client_kim = MongoClient('mongodb+srv://test:sparta@cluster0.rcfiigi.mongodb.net/Cluster0?retryWrites=true&w=majority')
db_kim = client_kim.dbname
client_baek = MongoClient('mongodb+srv://baek940dog:sparta@cluster0.jsve0rd.mongodb.net/Cluster0?retryWrites=true&w=majority')
db_baek = client_baek.dbsparta


@app.route('/')
def home():
    return render_template('main.html')


@app.route('/song')
def song_page():
    return render_template('song.html')


@app.route("/song-api", methods=["POST"])
def song_guestbook_post():
    method.guestbook_post(db_song, request.form['name_give'], request.form['comment_give'], request.form['password_give'])
    return jsonify({'msg': "성공"})


@app.route("/song-api", methods=["GET"])
def song_guestbook_get():
    guestbook_list = method.guestbook_get(db_song)
    return jsonify({'guestbook': guestbook_list})


@app.route("/song-api", methods=["PATCH"])
def song_guestbook_patch():
    b_Success = method.guestbook_patch(db_song, request.form['name_give'].strip(), request.form['comment_give'], request.form['password_give'])
    return jsonify({'success': b_Success})


@app.route("/song-api", methods=["DELETE"])
def song_guestbook_delete():
    b_Success = method.guestbook_delete(db_song, request.form['name_give'].strip(), request.form['password_give'])
    return jsonify({'success': b_Success})

@app.route('/sung')
def sung_page():
    return render_template('sung.html')


@app.route("/sung-api", methods=["POST"])
def sung_guestbook_post():
    method.guestbook_post(db_sung, request.form['name_give'], request.form['comment_give'], request.form['password_give'])
    return jsonify({'msg': "성공"})


@app.route("/sung-api", methods=["GET"])
def sung_guestbook_get():
    guestbook_list = method.guestbook_get(db_sung)
    return jsonify({'guestbook': guestbook_list})


@app.route("/sung-api", methods=["PATCH"])
def sung_guestbook_patch():
    b_Success = method.guestbook_patch(db_sung, request.form['name_give'].strip(), request.form['comment_give'], request.form['password_give'])
    return jsonify({'success': b_Success})


@app.route("/sung-api", methods=["DELETE"])
def sung_guestbook_delete():
    b_Success = method.guestbook_delete(db_sung, request.form['name_give'].strip(), request.form['password_give'])
    return jsonify({'success': b_Success})

@app.route('/jeon')
def jeon_page():
    return render_template('jeon.html')


@app.route("/jeon-api", methods=["POST"])
def jeon_guestbook_post():
    method.guestbook_post(db_jeon, request.form['name_give'], request.form['comment_give'], request.form['password_give'])
    return jsonify({'msg': "성공"})


@app.route("/jeon-api", methods=["GET"])
def jeon_guestbook_get():
    guestbook_list = method.guestbook_get(db_jeon)
    return jsonify({'guestbook': guestbook_list})


@app.route("/jeon-api", methods=["PATCH"])
def jeon_guestbook_patch():
    b_Success = method.guestbook_patch(db_jeon, request.form['name_give'].strip(), request.form['comment_give'], request.form['password_give'])
    return jsonify({'success': b_Success})


@app.route("/jeon-api", methods=["DELETE"])
def jeon_guestbook_delete():
    b_Success = method.guestbook_delete(db_jeon, request.form['name_give'].strip(), request.form['password_give'])
    return jsonify({'success': b_Success})

@app.route('/kim')
def kim_page():
    return render_template('kim.html')


@app.route("/kim-api", methods=["POST"])
def kim_guestbook_post():
    method.guestbook_post(db_kim, request.form['name_give'], request.form['comment_give'], request.form['password_give'])
    return jsonify({'msg': "성공"})


@app.route("/kim-api", methods=["GET"])
def kim_guestbook_get():
    guestbook_list = method.guestbook_get(db_kim)
    return jsonify({'guestbook': guestbook_list})


@app.route("/kim-api", methods=["PATCH"])
def kim_guestbook_patch():
    b_Success = method.guestbook_patch(db_kim, request.form['name_give'].strip(), request.form['comment_give'], request.form['password_give'])
    return jsonify({'success': b_Success})


@app.route("/kim-api", methods=["DELETE"])
def kim_guestbook_delete():
    b_Success = method.guestbook_delete(db_kim, request.form['name_give'].strip(), request.form['password_give'])
    return jsonify({'success': b_Success})

@app.route('/baek')
def baek_page():
    return render_template('baek.html')


@app.route("/baek-api", methods=["POST"])
def baek_guestbook_post():
    method.guestbook_post(db_baek, request.form['name_give'], request.form['comment_give'], request.form['password_give'])
    return jsonify({'msg': "성공"})


@app.route("/baek-api", methods=["GET"])
def baek_guestbook_get():
    guestbook_list = method.guestbook_get(db_baek)
    return jsonify({'guestbook': guestbook_list})


@app.route("/baek-api", methods=["PATCH"])
def baek_guestbook_patch():
    b_Success = method.guestbook_patch(db_baek, request.form['name_give'].strip(), request.form['comment_give'], request.form['password_give'])
    return jsonify({'success': b_Success})


@app.route("/baek-api", methods=["DELETE"])
def baek_guestbook_delete():
    b_Success = method.guestbook_delete(db_baek, request.form['name_give'].strip(), request.form['password_give'])
    return jsonify({'success': b_Success})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
