from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def get_blog():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    blog_data = requests.get(url=blog_url).json()
    return render_template('index.html', posts=blog_data)


@app.route('/post/<blog_id>')
def get_post(blog_id):
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    blog_data = requests.get(url=blog_url).json()
    blog_id = int(blog_id)
    return render_template('post.html', posts=blog_data, post_id=blog_id)


if __name__ == "__main__":
    app.run(debug=True)

