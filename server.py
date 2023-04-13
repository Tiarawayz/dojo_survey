from flask import Flask, render_template, request, redirect, session
app= Flask (__name__)
app.secret_key = 'Run It Or Not'


@app.route('/')
def survey():
    return render_template('dojo.html')


@app.route('/submit', methods=['POST'])
def survey_done():
    session['name'] = request.form ['name']
    session['dojo_location'] = request.form['dojo_location']
    session['favorite_language'] = request.form['favorite_language']
    session['comments'] = request.form['comments']
    return redirect('/submit')


@app.route('/submit')
def done():
    print(session)
    return render_template('submit.html')

@app.route('/destroy_session')
def refresh():
    session()
    return render_template('/')


if __name__=='__main__':
    app.run(debug=True)