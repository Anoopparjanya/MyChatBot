from flask import Flask, request, send_from_directory, redirect, render_template, flash, url_for, jsonify, \
    make_response, abort

from Anoop_word_seq2seq_glove_predict import AnoopWordGloveChatBot



app = Flask(__name__)
app.config.from_object(__name__)  # load config from this file , flaskr.py

# Load default config and override config from an environment variable
app.config.from_envvar('FLASKR_SETTINGS', silent=True)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

Anoop_word_glove_chat_bot = AnoopWordGloveChatBot()


Anoop_word_glove_chat_bot_conversations = []



@app.route('/')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return 'About Us'


@app.route('/Anoop_word_glove_reply', methods=['POST', 'GET'])
def Anoop_word_glove_reply():
    if request.method == 'POST':
        if 'sentence' not in request.form:
            flash('No sentence post')
            redirect(request.url)
        elif request.form['sentence'] == '':
            flash('No sentence')
            redirect(request.url)
        else:
            sent = request.form['sentence']
            Anoop_word_glove_chat_bot_conversations.append('YOU: ' + sent)
            reply = Anoop_word_glove_chat_bot.reply(sent)
            Anoop_word_glove_chat_bot_conversations.append('BOT: ' + reply)
    return render_template('Anoop_word_glove_reply.html', conversations=Anoop_word_glove_chat_bot_conversations)



    target_text = sentence
    if level == 'word-glove' and dialogs == 'Anoop':
        target_text = Anoop_word_glove_chat_bot.reply(sentence)
    
    return jsonify({
        'sentence': sentence,
        'reply': target_text,
        'dialogs': dialogs,
        'level': level
    })


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


def main():
   
    Anoop_word_glove_chat_bot.test_run()
   
    app.run(debug=True, use_reloader=False)

if __name__ == '__main__':
    main()
