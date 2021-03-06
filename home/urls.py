from django.contrib import admin
from django.urls import path
from  home import views
urlpatterns = [
     path("",views.index,name= 'home'),
     path("about",views.about,name= 'about'), 
     path("services",views.services,name= 'services'),
     path("contact",views.contact,name= 'contact'),
     path("prelogin",views.prelogin,name= 'prelogin'),
     path("adminlogin/",views.adminlogin,name= 'adminlogin'),
     path("dispatchlogin/",views.dispatchlogin,name= 'dispatchlogin'),
     path("mislogin/",views.mislogin,name= 'mislogin'),
     path("bookinglogin/",views.bookinglogin,name= 'bookinglogin'),
     path("registeradmin/" , views.registeradmin , name='registeradmin'),
     path("registerbooking/" , views.registerbooking , name='registerbooking'),
     path("registerdispatch/" , views.registerdispatch , name='registerdispatch'),
     path("registermis/" , views.registermis , name='registermis'),
     path("registernewuser/" , views.registernewuser , name='registernewuser'),
     path("registernewcompany/" , views.registernewcompany , name='registernewcompany'),
     path("postregisternewcompany/" , views.postregisternewcompany , name='postregisternewcompany'),
     path("postregisternewproduct/" , views.postregisternewproduct , name='postregisternewproduct'),
     path("registernewproduct/" , views.registernewproduct , name='registernewproduct'),
     path("postregisteradmin/" , views.postregisteradmin , name='postregisteradmin'),
     path("postregisterbooking/" , views.postregisterbooking , name='postregisterbooking'),
     path("postregistermis/" , views.postregistermis , name='postregistermis'),
     path("postregisterdispatch/" , views.postregisterdispatch , name='postregisterdispatch'),
     path("login/" , views.login ,name='login' ),
     path("lh1/" , views.lh1 ,name='lh1' ),
     path("lh2/" , views.lh2 ,name='lh2' ),
     path("lh3/" , views.lh3 ,name='lh3' ),
     path("postloginadmin/" , views.postloginadmin ,name='postloginadmin' ),
     path("postloginbooking/" , views.postloginbooking ,name='postloginbooking' ),
     path("postloginmis/" , views.postloginmis ,name='postloginmis' ),
     path("postlogindispatch/" , views.postlogindispatch ,name='postlogindispatch' ),
     path("bookingforget/" , views.bookingforget ,name='bookingforget' ),
     path("dispatchforget/" , views.dispatchforget ,name='dispatchforget' ),
     path("misforget/" , views.misforget ,name='misforget' ),
     path("adminforget/" , views.adminforget ,name='adminforget' ),
     path("postresetbooking/" , views.postresetbooking ,name='postresetbooking' ),
     path("postresetdispatch/" , views.postresetdispatch ,name='postresetdispatch' ),
     path("postresetmis/" , views.postresetmis ,name='postresetmis' ),
     path("postresetadmin/" , views.postresetadmin ,name='postresetadmin' ),
     path("usertable/" , views.usertable ,name='usertable' ),
     path("checkuserupdate/" , views.checkuserupdate ,name='checkuserupdate' ),
     path("postcheckuserupdate/" , views.postcheckuserupdate ,name='postcheckuserupdate' ),
     path("postdeleteuser/" , views.postdeleteuser ,name='postuserdelete' ),
     path("deleteuser/" , views.deleteuser ,name='deleteuser' ),
     path("productdetails/" , views.productdetails ,name='productdetails' ),
     path("bookingorder/" , views.bookingorder ,name='bookingorder' ),
     path("postbookingorder/" , views.postbookingorder ,name='postbookingorder' ),
     path("postuserupdate/" , views.postuserupdate ,name='postuserupdate' ),
]