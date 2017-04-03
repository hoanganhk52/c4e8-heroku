from flask import *
from datetime import *
import mlab
from model.fooditem import FoodItem
from model.user import User
import os
from werkzeug.utils import *
from flask_login import *
from sessionuser import SessionUser


app = Flask(__name__)

#connect to mlab database
mlab.connect()

app.config["UPLOAD_PATH"] = os.path.join(app.root_path, "uploads")
if not os.path.exists(app.config["UPLOAD_PATH"]):
    os.makedirs(app.config["UPLOAD_PATH"])

app.secret_key = "nganha12a2"

#initialize login system
login_manager = LoginManager()
login_manager.init_app(app)

# tao 1 tai khoan
# admin_user = User()
# admin_user.username = "admin"
# admin_user.password = "admin"
# admin_user.save()

@login_manager.user_loader
def user_loader(user_token):
    found_user = User.objects(token=user_token).first()
    if found_user:
        session_user = SessionUser(found_user.id)
        return session_user



#creat a new FoodItem and save it to database

@app.route('/')
def hello_world():
    return redirect(url_for("foodblog"))


@app.route('/dangnhap', methods=["GET", "POST"])
def dangnhap():
    if request.method == "GET":
        return render_template("dangnhap.html")
    elif request.method == "POST":
        user = User.objects(username=request.form["username"]).first()
        if user and user.password == request.form["password"]:
            session_user = SessionUser(user.id)
            user.update(set__token=str(user.id))
            login_user(session_user)
            return redirect(url_for("addfood"))
        else:
            return render_template("dangnhap.html")

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for("dangnhap"))


girl_list = [
    {
        "src" : "http://68.media.tumblr.com/c2b359d90b868247565a37b4f70ea2d9/tumblr_omu6agTv6b1qbd81ro1_1280.jpg",
        "title" : "12343 by Đinh Văn Linh ♥",
        "tag" : "A lot more at http://xkcn.info - Xinh Ko Chiu Noi ♥"
    },
    {
        "src" : "http://68.media.tumblr.com/fdce8d90185f8f38a5f36a69b198a271/tumblr_ojqkfv1h7c1qbd81ro1_1280.jpg",
        "title" : "lightstudio | 0966726996 by Leo White | 0966 72 6996 | 0164 960 8794 ♥",
        "tag" : "A lot more at http://xkcn.info - Xinh Ko Chiu Noi ♥"
    },
{
        "src":"http://68.media.tumblr.com/333c275f13f585bb49a55f9e7b8fa9c8/tumblr_of8kztZ3QA1qbd81ro1_1280.jpg",
        "title" : "lightstudio | 0966726996 by Leo White | 0966 72 6996 | 0164 960 8794 ♥",
        "tag" : "A lot more at http://xkcn.info - Xinh Ko Chiu Noi ♥"
    },
{
        "src" : "http://68.media.tumblr.com/6707567f4007a0ebb6e342f37692da0b/tumblr_of8kzf8gMp1qbd81ro1_1280.jpg",
        "title" : "lightstudio | 0966726996 by Leo White | 0966 72 6996 | 0164 960 8794 ♥",
        "tag" : "A lot more at http://xkcn.info - Xinh Ko Chiu Noi ♥"
    }
]



my_contact = {
    "Avatar": "https://scontent.fhan2-1.fna.fbcdn.net/v/t1.0-9/1655910_258291991014902_2123799782_n.jpg?oh=d4ff603db8ca1b9ce9f5e3f00e549cfe&oe=596903F7",
    "Fullname": "Pham Hoang Anh",
    "DOB": "03-11-1989",
    "Location": "Ha noi, Viet Nam",
    "Martial Status": "Maried",
    "Email": "hoanganhctm7@gmail.com",
    "Phone": "01628338711",
    "Education": "Bach Khoa University"
}

foodlist=[

{
    "src" : "../static/images/food1.png",
    "alt" : "Sandwich",
    "title" : "The Perfect Sandwich, A Real NYC Classic",
    "information" : "Just some random text, lorem ipsum text praesent tincidunt ipsum lipsum."
    },
{
    "src" : "../static/images/food2.png",
    "alt" : "Steak",
    "title" : "Let Me Tell You About This Steak",
    "information" : "Once again, some random text to lorem lorem lorem lorem ipsum text praesent tincidunt ipsum lipsum."
    },
{
    "src" : "../static/images/food3.png",
    "alt" : "Cherries",
    "title" : "Cherries, interrupted",
    "information" : "Lorem ipsum text praesent tincidunt ipsum lipsum."
    },
{
    "src" : "../static/images/food4.png",
    "alt" : "Pasta and Wine",
    "title" : "Once Again, Robust Wine and Vegetable Pasta",
    "information" : "Lorem ipsum text praesent tincidunt ipsum lipsum."
    }
,

{
    "src" : "../static/images/food5.png",
    "alt" : "Popsicle",
    "title" : "All I Need Is a Popsicle",
    "information" : "Just some random text, lorem ipsum text praesent tincidunt ipsum lipsum."
    },
{
    "src" : "../static/images/food6.png",
    "alt" : "Salmon",
    "title" : "Salmon For Your Skin",
    "information" : "Once again, some random text to lorem lorem lorem lorem ipsum text praesent tincidunt ipsum lipsum."
    },
{
    "src" : "../static/images/food7.png",
    "alt" : "Sandwich",
    "title" : "The Perfect Sandwich, A Real Classic",
    "information" : "Just some random text, lorem ipsum text praesent tincidunt ipsum lipsum."
    },
{
    "src" : "../static/images/food8.png",
    "alt" : "Croissant",
    "title" : "Le French",
    "information" : "Lorem lorem lorem lorem ipsum text praesent tincidunt ipsum lipsum."
    }

]

# for image in foodlist:
#     new_food = FoodItem()
#     new_food.src = image["src"]
#     new_food.title = image["alt"]
#     new_food.description = image["title"]
#     new_food.save()


number_of_visitor = 0


@app.route('/contact')
def contact():
    return render_template("contact.html", contact=my_contact)


@app.route('/login')
def login():
    global number_of_visitor
    number_of_visitor += 1
    current_time_on_server = str(datetime.now())
    return render_template("login.html", current_time_on_server=current_time_on_server, number_of_visitor=number_of_visitor * 1000)


@app.route('/food')
def food():
    return render_template("food.html", list_girl=girl_list)


@app.route('/cssdemo')
def cssdemo():
    return render_template("cssdemo.html")


@app.route('/w3cssdemo')
def w3cssdemo():
    return render_template("w3cssdemo.html")


@app.route('/foodblog')
def foodblog():
    return render_template("foodblog.html", foodlist=FoodItem.objects())


@app.route('/addfood', methods=["GET", "POST"])
@login_required
def addfood():
    if request.method == "GET":
        return render_template("addfood.html")
    elif request.method == "POST":
        file = request.files["source"]
        if file:
            filename = secure_filename(file.filename)
            if os.path.join(app.config["UPLOAD_PATH"], filename):
                name_index = 0
                #filename = home.png
                #filename.rsplit(".", 1)[0] => ["home", "png"]
                original_name = filename.rsplit(".", 1)[0]
                original_extension = filename.rsplit(".", 1)[1]
                while os.path.exists(os.path.join(app.config["UPLOAD_PATH"], filename)):
                    name_index +=1
                    filename = "{0} ({1}).{2}".format(original_name, name_index, original_extension)
            file.save(os.path.join(app.config["UPLOAD_PATH"], filename))

        newfood = FoodItem()
        newfood.src = url_for("uploaded_file", filename=filename)
        newfood.title = request.form["title"]
        newfood.description = request.form["description"]
        newfood.save()
        return render_template("addfood.html")


@app.route("/uploads/<filename>")
def uploaded_file(filename):
    return send_from_directory(app.config["UPLOAD_PATH"], filename)


@app.route('/deletefood', methods=["GET", "POST"])
def deletefood():
    if request.method == "GET":
        return render_template("deletefood.html")
    elif request.method == "POST":
        newfood = FoodItem.objects(title=request.form["title"]).first()
        if newfood is not None:
            newfood.delete()
        return render_template("deletefood.html")


@app.route('/updatefood', methods=["GET", "POST"])
def updatefood():
    if request.method == "GET":
        return render_template("updatefood.html")
    elif request.method == "POST":
        oldfood = FoodItem.objects(title=request.form["title"]).first()
        if oldfood is not None:
            oldfood.delete()
        newfood = FoodItem()
        newfood.src = request.form["source"]
        newfood.title = request.form["new_title"]
        newfood.description = request.form["description"]
        newfood.save()
        return render_template("updatefood.html")


if __name__ == '__main__':
    app.run()


