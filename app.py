from flask import Flask, render_template, url_for, request, redirect, flash, send_file, abort
import markdown
import requests

class Post:
    def __init__(self, title, url):
        self.title = title
        self.url = url
       

blog_posts = [Post('Refleksjoner rundt arbeidsmarkedet','https://raw.githubusercontent.com/KrHaugen/markdowns/refs/heads/main/refleksjoner_rundt_arbeidsmarkedet'),
              Post('Ulykker til sjøs','https://raw.githubusercontent.com/KrHaugen/markdowns/refs/heads/main/ulykker_til_sj%C3%B8s')]

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/blog/<int:number>')
def blog(number):
    if number < 1 or number > len(blog_posts):
       abort(404, "This Post doesn't exist") 

    data = blog_posts[number -1]    
    data.content = markdown.markdown(requests.get(blog_posts[number -1].url).text)
    return render_template('post.html', item=data)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)
