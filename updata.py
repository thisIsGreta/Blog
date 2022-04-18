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
@app.route('/contact', methods=["POST", "GET"])
def contact_data():
    if request.method == "POST":
        name_data = request.form['username']
        email_data = request.form['email']
        phone_data = request.form['phone']
        message_data = request.form['message']
        return render_template('contact.html', message="Successfully sent your message.")
    elif request.method == "GET":
        return render_template('contact.html')
     
#contact.html # ⬇️
   <div class="page-heading">
       {% if request.method == "GET": %}
       <h1>Contact Me</h1>
       {% elif request.method == "POST": %}
       <h1>{{message}}</h1>
       {% endif %}
   </div>
