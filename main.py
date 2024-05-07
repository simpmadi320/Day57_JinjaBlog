from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    blog_url = "https://api.npoint.io/1f94745f5753e2eb1013"
    response = requests.get(blog_url)
    data=response.json()
    print(data)
    return render_template("index.html", posts=data)

@app.route('/post/<index>')
def get_post(index):
    blog_url = "https://api.npoint.io/1f94745f5753e2eb1013"
    response = requests.get(blog_url)
    data=response.json()
    return render_template("post.html", post=data[int(index)-1])

if __name__ == "__main__":
    app.run(debug=True)
