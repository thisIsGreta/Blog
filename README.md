# Blog Project
To build a personal blog using Python, Flask and Jinja.

# What I learned:
1) Sending over arguments from Python file to HTML file. In the HTML file, the variable shall be wrapped with {{ }}
2) Writing multi-lines expressions in the HTML file using {% %} and {% endfor %}. See Flask--> quickstart--> routing
3) Navigating to another individual HTML file from index.html file by using: href = "{{ url_for( 'function_name_without_parentheses', input=variable) }}"

# UPDATES from Day 58
4) {% include "header.html" %}
   {% include "footer.html" %}
5) url building concerning inline style: style="background-image: **url(url_for('static', filename='assets/img/post-bg.jpg'))**"
