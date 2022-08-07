from flask import Flask, render_template, request
import nltk
from nltk.chat.util import Chat
app = Flask(__name__)



qa_pairs = [ ['(hi|HI|Hi|Hey|hey)',['hello']],
             ['(.*)name',['my name is upbot']],
             ['what is your favourite food',['sorry i can not eat']],
             ['what is your age',['I am two years old']],
             ['tell something',['Feeling good']],
             ['what are you learning',['Learning NLP']],
             ['Success rate',['100 percent']],
             ['Hobbies',['playing']],
             ['current job',['student']],
             ['how are you',['fine']]
          ]
cb = Chat(qa_pairs)
@app.route("/", methods = ["GET","POST"])
def chatbot_responses():
  response = ''
  if request.method == 'POST':
    msg = request.form['message']
    response = cb.respond(msg)
  return render_template("index.html",response1 = response)
if __name__ == "__main__":
  app.run(debug=True)