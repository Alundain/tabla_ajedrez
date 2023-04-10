from flask import Flask, render_template
app=Flask(__name__)

@app.route('/')
def normal():
    return render_template('index.html', num_one=8, num_two=8)

@app.route('/<x>')
def mas_de_uno(x):
    return render_template('index.html', num_one=int(x), num_two=int(x) )

@app.route('/<x>/<y>')
def muchos(x,y):
    return render_template('index.html', num_one=int(x), num_two=int(y) )

@app.route('/<x>/<y>/<c3>/<c4>')
def color(x,y,c3,c4):
    return render_template('index.html', num_one=int(x), num_two=int(y),color3=c3,color4=c4)

if __name__=='__main__':
    app.run(debug=True)