from flask import Flask, render_template, url_for, request, redirect,flash,session, Response, jsonify

secret_key = 'th!5!5r@nd0mk3y'

app = Flask(__name__)

#Remember to keep the empty spaces as ' ' and not '' or the program will not work

app.secret_key = secret_key

matrix = [[' ',' ',' ',' ',' ',' ',' '],
          [' ','p','i','n',' ',' ',' '],
          [' ','a',' ','p','e','a','k'],
          [' ','a',' ','c',' ',' ',' '],
          [' ','a','c','b','d','e',' '],
          [' ','c',' ',' ','r',' ',' '],
          [' ','b',' ',' ','p',' ',' ']]


# Enter the original answers to the questions here

# Across answers
playerlist={}
user_matrices = []
original_answer1 = 'pin'
original_answer2 = 'peak'
original_answer3 = ''

# Down answers

original_answer4 = ''
original_answer5 = ''
original_answer6 = ''
question1 = ''
question2 = ''
question3 = ''
question4 = ''
question5 = ''
question6 = ''

key = False
def start_pos_across(word,direction):
    if direction == "across":
        for i in range(len(matrix)):
            for j in range(len(matrix[0]) - len(word) + 1):
                if all(matrix[i][j + k] == " " or matrix[i][j + k] == word[k] for k in range(len(word))):
                    return i+1, j+1
    elif direction == "down":
        for i in range(len(matrix) - len(word) + 1):
            for j in range(len(matrix[0])):
                if all(matrix[i + k][j] == " " or matrix[i + k][j] == word[k] for k in range(len(word))):
                    return i, j
@app.route('/crossword', methods=['GET', 'POST'])
def home():
    if 'username' in session:
        print(playerlist)
        print(session['username'])
        user_matrix = [[' ',' ',' ',' ',' ',' ',' '],
                [' ',' ',' ',' ',' ',' ',' '],
                [' ',' ',' ',' ',' ',' ',' '],
                [' ',' ',' ',' ',' ',' ',' '],
                [' ',' ',' ',' ',' ',' ',' '],
                [' ',' ',' ',' ',' ',' ',' '],
                [' ',' ',' ',' ',' ',' ',' ']]
        if request.method == 'POST':
            print(request.json)
            if request.json['answer1'] != '':
                answer1 = request.json['answer1']
                print(answer1)
                if answer1 == original_answer1:
                    start_i, start_j = start_pos_across(answer1,"across")
                    for idx, char in enumerate(answer1):
                        user_matrix[start_i][start_j + idx] = char
                        matrix[start_i][start_j + idx] = char
            if request.json['answer2'] != '':
                answer2 = request.json['answer2']
                print(answer2)
                if answer2 == original_answer2:
                    start_i, start_j = start_pos_across(answer2,"across")
                    for idx, char in enumerate(answer2):
                        user_matrix[start_i][start_j + idx] = char
                        matrix[start_i][start_j + idx] = char
            if request.json['answer3'] != '':
                answer3 = request.json['answer3']
                print(answer3)
                if answer3 == original_answer3:
                    start_i, start_j = start_pos_across(answer3,"across")
                    for idx, char in enumerate(answer3):
                        user_matrix[start_i][start_j + idx] = char
                        matrix[start_i][start_j + idx] = char
            if request.json['answer4'] != '':
                answer4 = request.json['answer4']
                print(answer4)
                if answer4 == original_answer4:
                    start_i, start_j = start_pos_across(answer4,"down")
                    for idx, char in enumerate(answer4):
                        user_matrix[start_i][start_j + idx] = char
                        matrix[start_i][start_j + idx] = char
            if request.json['answer5'] != '':
                answer5 = request.json['answer5']
                print(answer5)
                if answer5 == original_answer5:
                    start_i, start_j = start_pos_across(answer5,"down")
                    for idx, char in enumerate(answer5):
                        user_matrix[start_i][start_j + idx] = char
                        matrix[start_i][start_j + idx] = char
            if request.json['answer6'] != '':
                answer6 = request.json['answer6']
                print(answer6)
                if answer6 == original_answer6:
                    start_i, start_j = start_pos_across(answer6,"down")
                    for idx, char in enumerate(answer6):
                        user_matrix[start_i][start_j + idx] = char
                        matrix[start_i][start_j + idx] = char
                    print(matrix)
                return jsonify(user_matrix=user_matrix, matrix=matrix)  
            else:
                flash('Incorrect answer')
                 
        return render_template('index.html', user_matrix=user_matrix, matrix=matrix,question1 = question1,question2 = question2,question3 = question3,question4 = question4,question5 = question5,question6 = question6)
    else:
        return render_template('loginerr.html',error_type="not_logged_in")
@app.route('/', methods=["POST","GET"])
def login():
    if request.method == "POST":
        if request.form["usr"] in playerlist:
            if request.form["pswd"] == playerlist[request.form["usr"]]:
                session['username'] = request.form["usr"]
                session['logged_in'] = False
            
                if request.form["usr"] == "MeekOmni" and playerlist[request.form["usr"]] == "thisisrandompass":
                    session['logged_in'] = True
                    return redirect('/admin')
                return redirect('/crossword')
            else:
                return render_template('loginerr.html',error_type="invalid_credentials")
        username = request.form["usr"]
        password = request.form["pswd"]
        playerlist[username] = password
        session['username'] = username   
        return redirect('/crossword')
    else:
        return render_template('login.html')
@app.route('/admin', methods=["POST","GET"])

def admin():
    global original_answer1,original_answer2,original_answer3,original_answer4,original_answer5,original_answer6
    global question1,question2,question3,question4,question5,question6
    try:
        print(session['logged_in'])
        if session['logged_in'] == True:
            if request.method == "POST":
                question1 = request.form["question1"]
                original_answer1 = request.form["answer1"]
                question2 = request.form["question2"]
                original_answer2 = request.form["answer2"]
                question3 = request.form["question3"]
                original_answer3 = request.form["answer3"]
                question4 = request.form["question4"]
                original_answer4 = request.form["answer4"]
                question5 = request.form["question5"]
                original_answer5 = request.form["answer5"]
                question6 = request.form["question6"]       
                original_answer6 = request.form["answer6"]
            if request.method == "POST" and "pass_reset" in request.form:
                playerlist[request.form["pass_reset"]] = "samplepass"
            return render_template('admin.html', playerlist= playerlist)   
        else:
            return render_template('loginerr.html',error_type="privilege_escalation")   
    except:
        return render_template('loginerr.html',error_type="privilege_escalation")


if __name__ == '__main__':

    app.run(debug=True)
