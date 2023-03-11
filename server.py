from flask import Flask
import random

app = Flask(__name__)

topics = [
    {'id': 1, 'title': 'html', 'body': 'html is ...'},
    {'id': 2, 'title': 'css', 'body': 'css is ...'},
    {'id': 3, 'title': 'javascript', 'body': 'javascript is ...'}
]

def template(contents, content):
    return f'''
        <!DOCTYPE html>
        <body>
            <h1><a href="/">WEB</a></h1>
            <ol>
                {contents}
            </ol>
            {content}
            <ul>
                <li><a href="/create/">create</a></li>
            </ul>
        </body>
        </html>
    '''

def getContents():
    liTags = ''
    for topic in topics:
        #<li><a href="/read/1/">html</a></li>
        liTags = liTags + f'<li><a href="/read/{topic["id"]}/">{topic["title"]}</a></li>'
    return liTags

@app.route('/')
def index():
    return template(getContents(), '<h2>Welcome</h2>Hello, WEB')

@app.route('/create/')
def create():
    content = '''
        <form action="/create/" method="POST">
            <p><input type="text" name="title" placeholder="TITLE"></p>
            <p><textarea name="body" placeholder="BODY"></textarea></p>
            <p><input type="submit" value="create"></p>
        </form>
    '''
    return template(getContents(), content)

@app.route('/read/<int:id>/')
def read(id):
    title = ''
    body = ''
    for topic in topics:
        if id  == topic['id']:
            title = topic['title']
            body = topic['body']
            break
    return template(getContents(), f'<h2>{title}</h2>{body}')
    return 'read :' +id

app.run(debug=True)