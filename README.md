# Blog Project
To build a personal blog using Python, Flask and Jinja.

# What I learned:
1) Sending over arguments from Python file to HTML file. In the HTML file, the variable shall be wrapped with {{ }}
2) Writing multi-lines expressions in the HTML file using {% %} and {% endfor %}. See Flask--> quickstart--> routing
3) Navigating to another individual HTML file from index.html file by using: href = "{{ url_for( 'function_name_without_parentheses', input=variable) }}"

# Updates from Day 59
4) {% include "header.html" %}
   {% include "footer.html" %}
5) url building concerning inline style: style="background-image: **url(url_for('static', filename='assets/img/post-bg.jpg'))**"

# Updates from Day 60 - Handle POST Request with Flask
6)在HTML文件的Form中，action="{{ url_for('function') }}" method="post"
7) To catch the Post request in the server, we first need to give each <input> in the form a name attribute. e.g. <input name="username">
8) Then cretae a decorator in the main.py that will trigger a method wehn it receives a POST request. Note that the methods is a list and its name is in plural form. e.g. @app.route('/contact', method**s**=['POST', 'GET'])
