from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """<p>Це головна сторінка нашого сайту.</p>
              <a href='/about/'>Про нас</a> | 
              <a href='/services/'>Послуги</a> | 
              <a href='/contact/'>Контакти</a>"""

@app.route('/about/')
def about():
    return """<h1>Про нас</h1>
              <a href='/'>Головна</a> | 
              <a href='/services/'>Послуги</a> | 
              <a href='/contact/'>Контакти</a>"""

@app.route('/services/')
def services():
    return """<h1>Наші послуги</h1>
              <a href='/'>Головна</a> | 
              <a href='/about/'>Про нас</a> | 
              <a href='/contact/'>Контакти</a>"""

@app.route('/contact/')
def contact():
    return """<h1>Контакти</h1>
              <a href='/'>Головна</a> | 
              <a href='/about/'>Про нас</a> | 
              <a href='/services/'>Послуги</a>"""

if __name__ == '__main__':
    app.run(debug=True)
