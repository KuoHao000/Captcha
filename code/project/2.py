import functools
from flask import Flask, render_template, jsonify, request, redirect, url_for, session

DATA_DICT = {
    '1': {'name':'richard','age':33},
    '2': {'name':'amy','age':55}
}

app = Flask(__name__)
#app = Flask(__name__,template_folder=) template_folder= 放置模板的位置，沒有給的話預設路徑是templates資料夾
app.secret_key = 'jasldkajsdlkasjdksad'

#驗證使否有登入
def auth(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        username = session.get('a')
        if not username:
            return redirect('/')
        return func(*args,**kwargs)
    return inner

#@app.route('/') 預設只允許GET方法
@app.route('/', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        #return '登入' http response
        #return render_template('login.html') render
        #return jsonify({'test':20230818,'data':[1,2,3]}) json response
        
        return render_template('login.html')
    
    user = request.form.get('user')
    pwd = request.form.get('pwd')
     
    print(request.form)

    if user == '1' and pwd == 'a':
        session['a'] = '1'
        return redirect('/index')
    error = 'username or password fail'
    #return render_template('login.html', **{'error':error})
    return render_template('login.html', error=error)

#@app.route('/index')
@app.route('/index', endpoint='idx')
@auth
def index():
    data_dict = DATA_DICT
    return render_template('index.html', data_dict=data_dict)

@app.route('/edit', methods=['GET','POST'])
@auth
def edit():
    nid = request.args.get('nid')

    if request.method == 'GET':
        #print(nid, type(nid))
        info = DATA_DICT[nid]
        return render_template('edit.html', info=info)

    user = request.form.get('user')
    age = request.form.get('age')
    DATA_DICT[nid]['name'] = user
    DATA_DICT[nid]['age'] = age
    return redirect(url_for('idx'))
    
# @app.route('/del')
# def delete():
#     nid = request.args.get('nid')
#     print(nid)
#     return '刪除'

#@app.route('/del/<int:nid>')
@app.route('/del/<nid>')
@auth
def delete(nid):
    print(nid,type(nid))
    del DATA_DICT[nid]
    #return redirect('/index')
    return redirect(url_for('idx'))

# @app.errorhandler(404)
# def page_not_found_404(e):
#     return render_template('error.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
    #app.run(host='0.0.0.0', port='8080', debug=True)