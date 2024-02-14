from flask import Flask, render_template, url_for, request, redirect,flash,session, Response, jsonify
import datetime

secret_key = 'th!5!5r@nd0mk3y'

app = Flask(__name__)

#Remember to keep the empty spaces as ' ' and not '' or the program will not work

app.secret_key = secret_key

matrix = [[' ',' ',' ',' ',' ',' ',' '],
          [' ','p','i','n',' ',' ',' '],
          [' ','i',' ','e','d','g','e'],
          [' ','c',' ','g',' ',' ',' '],
          [' ','k','r','a','b','s',' '], 
          [' ','l',' ',' ','e',' ',' '],
          [' ','e',' ',' ','e',' ',' ']]


# Enter the original answers to the questions here

# Across answers
playerlist={}
leaderboard = {}
user_matrices = []
original_answer1 = ''
original_answer2 = ''
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
idx_i = 0
idx_j = 0
def start_pos_across(word, direction):
    
    if direction == "across":
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if (matrix[i][j]!=" ") and (matrix[i][j] == word[0]):
                    if j+len(word)<=7:
                        idx_i = i
                        idx_j = j
                        return idx_i, idx_j
    elif direction == "down":
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if (matrix[i][j]!=" ") and (matrix[i][j] == word[0]):
                    if i+len(word)<=7:
                        idx_i = i
                        idx_j = j
                        return idx_i, idx_j
    return None, None
startflag = False
complete = [0,0,0,0,0,0]
@app.route('/crossword', methods=['GET', 'POST'])
def home():  
    global startflag
    global complete
    global start
    global end
    global leaderboard
    if 'username' in session:  
        user_matrix = [[' ',' ',' ',' ',' ',' ',' '],
                [' ',' ',' ',' ',' ',' ',' '],
                [' ',' ',' ',' ',' ',' ',' '],
                [' ',' ',' ',' ',' ',' ',' '],
                [' ',' ',' ',' ',' ',' ',' '],
                [' ',' ',' ',' ',' ',' ',' '],
                [' ',' ',' ',' ',' ',' ',' ']]
        if startflag == False: 
            user_matrices.append(user_matrix)
            startflag = True
            start = datetime.datetime.now()
        if request.method == 'POST':
            if user_matrix == matrix:
                leaderboard[request.json["usr"]] = request.json["ElapsedT"]
            if request.json['answer1'] != '':
                answer1 = request.json['answer1']
                start_i, start_j = start_pos_across(answer1, "across")
                if start_i is not None and start_j is not None:
                    for idx, char in enumerate(answer1):
                        user_matrix[start_i][start_j+idx] = char
                        #matrix[start_i][start_j+idx] = char
                complete[0]= 1
            if request.json['answer2'] != '':
                answer2 = request.json['answer2']
                start_i, start_j = start_pos_across(answer2, "across")
                if start_i is not None and start_j is not None:
                    for idx, char in enumerate(answer2):
                        user_matrix[start_i][start_j+idx] = char
                        #matrix[start_i][start_j+idx] = char
                complete[1]= 1
            if request.json['answer3'] != '':
                answer3 = request.json['answer3']
                start_i, start_j = start_pos_across(answer3, "across")
                if start_i is not None and start_j is not None:
                    for idx, char in enumerate(answer3):
                        user_matrix[start_i][start_j+idx] = char
                        #matrix[start_i][start_j+idx] = char
                complete[2]= 1
            if request.json['answer4'] != '':
                answer4 = request.json['answer4']
                start_i, start_j = start_pos_across(answer4, "down")
                if start_i is not None and start_j is not None:
                    for idx, char in enumerate(answer4):
                        user_matrix[start_i + idx][start_j] = char
                        #matrix[start_i + idx][start_j] = char
                complete[3]= 1
            if request.json['answer5'] != '':
                answer5 = request.json['answer5']
                start_i, start_j = start_pos_across(answer5, "down")
                if start_i is not None and start_j is not None:
                    for idx, char in enumerate(answer5):
                        user_matrix[start_i + idx][start_j] = char
                        #matrix[start_i + idx][start_j] = char
                complete[4]= 1
            if request.json['answer6'] != '':
                answer6 = request.json['answer6']
                start_i, start_j = start_pos_across(answer6, "down")
                if start_i is not None and start_j is not None:
                    for idx, char in enumerate(answer6):
                        user_matrix[start_i + idx][start_j] = char
                        #matrix[start_i + idx][start_j] = char
                complete[5]= 1
                if 0 not in complete:
                    end = datetime.datetime.now()
                    elapsed_time = end - start
                    leaderboard[username] = elapsed_time
                    start = datetime.datetime.now()
            
            return jsonify(user_matrix=user_matrix, matrix=matrix)
        return render_template('index.html', user_matrix=user_matrix, matrix=matrix,question1 = question1,question2 = question2,question3 = question3,question4 = question4,question5 = question5,question6 = question6)
    else:
        return render_template('loginerr.html',error_type="not_logged_in")
@app.route('/', methods=["POST","GET"])
def login():
    
    if request.method == "POST":
        if request.form["usr"] in playerlist:
            if request.form["pswd"] == playerlist[request.form["usr"]]:
                session['username'] = request.form["usr"]
                if request.form["usr"] == "MeekOmni" and playerlist[request.form["usr"]] == "thisisrandompass":
                    session['logged_in'] = True
                    return redirect('/admin')
                else:
                    return redirect('/crossword')
            else:
                return render_template('loginerr.html',error_type="invalid_credentials")
        global username
        username = request.form["usr"]
        password = request.form["pswd"]
        playerlist[username] = password
        session['username'] = username 
        if request.form["usr"] == "MeekOmni":
            if playerlist[request.form["usr"]] == "thisisrandompass":
                    session['logged_in'] = True
                    return redirect('/admin')
            else:
                    playerlist.pop('MeekOmni')
                    return render_template('loginerr.html',error_type="invalid_credentials")
        else:
                    return redirect('/crossword')  
    else: 
        return render_template('login.html')
    
@app.route('/leaderboard' , methods =["POST","GET"])
def show_leaderboard():
    return render_template('leaderboard.html',leaderboard = leaderboard)
@app.route('/admin', methods=["POST","GET"])
def admin():
    global original_answer1,original_answer2,original_answer3,original_answer4,original_answer5,original_answer6
    global question1,question2,question3,question4,question5,question6
    try:
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
