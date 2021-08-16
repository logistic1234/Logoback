# Create your views here.
from django import contrib
from django.shortcuts import redirect, render, HttpResponse
from datetime import datetime 
from firebase import firebase
from requests import post,get
from firebase.firebase import FirebaseApplication, FirebaseAuthentication
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth import SESSION_KEY, authenticate
from django.contrib.auth import logout,login
import pyrebase 
from pyrebase.pyrebase import Database
import firebase_admin
from firebase_admin import auth ,credentials, db
#This is Neemeesh
#This is Omkar
config = {    
    "apiKey": "AIzaSyDxtgOS-lNR5iHH-35xjs9r1gIwiLDW6E8",
    "authDomain": "neemeesh-trial.firebaseapp.com",
    "databaseURL": "https://neemeesh-trial-default-rtdb.firebaseio.com",
    "projectId": "neemeesh-trial",
    "storageBucket": "neemeesh-trial.appspot.com",
    "messagingSenderId": "608861234921",
    "appId": "1:608861234921:web:2792a40a8e9cf8611c7278",
    'measurementId': "G-67HDRQV9KN"
}
firebase = pyrebase.initialize_app(config) 
authe = firebase.auth() 
database = firebase.database()
cred = credentials.Certificate('neemeesh-trial-firebase-adminsdk-kl0a5-1cf2f25008.json')
firebase_admin.initialize_app(cred)
def index(request):
    #context = {"variable1": "Harry is great", "variable2": "Rohan is great"}
    #return HttpResponse("This is homepage")
    return render(request, 'index.html')
def contact(request):
    return render(request, 'contact.html')
def about(request):
    return render(request, 'about.html')
def services(request):
    return render(request, 'services.html')    
def prelogin(request):
    return render(request,'prelogin.html')  
def adminlogin(request):
    return render(request,'adminlogin.html')    
def dispatchlogin(request):
    return render(request,'dispatchlogin.html')    
def mislogin(request):
    return render(request,'mislogin.html')    
def bookinglogin(request):
    return render(request,'bookinglogin.html')
def registeradmin (request) :
    return render(request , "registeradmin.html")    
def registerbooking (request) :
    return render(request , "registerbooking.html")    
def registerdispatch (request) :
    return render(request , "registerdispatch.html")    
def registermis (request) :
    return render(request , "registermis.html")    
def postregisteradmin (request) :
    name = request.POST.get('name')
    email = request.POST.get('email')
    passw1 = request.POST.get('pass')
    address = request.POST.get('add')
    country = request.POST.get('count')
    state = request.POST.get('state')
    city = request.POST.get('city')
    pincode = request.POST.get('pin')
    phone = request.POST.get('phone')
    try:
        user=authe.create_user_with_email_and_password(email,passw1)
        session_id=user['idToken']
        request.session['uid']=str(session_id)
    except:
        msg="Email Already Exists!"
        return render(request,"registeradmin.html",{"msg":msg}) 
        #push data 
    data={
        "name" :name ,
        "email" : email ,
        "address" : address ,
            "country" : country ,
            "state":state,
            "city":city,
            "pincode":pincode,
            "phone":phone
        }
    database.child("Data").child("Signup").child("Admin").push(data)
    print("User created")
    msg="You have successfully registered a new Admin!"
    return render(request,"registernewuser.html",{"msg":msg})
    # messages.success(request, 'Your have successfully registered!')
    # return render(request,"registernewuser.html")
def postregisterbooking (request) :
    name = request.POST.get('name')
    email = request.POST.get('email')
    passw1 = request.POST.get('pass')
    address = request.POST.get('add')
    country = request.POST.get('count')
    state = request.POST.get('state')
    city = request.POST.get('city')
    pincode = request.POST.get('pin')
    phone = request.POST.get('phone')
    try:
        user=authe.create_user_with_email_and_password(email,passw1)
        session_id=user['idToken']
        request.session['uid']=str(session_id)
    except:
        msg="Email Already Exists!"
        return render(request,"registerbooking.html",{"msg":msg}) 
        #push data 
    data={
        "name" :name ,
        "email" : email ,
        "address" : address ,
            "country" : country ,
            "state":state,
            "city":city,
            "pincode":pincode,
            "phone":phone
        }
    database.child("Data").child("Signup").child("Booking").push(data)
    print("User created")
    msg="You have successfully registered a new Booking User!"
    return render(request,"registernewuser.html",{"msg":msg})
def postregistermis (request) :
    name = request.POST.get('name')
    email = request.POST.get('email')
    passw1 = request.POST.get('pass')
    address = request.POST.get('add')
    country = request.POST.get('count')
    state = request.POST.get('state')
    city = request.POST.get('city')
    pincode = request.POST.get('pin')
    phone = request.POST.get('phone')
    try:
        user=authe.create_user_with_email_and_password(email,passw1)
        session_id=user['idToken']
        request.session['uid']=str(session_id)
    except:
        msg="Email Already Exists!"
        return render(request,"registermis.html",{"msg":msg}) 
        #push data 
    data={
        "name" :name ,
        "email" : email ,
        "address" : address ,
            "country" : country ,
            "state":state,
            "city":city,
            "pincode":pincode,
            "phone":phone
        }
    database.child("Data").child("Signup").child("MIS").push(data)
    print("User created")
    msg="You have successfully registered a new MIS User!"
    return render(request,"registernewuser.html",{"msg":msg})
def postregisterdispatch (request) :
    name = request.POST.get('name')
    email = request.POST.get('email')
    passw1 = request.POST.get('pass')
    address = request.POST.get('add')
    country = request.POST.get('count')
    state = request.POST.get('state')
    city = request.POST.get('city')
    pincode = request.POST.get('pin')
    phone = request.POST.get('phone')
    try:
        user=authe.create_user_with_email_and_password(email,passw1)
        session_id=user['idToken']
        request.session['uid']=str(session_id)
    except:
        msg="Email Already Exists!"
        return render(request,"registerdispatch.html",{"msg":msg}) 
        #push data 
    data={
        "name" :name ,
        "email" : email ,
        "address" : address ,
        "country" : country ,
        "state":state,
        "city":city,
        "pincode":pincode,
        "phone":phone
        }
    database.child("Data").child("Signup").child("Dispatch").push(data)
    msg="You have successfully registered a new Dispatch User!"
    return render(request,"registernewuser.html",{"msg":msg})
def postloginadmin (request) :
    email = request.POST.get('username')
    passwd =  request.POST.get('password')
    firebase=FirebaseApplication("https://neemeesh-trial-default-rtdb.firebaseio.com/", None)
    result=firebase.get('/Data/Signup/Admin', None) 
    flag=0
    tempmail='0'
    msg='0'
    for userid,user in result.items():
        if email==user['email'] :    
            flag=1
            # if there is no error then signin the user with given email and password
            try:
                user=authe.sign_in_with_email_and_password(email,passwd)
                session_id=user['idToken']
                request.session['uid']=str(session_id)
                return render(request , 'adminhome.html')
            except:
                tempmail=email
                msg="Invalid Password!!"
                return render(request,"adminlogin.html",{"msg":msg,"tempmail":tempmail})   
    if flag==0:       
        msg="Invalid Credentials!!Please ChecK your Data"
        return render(request,"adminlogin.html",{"msg":msg}) 
def postloginbooking(request) :
    email = request.POST.get('username')
    passwd =  request.POST.get('password')
    firebase=FirebaseApplication("https://neemeesh-trial-default-rtdb.firebaseio.com/", None)
    result=firebase.get('/Data/Signup/Booking', None)
    # db2 =  database.child("Data").child("Product").get()
    # print(db2.val())
    # for i in db2.each() :
    #     data1 = i.val()
    #     print(data1)
    #     company_name = data1["Company Name"]
    #     print(company_name)
    #     Product_name = data1["Product Name"]
    #     print(Product_name)
    #     company_address = data1["Address"]
    #     company_city = data1["City"]
    #     company_email = data1["Email id"]
    #     company_state = data1["State"]
        
    #     return render (request , "lh1.html" , {"company_name":company_name, "Product_name":Product_name , "company_address":company_address, "company_city":company_city , "company_email": company_email , "company_state":company_state })
    



    
    flag=0
    tempmail='0'
    msg='0'
    for userid,user in result.items():
        if email==user['email'] :    
            flag=1
            # if there is no error then signin the user with given email and password
            try:
                user=authe.sign_in_with_email_and_password(email,passwd)
                session_id=user['idToken']
                request.session['uid']=str(session_id)
                return render(request , 'lh1.html')
            except :
                tempmail=email
                msg="Invalid Password!!"
                return render(request,"bookinglogin.html",{"msg":msg,"tempmail":tempmail})   
    if flag==0:       
        msg="Invalid Credentials!!Please ChecK your Data"
        return render(request,"bookinglogin.html",{"msg":msg})
def postloginmis(request) :
    email = request.POST.get('username')
    passwd =  request.POST.get('password')
    firebase=FirebaseApplication("https://neemeesh-trial-default-rtdb.firebaseio.com/", None)
    result=firebase.get('/Data/Signup/MIS', None)
    flag=0
    tempmail='0'
    msg='0'
    for userid,user in result.items():
        if email==user['email'] :    
            flag=1
            # if there is no error then signin the user with given email and password
            try:
                user=authe.sign_in_with_email_and_password(email,passwd)
                session_id=user['idToken']
                request.session['uid']=str(session_id)
                return render(request , 'lh2.html')
            except :
                tempmail=email
                msg="Invalid Password!!"
                return render(request,"mislogin.html",{"msg":msg,"tempmail":tempmail})   
    if flag==0:       
        msg="Invalid Credentials!!Please ChecK your Data"
        return render(request,"mislogin.html",{"msg":msg})
def postlogindispatch(request) :
    email = request.POST.get('username')
    passwd =  request.POST.get('password')
    firebase=FirebaseApplication("https://neemeesh-trial-default-rtdb.firebaseio.com/", None)
    result=firebase.get('/Data/Signup/Dispatch', None)
    flag=0
    tempmail='0'
    msg='0'
    for userid,user in result.items():
        if email==user['email'] :    
            flag=1
            # if there is no error then signin the user with given email and password
            try:
                user=authe.sign_in_with_email_and_password(email,passwd)
                session_id=user['idToken']
                request.session['uid']=str(session_id)
                return render(request , 'lh3.html')
            except :
                tempmail=email
                msg="Invalid Password!!"
                return render(request,"dispatchlogin.html",{"msg":msg,"tempmail":tempmail})   
    if flag==0:      
        msg="Invalid Credentials!!Please ChecK your Data"
        return render(request,"dispatchlogin.html",{"msg":msg})
def registernewuser(request):
    return render(request , "registernewuser.html")
def registernewproduct(request):
    return render(request , "registernewproduct.html")
def lh1(request):
     pass
def lh2(request):
     pass  
def lh3(request):
     messages.success(request, 'You have successfully logged in')  
     pass
def postresetbooking (request) :
    email = request.POST.get("email")
    try :
        authe.send_password_reset_email(email)
        message  = "A email to reset password is succesfully sent"
        return render(request, "bookingreset.html", {"msg":message})
    except:
        message  = "Something went wrong, Please check the email you provided is registered or not"
        return render(request, "bookingreset.html", {"msg":message})
def postresetdispatch (request) :
    email = request.POST.get("email")
    try :
        authe.send_password_reset_email(email)
        message  = "A email to reset password is succesfully sent"
        return render(request, "postresetdispatch.html", {"msg":message})
    except:
        message  = "Something went wrong, Please check the email you provided is registered or not"
        return render(request, "postresetdispatch.html", {"msg":message})
def postresetmis (request) :
    email = request.POST.get("email")
    try :
        authe.send_password_reset_email(email)
        message  = "A email to reset password is succesfully sent"
        return render(request, "misreset.html", {"msg":message})
    except:
        message  = "Something went wrong, Please check the email you provided is registered or not"
        return render(request, "misreset.html", {"msg":message})  
def postresetadmin (request) :
    email = request.POST.get("email")
    try :
        authe.send_password_reset_email(email)
        message  = "A email to reset password is succesfully sent"
        return render(request, "postresetadmin.html", {"msg":message})
    except:
        message  = "Something went wrong, Please check the email you provided is registered or not"
        return render(request, "postresetadmin.html", {"msg":message})
def bookingforget (request) :
    return render (request ,"bookingreset.html")
def dispatchforget (request) :
    return render (request ,"dispatchreset.html")
def misforget (request) :
    return render (request ,"misreset.html")
def adminforget (request) :
    return render (request ,"postresetadmin.html")

def registernewproduct(request):
    return render(request , "registernewproduct.html")

def postregisternewproduct(request):
    
    firebase=FirebaseApplication("https://neemeesh-trial-default-rtdb.firebaseio.com/", None)
    Data={
        'Company id': request.POST.get('compid'),
        'Company Name': request.POST.get('compname'),
        'Product Name': request.POST.get('prodname'),
        'Email id': request.POST.get('compmail'),
        'Contact Number 1': request.POST.get('compcont1'),
        'Contact Number 2': request.POST.get('compcont2'),
        'Address': request.POST.get('compadd'),
        'City': request.POST.get('compcity'),
        'State': request.POST.get('compstate'),
        'Cost(per Kg)': request.POST.get('prodcostkg'),
        'Cost(per Box)': request.POST.get('prodcostbox'),
    }
    firebase.post('/Data/Product/', Data)
    msg="Product is Registered Successfully!"
    return render(request,"registernewproduct.html",{"msg":msg})
def usertable (request) :
    firebase=FirebaseApplication("https://neemeesh-trial-default-rtdb.firebaseio.com/", None)
    admindata=list(firebase.get("/Data/Signup/Admin",None).values())
    dispatchdata=list(firebase.get("/Data/Signup/Dispatch",None).values())
    bookingdata=list(firebase.get("/Data/Signup/Booking",None).values())
    misdata=list(firebase.get("/Data/Signup/MIS",None).values())
    #print(data[0]['address'])
    return render (request ,"usertable.html",{'admindata':admindata,'dispatchdata':dispatchdata,'bookingdata':bookingdata,'misdata':misdata,})


def adminupdate(request)  :
    return  render(request ,"adminupdate.html" )


def postadminupdate (request) :
    user_type = request.POST.get("usertype")
    old_email = request.POST.get("email")
    old_user_name=request.POST.get("username")
    

    db = database.child("Data").child("Signup").child(user_type).get()

    new_address = request.POST.get("newaddress")
    new_city = request.POST.get("newcity")
    new_country = request.POST.get("newcountry")
    new_email = request.POST.get("newemail")
    new_name = request.POST.get("newname")
    new_phone= request.POST.get("newphone")
    new_pincode = request.POST.get("newpincode")
    new_state = request.POST.get("newstate")

    for i in db.each() :
        if i.val()['email']==old_email : 
            if i.val()['name']==old_user_name :
                database.child("Data").child("Signup").child(user_type).child(i.key()).update({
                "address" : new_address ,
                 "city"   : new_city ,
                 "country": new_country ,
                 "email"  : new_email ,
                 "name"   : new_name ,
                 "phone"  : new_phone ,
                 "pincode": new_pincode ,
                 "state"  :  new_state 
                })
                return render(request , "adminupdate.html" , {"msg1" : "The details of the required user have been updated !!"})
            else :
                msg1 = "This Name does not match with the give Email!"
                return render(request , "adminupdate.html" , {"msg1" : msg1})
        else :
            msg1 = "This email is not Registered in our database!"
            return render(request , "adminupdate.html" , {"msg1" : msg1})

def deleteuser(request)  :
    return render(request,"deleteuser.html")

def postdeleteuser(request):
    user_type = request.POST.get("usertype")
    email = request.POST.get("email")
    db = database.child("Data").child("Signup").child(user_type).get()
    for user in db.each() :
        if user.val()['email']==email : 
            database.child("Data").child("Signup").child(user_type).child(user.key()).remove()
            user = auth.get_user_by_email(email)
            auth.delete_user(user.uid)
            return render(request , "deleteuser.html" , {"msg1" : "The User is deleted succesfully!"})
    return render(request , "deleteuser.html" , {"msg1" : "User not Found!"})

def productdetails(request):
    firebase=FirebaseApplication("https://neemeesh-trial-default-rtdb.firebaseio.com/", None)
    compdetails=list(firebase.get("/Data/Product",None).values())
    return render (request ,"productdetails.html",{'compdetails':compdetails})