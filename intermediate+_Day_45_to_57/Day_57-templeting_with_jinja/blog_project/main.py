import requests
from flask import Flask, render_template
from post import Post


app = Flask(__name__)

# Fetch all the blog posts using api
url = 'https://api.npoint.io/ecc8ddefc7a8ef28a6c1'
posts = requests.get(url).json()

post_objects = []  # Holds created post objects
for post in posts:  # Creates post objects
    post_obj = Post(
        post['id'],
        post['title'],
        post['subtitle'],
        post['body']
    )
    post_objects.append(post_obj)


""" Home page that contains blog posts title """
@app.route('/')
def home():
    return render_template("index.html", posts=post_objects)


""" Creates page for each blog post based on post id """
@app.route('/blog/<int:index>')
def blog_post(index):
    requested_post = None
    for post in post_objects:
        if post.id == index:
            requested_post = post
    return render_template('post.html', post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
