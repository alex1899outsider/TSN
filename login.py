import secrets
import re
from flask import Flask, render_template, request, redirect, url_for, flash

valid = re.compile(r"\w+")

app = Flask(__name__, template_folder='C:/Users/hp/PythonProjects/pythonProject/thefacebook')
app.secret_key = secrets.token_hex(16) # 用于 flash 消息的密钥

@app.route('/')
def home_page():
    return render_template('home_page.html')

@app.route('/login.html', methods=['POST'])
def login():
    # 获取表单数据
    username = request.form.get('username')
    password = request.form.get('password')

    # 在这里可以进行登录逻辑的处理，比如验证用户名密码等
    match_username = valid.findall(username)
    match_password = valid.findall(password)

    if match_username and match_password:
        flash("Login successful!", "success")
        return redirect('http://127.0.0.1:3000/thefacebook/home_page.html')
    else:
        flash("Invalid username or password. Only English letters(a-Z), numerals(0-9), and _ are supported.", "error")
        return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)