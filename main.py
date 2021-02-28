from flask import *
import csv

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


# def write_to_file(data):
#     with open('database.txt', mode="a") as database:
#         email = data["email"]
#         content = data["content"]
#         message = data["message"]
#         file = database.write(f"\n {email},{content},{message}")


def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database1:
        email = data["email"]
        content = data["content"]
        message = data["message"]
        csv_writer = csv.writer(database1, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, content, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            #write_to_file(data)
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return "Did not work as expected"
    else:
        return "Something went wrong. Try Again!"


if __name__ == '__main__':
    app.run(debug=True)
