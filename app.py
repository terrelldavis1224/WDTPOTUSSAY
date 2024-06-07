import utils
import flask
app = flask.Flask(__name__)

president_list =[]
executive_order_list = []
ans_president_list =[]
ans_executive_order_list = []
current_executive_order = ""
current_president = ""
correct = 0

@app.route('/')
def index():
    return flask.render_template('index.html')

@app.route('/about')
def about():
    return flask.render_template('about.html')

@app.route('/history')
def history():
    return flask.render_template('history.html', president_list=ans_president_list, executive_order_list=ans_executive_order_list, total=len(ans_president_list), correct=correct)

@app.route('/guess', methods=['GET', 'POST'])
def predict():
    president,executive = utils.get_executive_order()
    global correct
    if flask.request.method == 'POST':
        ans_president_list.append(president_list[-1])
        ans_executive_order_list.append(executive_order_list[-1])
        data = flask.request.form
        guess = data['guess']
        if guess == president_list[-1]:
            correct = correct + 1

        president_list.append(president)
        executive_order_list.append(executive)
        return flask.render_template('guess.html', president=president, executive=executive,correct=correct, total=len(ans_president_list))
    president_list.append(president)
    executive_order_list.append(executive)
    return flask.render_template('guess.html',president=president,executive=executive,correct=correct, total=len(ans_president_list))

if __name__ == '__main__':
    app.run(debug=True)