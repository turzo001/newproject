from django.urls import path ,include
from app import views

urlpatterns = [
    
    path('chatbox/', views.chatbox,name='chatbox'),
    path('contractlist/', views.contractlist,name='contractlist'),
    path('emailbox/', views.emailbox,name='emailbox'),
    path('emailread/', views.emailread,name='emailread'),
    path('filemanager/', views.filemanager,name='filemanager'),
    path('fullcalender/', views.fullcalender,name='fullcalender'),
    path('invoice/', views.invoice,name='invoice'),
    path('todo/', views.todo,name='todo'),
    
    #basic
    path('fotgotpass/', views.forgotpass,name='forgotpass'),
    path('login/', views.login,name='login'),
    path('register/', views.register,name='register'),
    path('resetpass/', views.resetpass,name='resetpass'),
    path('forgotpass/', views.forgotpass,name='forgotpass'),
    
    #boxed
    path('boxedlogin/', views.boxedlogin,name='boxedlogin'),
    path('boxedregister/', views.boxedregister,name='boxedregister'),
    path('boxedresetpass/', views.boxedresetpass,name='boxedresetpass'),
    path('boxedforgetpass/', views.boxedforgetpass,name='boxedforgetpass'),

    #cover
    path('coverlogin', views.coverlogin,name='coverlogin'),
    path('coverregister', views.coverregister,name='coverregister'),
    path('coverresetpass', views.coverresetpass,name='coverresetpass'),
    path('coverforgetpass', views.coverforgetpass,name='coverforgetpass'),
    
    path('chartapex/', views.chartapex,name='chartapex'),
    path('chartjs/', views.chartjs,name='chartjs'),
    
    path('componentaccording/', views.componentaccording,name='componentaccording'),
    path('componentalerts/', views.componentalerts,name='componentalerts'),
    path('componentbadges/', views.componentbadges,name='componentbadges'),
    path('componentcards/', views.componentcards,name='componentcards'),
    path('componentbuttons/', views.componentbuttons,name='componentbuttons'),
    path('componentcarousels/', views.componentcarousels,name='componentcarousels'),
    path('componentlightbox/', views.componentlightbox,name='componentlightbox'),
    path('componentlistgroups/', views.componentlistgroups,name='componentlistgroups'),
    path('componentmediaobject/', views.componentmediaobject,name='componentmediaobject'),
    path('componentmodals/', views.componentmodals,name='componentmodals'),
    path('componentnavstabs/', views.componentnavstabs,name='componentnavstabs'),
    path('componentnotifications/', views.componentnotifications,name='componentnotifications'),
    path('componentpaginations/', views.componentpaginations,name='componentpaginations'),
    path('componentpopoverstooltips/', views.componentpopoverstooltips,name='componentpopoverstooltips'),
    path('componentprogressbars/', views.componentprogressbars,name='componentprogressbars'),
    path('componentspinners/', views.componentspinners,name='componentspinners'),
    
    path('ecommerceaddprod/', views.ecommerceaddprod,name='ecommerceaddprod'),
    path('ecommercecustomerdetails/', views.ecommercecustomerdetails,name='ecommercecustomerdetails'),
    path('ecommercecustomers/', views.ecommercecustomers,name='ecommercecustomers'),
    path('ecommerceorderdetails/', views.ecommerceorderdetails,name='ecommerceorderdetails'),
    path('ecommerceorders', views.ecommerceorders,name='ecommerceorders'),
    path('ecommerceprod/', views.ecommerceprod,name='ecommerceprod'),
    
    path('faq/', views.faq,name='faq'),
    
    path('formdatetimepicks/', views.formdatetimepicks,name='formdatetimepicks'),
    path('formelements/', views.formelements,name='formelements'),
    path('formfileupload/', views.formfileupload,name='formfileupload'),
    path('forminputgroup/', views.forminputgroup,name='forminputgroup'),
    path('formlayout/', views.formlayout,name='formlayout'),
    path('formradiosandcheckboxes/', views.formradiosandcheckboxes,name='formradiosandcheckboxes'),
    path('formrepeater/', views.formrepeater,name='formrepeater'),
    path('formselect2/', views.formselect2,name='formselect2'),
    path('formvalidations/', views.formvalidations,name='formvalidations'),
    path('formwizard/', views.formwizard,name='formwizard'),
    
    path('iconsboxicons/', views.iconsboxicons,name='iconsboxicons'),
    path('iconsfeathericons/', views.iconsfeathericons,name='iconsfeathericons'),
    path('iconslineicons/', views.iconslineicons,name='iconslineicons'),
    
    path('index/', views.index,name='index'),
    
    path('googlemap/', views.googlemap,name='googlemap'),
    path('vectormap/', views.vectormap,name='vectormap'),

    path('pagescomingsoon/', views.pagescomingsoon,name='pagescomingsoon'),
    path('pageseditprofile/', views.pageseditprofile,name='pageseditprofile'),
    
    path('pageseror403/', views.pageseror403,name='pageseror403'),
    path('pageseror404/', views.pageseror404,name='pageseror404'),
    path('pageseror500/', views.pageseror500,name='pageseror500'),
    path('pagesstarterpage/', views.pagesstarterpage,name='pagesstarterpage'),
    
    path('pricingtable/', views.pricingtable,name='pricingtable'),
    
    path('tablebasic/', views.tablebasic,name='tablebasic'),
    path('tabledatable/', views.tabledatable,name='tabledatable'),
    
    path('timeline/', views.timeline,name='timeline'),
    path('userprofile/', views.userprofile,name='userprofile'),
    path('widgetdata/', views.widgetdata,name='widgetdata'), 
    path('widgetstatic/', views.widgetstatic,name='widgetstatic'),       

]
