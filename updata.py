# Update from Day 60 - Handle Post Requests with Flask #

# index.html---form---action, method and name #  ⬇️ 
 <form action="{{url_for(receive_data)}}" method="post">
     <label>Name:</label> <input name="username">
     <br><br>
     <label>Password:</label> <input type="password" placeholder="enter please" name="password">
     <br>
     <button type="submit" value="Submit">OK</button>
 </form>


# main.py---request, methodS #  ⬇️ 
from flask import Flask, render_template, request
@app.route('/login', methods=["POST"])
def receive_data():
    username_data = request.form['username']
    password_data = request.form['password']
    return render_template('login.html', username=username_data, password=password_data)
