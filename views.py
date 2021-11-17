#"""
#Routes and views for the flask application.
#"""

#from datetime import datetime
#from flask import render_template
#from flask import request
#from .lvrtech import dbconnect
#from .lvrtech import OuraConnect as oc

#@app.route('/')
#@app.route('/home')
#def home():
#    """Renders the home page."""
#    return render_template(
#        'index.html',
#        title='Home Page',
#        year=datetime.now().year,
#    )

#@app.route('/contact')
#def contact():
#    """Renders the contact page."""
#    return render_template(
#        'contact.html',
#        title='Contact',
#        year=datetime.now().year,
#        message='Your contact page.'
#    )

#@app.route('/about')
#def about():
#    """Renders the about page."""
#    return render_template(
#        'about.html',
#        title='About',
#        year=datetime.now().year,
#        message='Your application description page.'
#    )

#@app.route('/createuser', methods=['GET', 'POST'])
#def createuser():    
#    print(request)
#    if request.method == 'POST':
#        dbconnect.create_user(request.form.get("userid"), request.form.get("token"), request.form.get("email"))
#        oc.get_user_info(request.form.get("token"))
#        oc.get_readiness_summary(request.form.get("token"))
#        oc.get_activity_summary(request.form.get("token"))
#        oc.get_sleep_summary(request.form.get("token"))
        
#    return render_template(
#        'create_user.html'    ,
#        title="Create User"
#    )

#@app.route("/getusers")
#def get_users():
#    dbconnect.get_all_users()
#    return render_template(
#        'create_user.html'    ,
#        title="Create User"
#    ) 

#@app.route("/userinfo")
#def get_all_user_info():
#    activities = dbconnect.get_all_activity()
#    userinfo = dbconnect.get_all_userinfo()
#    print(len(userinfo))
#    return render_template(
#        'userinfo.html',
#        userinfotitle="User info - All Users",
#        activitytitle="Activities - All Users",
#        userinfo=userinfo,
#        activities=activities
#    )