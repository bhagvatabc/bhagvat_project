from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_protect
from django.http import StreamingHttpResponse
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import csrf_exempt, csrf_protect
# Create your views here.
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render_to_response
from myapp.models import *
import myapp.views
from myapp.views import *
import json
from django.db.models import F
import simplejson
import json as simplejson
import os
import sys
from urllib2 import urlopen, HTTPError
import urllib
from urllib2 import Request, urlopen, URLError
import requests
from requests import *
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.http import JsonResponse
from django.db.models import Q
import operator
import dpath.util
import random
import csv
import string
from pyfcm import FCMNotification
from rest_framework.authtoken.models import Token#new
from rest_framework.decorators import api_view#new
import smtplib
#2017
@api_view(['POST','GET'])
@csrf_exempt
def test(request):
 data = json.loads(request.body)
 return HttpResponse("done")
#

@api_view(['POST','GET'])
@csrf_exempt
def getLocationListAPI(request):
 data = json.loads(request.body)
 locationsData = json.loads(serializers.serialize("json",Location.objects.all()))
 locations = []
 for location in locationsData:
   locations.append(location["fields"])
 c1 = {"status":"success","message":"Locations found successfully","locations":locations,"count":len(locations)}
 return HttpResponse(json.dumps(c1),content_type="application/json")

@api_view(['POST','GET'])
@csrf_exempt
def addUpdateLocationAdminAPI(request):
 data = json.loads(request.body)
 if (data["password"] == "Lets89308805786"):
   p=Location.objects.update_or_create(defaults = data["location"], pin = data["location"]["pin"])
   LocationJson = json.loads(serializers.serialize("json",[p[0],]))[0]["fields"]
   if(p[1]==False):
    c1={"status":"success","message":"Location updated successfully","location":LocationJson}
   else:
    c1={"status":"success","message":"Location added successfully","location":LocationJson}
 else:
  c1={"status":"error","message":"Incorrect password"}
 return HttpResponse(json.dumps(c1),content_type="application/json")

@api_view(['POST','GET'])
@csrf_exempt
def deleteLocationAdminAPI(request):
 data = json.loads(request.body)
 if (data["password"] == "Lets89308805786"):
   p=Location.objects.filter(pincode = data["location"]["pincode"])
   if(p.count() == 0):
    c1={"status":"error","message":"Location does not exist"}
   else:
    p.delete()
    c1={"status":"success","message":"Location deleted successfully"}
 else:
  c1={"status":"error","message":"Incorrect password"}
 return HttpResponse(json.dumps(c1),content_type="application/json")

@api_view(['POST','GET'])
@csrf_exempt
def sendQueryAPI(request):
 data = json.loads(request.body)

 TO = ['d2rlabs.contree@gmail.com','contact@contree.awsapps.com','dsaini07@gmail.com']
 FROM = 'bhagvatsr@gmail.com'
 SUBJECT = data["userName"] + "|" + data["userNumber"] + "|" + data["issueFacing"]
 TEXT =""" 
 Email: %s
 Query: %s 
 Model: %s
 Version: %s
 """ % (data["userEmail"],data["query"],data["model"],data["version"])
 # Prepare actual message
 message = """From: %s\nTo: %s\nSubject: %s\n\n%s
 """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
 try:
  server = smtplib.SMTP('smtp.gmail.com',587)
  server.ehlo()
  server.starttls()
  server.ehlo()
  server.login('d2rlabs.contree@gmail.com','mwjolkeglvnvlwry')
  server.sendmail(FROM, TO, message)
  server.close()         
  status = "success"
 except SMTPException:
  status = "error"
 c1={"status":status}
 return HttpResponse(json.dumps(c1),content_type="application/json")

@api_view(['POST','GET'])
@csrf_exempt
def merchantOfringAPI(request):
 return HttpResponse(json.dumps({"merchant_data":json.loads(serializers.serialize("json",[Merchant.objects.get(number=json.loads(request.body)["merchantNumber"]),]))[0]["fields"]}),content_type="application/json")

@api_view(['POST','GET'])
@csrf_exempt
def placeOrderAPI(request):
 return HttpResponse(json.dumps(placeOrder(json.loads(request.body))),content_type="application/json")

def updateOrderObject(data):
 updateOrder_data  = Userorder.objects.update_or_create(defaults = data,orderid=data["orderid"])
 updateOrder_data = json.loads(serializers.serialize("json",[updateOrder_data[0],]))[0]["fields"]
 c1={"updateorder_data":updateOrder_data}
 return c1

@api_view(['POST','GET'])
@csrf_exempt
def updateOrderAPI(request):
 c1= updateOrderObject(json.loads(request.body))
 return HttpResponse(json.dumps(c1),content_type="application/json")

@api_view(['POST','GET'])
@csrf_exempt
def getUserVPAUserAPI(request):
 data = json.loads(request.body)
 try:
    vpa = User.objects.get(number = data["friendNumber"]).vpa
    if (vpa == None):
      c1 = {"status":"error","message":"User found but VPA not registered by user yet"}
    else:
      c1 = {"status":"success","message":"VPA found successfully","friendVPA":str(vpa)}
 except:
    c1 = {"status":"error","message":"Requested user not registered on Contree"}
 return HttpResponse(json.dumps(c1),content_type="application/json")
#@api_view(['POST','GET'])
@csrf_exempt
def getMerchantOrderAPI(request):
 data = json.loads(request.body)
 merchant_no=data["merchantNumber"]
 orderIDList=data["orderID"]
 print orderIDList
 orderIDList =[x.encode("utf-8")for x in orderIDList]
 orderData= Userorder.objects.filter(merchantnumber=merchant_no).exclude(orderid__in=orderIDList)
 print orderData 
 userorder_data = json.loads(serializers.serialize("json",orderData))
 print userorder_data
 return HttpResponse(json.dumps(userorder_data),content_type="application/json")

@api_view(['POST','GET'])
@csrf_exempt
def updateOrderStatusAPI(request):
 data = json.loads(request.body)
 order_id=data["orderid"]
 merchantNo=data["merchantnumber"]
 order_status=data["status"]
 orderdata=Userorder.objects.update_or_create(orderid = order_id,defaults=data)
 print orderdata[1]
 if orderdata[1]== False:
  return HttpResponse("Updated successfully")

#@api_view(['POST','GET'])
@csrf_exempt
def addMerchantOfferingAPI(request):
 data = json.loads(request.body)
 merchant_no = data["merchantnumber"]
 merchant_offerings=data["merchantOfferings"]
 merchantOffering = Merchant.objects.update_or_create(number = merchant_no,defaults=merchant_offerings)
 print merchantOffering[1]
 if merchantOffering[1] == False:
  return HttpResponse("Updated successfully")

@api_view(['POST','GET'])
@csrf_exempt
def getUserOrdersAPI(request):
 data = json.loads(request.body)
 userNumber=data["userNumber"]
 orderIDList = data["orderIDList"]
 print orderIDList
 idQuery = reduce(operator.or_,(Q(orderID = orderid)for orderid in orderIDList))
 print idQuery
 userorder_data = Userorder.objects.filter(idQuery,userNumber=userNumber).exclude(status = "-1")
 userorder_data = json.loads(serializers.serialize("json",userorder_data))
 ordersArray = []
 for order in userorder_data:
  ordersArray.append(order["fields"])
 if (len(ordersArray) > 0):
   c1={"orders":ordersArray,"status":"success","count":len(ordersArray)}
 else:
   c1={"message":"no orders found","status":"error"}
 return HttpResponse(json.dumps(c1),content_type="application/json")

def getdynamicValue():
 return json.loads(serializers.serialize("json",DynamicValue.objects.all()))[0]["fields"]

def getNotifications():
 notifications = []
 for notification in json.loads(serializers.serialize("json",PushNotification.objects.all())):
  notifications.append(notification["fields"])
 return notifications

@api_view(['POST','GET'])
@csrf_exempt
def updateHelperAPI(request):
 data = json.loads(request.body)
 p = Helper.objects.update_or_create(defaults = data,number = data["number"], merchantNumber = data["merchantNumber"])
 c1={"status":"success","message":"updated successfully","helperValue":json.loads(serializers.serialize("json",[p[0],]))[0]["fields"]}
 return HttpResponse(json.dumps(c1),content_type="application/json")


@api_view(['POST','GET'])
@csrf_exempt
def updateDynamicValue(request):
 data = json.loads(request.body)
 if(data["password"]=="Lets89308805786"):
  body = data["body"]
  if(body["identifier"]=="contree789"):
   p = DynamicValue.objects.update_or_create(defaults = body,identifier=body["identifier"])
   c1={"status":"success","message":"updated successfully","dynamicValue":json.loads(serializers.serialize("json",[p[0],]))[0]["fields"]}
  else:
   c1={"status":"error","message":"Incorrect identifier"}
 else:
  c1={"status":"error","message":"Incorrect password"}
 return HttpResponse(json.dumps(c1),content_type="application/json")


@api_view(['POST','GET'])
@csrf_exempt
def sync(request):
 syncExpenses(json.loads(request.body)["syncList"])
 return HttpResponse("ok")


@api_view(['POST','GET'])
@csrf_exempt
def getAllMerchantsAPI(request):
 data = json.loads(request.body)
 merchants = json.loads(serializers.serialize("json",Merchant.objects.filter(isVerified = data["isVerified"], status = data["status"])))
 finalMerchants = []
 for merchant in merchants:
  finalMerchants.append(merchant["fields"])
 c1={"status":"success","merchants":finalMerchants,"count":len(finalMerchants)}
 return HttpResponse(json.dumps(c1),content_type="application/json")

@api_view(['POST','GET'])
@csrf_exempt
def getMerchantsInLocationAPI(request):
 data = json.loads(request.body)
 merchants = json.loads(serializers.serialize("json",Merchant.objects.filter(isVerified = "yes", status = "1", isBlocked = "no", pin = data["pin"])))
 finalMerchants = []
 for merchant in merchants:
  finalMerchants.append(merchant["fields"])
 c1={"status":"success","merchants":finalMerchants,"count":len(finalMerchants)}
 return HttpResponse(json.dumps(c1),content_type="application/json")
@api_view(['POST','GET'])
@csrf_exempt
def getMerchantUserAPI(request):
 data = json.loads(request.body)
 try:
   merchant = json.loads(serializers.serialize("json",[Merchant.objects.get(number = data["merchantNumber"]),]))[0]["fields"]
   c1={"status":"success","message":"Merchant fetched successfully","merchant":merchant}
 except:
   c1={"status":"error","message":"Error fetching merchant"}
 return HttpResponse(json.dumps(c1),content_type="application/json")

def syncExpenses(syncList):
 for entry in syncList:
  Expensedetails.objects.update_or_create(defaults = entry,id1 = entry["id1"], object__contains = entry["object"].split("##")[0], expenseVersion = entry["expenseVersion"])

def connectFCM(category,body,idsList,isSilent):
  url = "https://fcm.googleapis.com/fcm/send"
  matter = {"category":category,"body":body, "isSilent":isSilent}
  data = {"data":matter,"registration_ids":idsList}
  headers = {'content-type':"application/json",'authorization': "key=AIzaSyAyr0ors7D1lVnhescbztbu7Z8F1pKqwEw"}
  response = requests.post(url, data=json.dumps(data), headers=headers)
  print response.text
  return json.loads(response.text)

def connectFCMMerchant(category,body,idsList,isSilent):
  url = "https://fcm.googleapis.com/fcm/send"
  matter = {"category":category,"body":body, "isSilent":isSilent}
  data = {"data":matter,"registration_ids":idsList}
  headers = {'content-type':"application/json",'authorization': "key=AIzaSyD4KKKdU3Vs9-l5aInS_fArrs33zfpcRcQ"}
  response = requests.post(url, data=json.dumps(data), headers=headers)
  print response.text
  return json.loads(response.text)

def connectFCMHelper(category,body,idsList,isSilent):
  url = "https://fcm.googleapis.com/fcm/send"
  matter = {"category":category,"body":body, "isSilent":isSilent}
  data = {"data":matter,"registration_ids":idsList}
  headers = {'content-type':"application/json",'authorization': "key=AIzaSyA7S7_ZfEyNCaBddj4QTL9eCkeTN9pBTPg"}
  response = requests.post(url, data=json.dumps(data), headers=headers)
  print "helper" + response.text
  return json.loads(response.text)

def sendRemindMessage(name,number,amount):
 message = "Your friend " + name + " asked you to pay Rs " + amount + " on Contree. Download from https://goo.gl/sX2Be5 #ShareExpenses"
 return connectMessage(number,message)

def sendOTPMessage(otp,number):
 message =  otp + " is One Time Password (OTP) for your Contree login verification. Please do not share it with anyone. WelcomeBack"
 return connectMessage(number,message)

@api_view(['POST','GET'])
@csrf_exempt
def sendPushNotification(request):
 data = json.loads(request.body)
 notification=data["notification"]
 isSilent = data["isSilent"]
 category = data["category"]
 if (data["password"] == "Lets89308805786"):
  fcmTokenList =[x.encode("utf-8")for x in User.objects.exclude(fcmToken = "").values_list('fcmToken',flat=True)]
  subLists = [fcmTokenList[i:i+1000] for i in range(0,len(fcmTokenList),1000)]
  counter = 0
  for subList in subLists:
   counter = counter + int(connectFCM(category,notification,subList,isSilent)["success"])
  c1={"status":"success","message":"Notifications sent successfully","TotalUsers":User.objects.exclude(fcmToken = "").count(),"NotificationsSent":counter}
  PushNotification.objects.update_or_create(defaults = notification,notificationID = notification["notificationID"])
 else:
  c1={"status":"error","message":"Incorrect password"}
 return HttpResponse(json.dumps(c1),content_type="application/json")


@api_view(['POST','GET'])
@csrf_exempt
def pushDynamicValues(request):
 data = json.loads(request.body)
 body = data["body"]
 isSilent = data["isSilent"]
 category = data["category"]
 if (data["password"] == "Lets89308805786"):
  fcmTokenList =[x.encode("utf-8")for x in User.objects.exclude(fcmToken = "").values_list('fcmToken',flat=True)]
  subLists = [fcmTokenList[i:i+1000] for i in range(0,len(fcmTokenList),1000)]
  counter = 0
  for subList in subLists:
   counter = counter + int(connectFCM(category,body,subList,isSilent)["success"])
  c1={"status":"success","message":"Notifications sent successfully","TotalUsers":User.objects.exclude(fcmToken = "").count(),"NotificationsSent":counter}
  DynamicValue.objects.update_or_create(defaults = body,identifier=body["identifier"])
 else:
  c1={"status":"error","message":"Incorrect password"}
 return HttpResponse(json.dumps(c1),content_type="application/json")

def connectMessage(number,message):
 url = ("http://alerts.solutionsinfini.com/api/v3/index.php?method=sms&api_key=A2da30c3f0e3f933485c8a7545dcaf895&to="+number+"&sender=Contri&message="+message)
 return json.loads(requests.get(url).text)["status"]

@api_view(['POST','GET'])
@csrf_exempt
def deleteUser(request):
  number = json.loads(request.body)["number"]
  querySet = User.objects.filter(number = number)
  if (querySet.count() == 0):
   c1={"status":"error","message":"User does not exist"}
  else:
   querySet.delete()
   c1={"status":"success","message":"User deleted"}
  return HttpResponse(json.dumps(c1),content_type="application/json")

@csrf_exempt
def deleteExpense(request):
  data = json.loads(request.body)
  id1 = data["id1"]
  object = data["object"].split("##")[0]
  expenseVersion = data["expenseVersion"]
  querySet = Expensedetails.objects.filter(id1 = id1, object__contains = object, expenseVersion = expenseVersion)
  if (querySet.count() == 0):
   c1={"status":"error","message":"Expense does not exist2"}
  else:
   querySet.delete()
   c1={"status":"success","message":"Expense deleted"}
  return HttpResponse(json.dumps(c1),content_type="application/json")
@api_view(['POST','GET'])
@csrf_exempt
def deleteAllExpenses(request):
  data = json.loads(request.body)
  if (data["password"] == "Lets89308805786"):
   querySet = Expensedetails.objects.all()
   if (querySet.count() == 0):
    c1={"status":"error","message":"Expenses do not exist"}
   else:
    querySet.delete()
    c1={"status":"success","message":"Expenses deleted"}
  return HttpResponse(json.dumps(c1),content_type="application/json")

@api_view(['POST','GET'])
@csrf_exempt
def DeleteExpenseAllVersions(request):
  data = json.loads(request.body)
  id1 = data["id1"]
  object = data["object"].split("##")[0]
  querySet = Expensedetails.objects.filter(id1 =id1 , object__contains = object )
  if (querySet.count() == 0):
   c1={"status":"error","message":"Expense does not exist1"}
  else:
   querySet.delete()
   c1={"status":"success","message":"Expense deleted"}
  return HttpResponse(json.dumps(c1),content_type="application/json")

@api_view(['POST','GET'])
@csrf_exempt
def remindAPI(request):
 comingJson = json.loads(request.body)
 memberList = comingJson["membersList"]
 whoRemindedName = comingJson["userName"] + " "
 whoRemindedNumber = comingJson["userNumber"]
 numberList =[]
 for member in memberList:
  numberList.append(member["number"])
 
 idQuery = reduce(operator.or_,(Q(number = number)for number in numberList))
 users =  User.objects.filter(idQuery)
 users = json.loads(serializers.serialize("json",users)) 
 userList = []
 savedNumberList = []
 for user in users:
  user2 = (user)["fields"]
  userList.append(user2)
  savedNumberList.append(user2["number"])
 
 counter = 0
 for member in memberList:
   requestNumber = member["number"]
   amount = member["amount"]
   if (requestNumber not in savedNumberList):
    result =  sendRemindMessage(whoRemindedName,requestNumber,amount)
    if (result == "OK"):
     counter = counter + 1
   else:
    for user in userList:
     if (user["number"] == requestNumber): 
      tokenValue = user["fcmToken"]
    fcmList = []
    fcmList.append(tokenValue)
    fcmList =[x.encode("utf-8")for x in fcmList]
    message = "asked you to pay Rs " + amount
    body = {"message":message,"whoRemindedName":whoRemindedName,"whoRemindedNumber":whoRemindedNumber}
    result = connectFCM("remind", body, fcmList,"no")
    if (result["success"] == 1):
     counter = counter + 1
 
 if (counter == 0):
  c1={"status":"error","message":"Could not send reminders. Try later"}
 else:
  c1={"status":"success","message":"Reminders sent successfully","count":counter}
 return HttpResponse(json.dumps(c1),content_type="application/json")

def sendFCMorMessage(numberList,fcmTitle,fcmBody,messageBody):
 idQuery = reduce(operator.or_,(Q(number = number)for number in numberList))
 users =  User.objects.filter(idQuery)
 users = json.loads(serializers.serialize("json",users))
 userList = []
 savedNumberList = []
 for user in users:
  user2 = (user)["fields"]
  userList.append(user2)
  savedNumberList.append(user2["number"])
 counter = 0
 fcmList = []
 for number in numberList:
   if (number not in savedNumberList):
    connectMessage(number,messageBody)
   else:
    for user in userList:
     if(user["number"] == number):
      fcmList.append(user["fcmToken"])
 fcmList =[x.encode("utf-8")for x in fcmList]
 connectFCM(fcmTitle, fcmBody, fcmList)


@api_view(['POST','GET'])
@csrf_exempt
def verifyReferralAPI(request):
 print "inside api call"
 print request.method
 data= request.body
 data = json.loads(data)
 referralInput=data["referralInput"]
 mobile_number = data["userNumber"]
 print data
 count  = User.objects.filter(referralCode = referralInput).count()
 if (count > 0):
   user = User.objects.filter(referralCode = referralInput)
   userJson = serializers.serialize("json",user)
   userJson = json.loads(userJson)[0]["fields"]
   referredFromName = userJson["name"]
   referredFromNumber = userJson["number"]
   referralCount = int(userJson["referralCount"])
   referralCount = referralCount + 1
   User.objects.filter(referralCode = referralInput).update(referralCount = referralCount)
   
   referredFromString = referredFromName + ":" + referredFromNumber
   User.objects.filter(number = mobile_number).update(referredFrom = referredFromString) 
   cuser = User.objects.filter(number = mobile_number)
   cuserJson = serializers.serialize("json",cuser)
   cuserJson = json.loads(cuserJson)[0]["fields"]  
   c1={"status":"success","message":"Referral successful","user":cuserJson}
   #connectFCM("referral", , ,"no")
 else: 
   c1={"status":"error","message":"Invalid referral"}
 return HttpResponse(json.dumps(c1),content_type="application/json")

@api_view(['POST','GET'])
@csrf_exempt
def updateUserAPI(request):
 data = json.loads(request.body)
 p=User.objects.update_or_create(defaults= data ,number = data["number"])
 UserJson = json.loads(serializers.serialize("json",[p[0],]))[0]["fields"]
 if(p[1]==False):
  c1={"status":"success","message":"User updated successfully","user":UserJson}
 else:
  p[0].delete()
  c1={"status":"error","message":"User does not exist"}
 return HttpResponse(json.dumps(c1),content_type="application/json")

@api_view(['POST','GET'])
@csrf_exempt
def updateMerchantAPI(request):
 data = json.loads(request.body)
 p=Merchant.objects.update_or_create(defaults= data ,number = data["number"])
 MerchantJson = json.loads(serializers.serialize("json",[p[0],]))[0]["fields"]
 if(p[1]==False):
  c1={"status":"success","message":"Merchant updated successfully","merchant":MerchantJson}
 else:
  p[0].delete()
  c1={"status":"error","message":"Merchant does not exist"}
 return HttpResponse(json.dumps(c1),content_type="application/json")

@api_view(['POST','GET'])
@csrf_exempt
def updateHelperAPI(request):
 data = json.loads(request.body)
 defaultsData = {"fcmToken":data["fcmToken"]}
 p=Helper.objects.update_or_create(defaults = defaultsData, number = data["number"], merchantNumber = data["merchantNumber"])
 HelperJson = json.loads(serializers.serialize("json",[p[0],]))[0]["fields"]
 if(p[1]==False):
  c1={"status":"success","message":"Helper updated successfully","helper":HelperJson}
 else:
  p[0].delete()
  c1={"status":"error","message":"Helper does not exist"}
 return HttpResponse(json.dumps(c1),content_type="application/json")

@api_view(['POST','GET'])
@csrf_exempt
def addUpdateHelperMerchantAPI(request):
 data = json.loads(request.body)
 p=Helper.objects.update_or_create(defaults = data ,number = data["number"], merchantNumber = data["merchantNumber"])
 HelperJson = json.loads(serializers.serialize("json",[p[0],]))[0]["fields"]
 if(p[1]==False):
  c1={"status":"success","message":"Helper updated successfully","helper":HelperJson}
 else:
  p[0].fcmToken = " "
  p[0].save()
  c1={"status":"success","message":"Helper added successfully","helper":HelperJson}
 return HttpResponse(json.dumps(c1),content_type="application/json")

@api_view(['POST','GET'])
@csrf_exempt
def deleteHelperMerchantAPI(request):
 data = json.loads(request.body)
 p=Helper.objects.filter(number = data["number"], merchantNumber = data["merchantNumber"])
 if(p.count() == 0):
  c1={"status":"error","message":"Helper does not exist for this merchant"}
 else:
  p.delete()
  c1={"status":"success","message":"Helper deleted successfully"}
 return HttpResponse(json.dumps(c1),content_type="application/json")

@api_view(['POST','GET'])
@csrf_exempt
def refreshOrdersMerchantAPI(request):
 data = json.loads(request.body)
 merchantNumber=data["merchantNumber"]
 orderIDList = data["orderIDList"]
 ordersArray = []
 if (len(orderIDList) > 0):
   updateData = json.loads(serializers.serialize("json",Userorder.objects.filter(orderID__in = orderIDList,merchantNumber = merchantNumber).exclude(status = "0")))
   for order in updateData:
     ordersArray.append(order["fields"])
 
 newData = json.loads(serializers.serialize("json",Userorder.objects.filter(merchantNumber = merchantNumber,status = "-1")))
 for order in newData:
   ordersArray.append(order["fields"])
 c1={"orders":ordersArray,"status":"success","count":len(ordersArray)}
 return HttpResponse(json.dumps(c1),content_type="application/json")

@api_view(['POST','GET'])
@csrf_exempt
def refreshOrdersHelperAPI(request):
 data = json.loads(request.body)
 merchantNumber=data["merchantNumber"]
 orderIDList = data["orderIDList"]
 status = data["status"]
 ordersArray = []
 if (len(orderIDList) > 0):
   idQuery = reduce(operator.or_,(Q(orderID = orderid)for orderid in orderIDList))
   updateData = json.loads(serializers.serialize("json",Userorder.objects.filter(idQuery,merchantNumber = merchantNumber).exclude(status = status)))
   for order in updateData:
     ordersArray.append(order["fields"])
   newData = json.loads(serializers.serialize("json",Userorder.objects.filter(merchantNumber = merchantNumber,status = status).exclude(idQuery)))
 else:
   newData = json.loads(serializers.serialize("json",Userorder.objects.filter(merchantNumber = merchantNumber,status = status)))
 for order in newData:
   ordersArray.append(order["fields"])
 c1={"orders":ordersArray,"status":"success","count":len(ordersArray)}
 return HttpResponse(json.dumps(c1),content_type="application/json")


@api_view(['POST','GET'])
@csrf_exempt
def updateOrderMerchantAPI(request):
 order = json.loads(request.body)
 if(order["status"]=="1" and float(order["refundValue"].split(":")[1]) > 0 and order["refundValue"].split(":")[0] == "P"):
    requestID = random.randint(1000000000,9999999999)
    consumerID = json.loads(serializers.serialize("json",User.objects.filter(number = order["userNumber"])))[0]["fields"]["consumerID"]
    refundJson = {"amount":float(order["refundValue"].split(":")[1]),"consumer_id":consumerID,"request_id": str(requestID)}
    c2 = json.loads(getWalletResponse('https://shmart.in/wallet/v1/credits/general',"post",refundJson))
    if(c2["status"] == "success"):
      order["refundValue"] = "S:" + order["refundValue"].split(":")[1]

 p=Userorder.objects.update_or_create(defaults = order, orderID = order["orderID"])
 OrderJson = json.loads(serializers.serialize("json",[p[0],]))[0]["fields"]
 if(p[1]==False):
  c1={"status":"success","message":"Order updated successfully","order":OrderJson}
  connectFCM("orderUpdate",order,getFCMTokenListOrder(order,"user"),"no")
  if (order["status"] == "0"):
    connectFCMHelper("Order",order,getFCMTokenListOrder(order,"helpers:dircetlySee_yes"),"no")
  elif (order["status"] == "1"):
    connectFCMHelper("Order",order,getFCMTokenListOrder(order,"helpers"),"no")
  elif (order["status"] == "2"):
    connectFCMHelper("orderRemove",order,getFCMTokenListOrder(order,"helpers"),"yes")
 else:
  p[0].delete()
  c1={"status":"error","message":"Order does not exist"}
 return HttpResponse(json.dumps(c1),content_type="application/json")

@api_view(['POST','GET'])
@csrf_exempt
def updateOrderHelperAPI(request):
 order = json.loads(request.body)
 if(order["status"]=="1" and float(order["refundValue"].split(":")[1]) > 0 and order["refundValue"].split(":")[0] == "P"):
    requestID = random.randint(1000000000,9999999999)
    consumerID = json.loads(serializers.serialize("json",User.objects.filter(number = order["userNumber"])))[0]["fields"]["consumerID"]
    refundJson = {"amount":float(order["refundValue"].split(":")[1]),"consumer_id":consumerID,"request_id": str(requestID)}
    c2 = json.loads(getWalletResponse('https://shmart.in/wallet/v1/credits/general',"post",refundJson))
    if(c2["status"] == "success"):
      order["refundValue"] = "S:" + order["refundValue"].split(":")[1]

 p=Userorder.objects.update_or_create(defaults = order, orderID = order["orderID"])
 OrderJson = json.loads(serializers.serialize("json",[p[0],]))[0]["fields"]
 if(p[1]==False):
  c1={"status":"success","message":"Order updated successfully","order":OrderJson}
  connectFCM("orderUpdate",order,getFCMTokenListOrder(order,"user"),"no")
  if (order["status"] == "2"):
    connectFCMMerchant("orderRemove",order,getFCMTokenListOrder(order,"merchant"),"yes")
  else:
    connectFCMMerchant("orderUpdate",order,getFCMTokenListOrder(order,"merchant"),"no")
 else:
  p[0].delete()
  c1={"status":"error","message":"Order does not exist"}
 return HttpResponse(json.dumps(c1),content_type="application/json")

@api_view(['POST','GET'])
@csrf_exempt
def updateBulkOrdersMerchantAPI(request):
 updateOrderArray = json.loads(request.body)["updateOrderArray"]
 updatedOrders = []
 successes = 0
 failures = 0
 for order in updateOrderArray:
   p=Userorder.objects.update_or_create(defaults = order, orderID = order["orderID"])
   OrderJson = json.loads(serializers.serialize("json",[p[0],]))[0]["fields"]
   if(p[1]==False):
    updatedOrders.append(OrderJson)
    successes = successes + 1
    connectFCM("orderUpdate",order,getFCMTokenListOrder(order,"user"),"no")
   else:
    failures = failures + 1
    p[0].delete()
 if (len(updateOrderArray)==failures):
    c1={"status":"error","message":"Orders do not exist"}
 else:
    c1={"status":"success","message":"Orders updated successfully","updatedOrders":updatedOrders,"successes":successes,"failures":failures}
 return HttpResponse(json.dumps(c1),content_type="application/json")

@api_view(['POST','GET'])
@csrf_exempt
def updateOrderUserAPI(request):
 order = json.loads(request.body)
 p=Userorder.objects.update_or_create(defaults = order, orderID = order["orderID"])
 OrderJson = json.loads(serializers.serialize("json",[p[0],]))[0]["fields"]
 if(p[1]==False):
  c1={"status":"success","message":"Order updated successfully","order":OrderJson}
  connectFCMMerchant("orderRemove",order,getFCMTokenListOrder(order,"merchant"),"yes")
  connectFCMHelper("orderRemove",order,getFCMTokenListOrder(order,"helpers"),"yes")
 else:
  p[0].delete()
  c1={"status":"error","message":"Order does not exist"}
 return HttpResponse(json.dumps(c1),content_type="application/json")

@api_view(['POST','GET'])
@csrf_exempt
def updateMerchantAdmin(request):
 data = json.loads(request.body)
 if (data["password"] == "Lets89308805786"):
   p=Merchant.objects.update_or_create(defaults= data ,number = data["number"])
   MerchantJson = json.loads(serializers.serialize("json",[p[0],]))[0]["fields"]
   if(p[1]==False):
    c1={"status":"success","message":"Merchant updated successfully","merchant":MerchantJson}
   else:
    p[0].delete()
    c1={"status":"error","message":"Merchant does not exist"}
 else:
   c1={"status":"error","message":"Incorrect password"}
 return HttpResponse(json.dumps(c1),content_type="application/json")

@api_view(['POST','GET'])
@csrf_exempt
def getMerchantAPI(request):
 data = json.loads(request.body)
 try:
    p = Merchant.objects.get(number = data["number"])
    MerchantJson = json.loads(serializers.serialize("json",[p,]))[0]["fields"]
    accountsList = json.loads(serializers.serialize("json",MerchantAccounts.objects.filter(merchantNumber = data["number"])))
    accounts = []
    for account in accountsList:
      accounts.append(account["fields"])
    settlementsList = json.loads(serializers.serialize("json",Settlement.objects.filter(merchantNumber =data["number"]).order_by("-dateTime")))
    settlements = []
    for settlement in settlementsList:
      settlements.append(settlement["fields"])
    if (len(settlements) > 0):
      pendingAmount = float(settlements[0]["carriedOver"])
    else:
      pendingAmount = 0.00
    unsettledOrdersList = json.loads(serializers.serialize("json",Userorder.objects.filter(merchantNumber = data["number"], isSettled = "no",status = "2")))
    unsettledOrders = []
    for unsettledOrder in unsettledOrdersList:
      unsettledOrders.append(unsettledOrder["fields"])
      pendingAmount = pendingAmount + float(unsettledOrder["fields"]["netPrice"])
    settlement = {"unsettledOrders":unsettledOrders,"pendingAmount":str(pendingAmount),"settlements":settlements}
    c1={"status":"success","message":"Merchant found successfully","merchant":MerchantJson,"accounts":accounts, "settlement":settlement}
 except:
    c1={"status":"error","message":"Merchant does not exist"}
 return HttpResponse(json.dumps(c1),content_type="application/json")

#@api_view(['POST','GET'])
@csrf_exempt
def sendOTPMessageAPI(request):
 data = json.loads(request.body)
 print data
 mobile_number=data["mobileNumber"]
 otpRow={"mobileNumber":mobile_number,"otp":random.randint(100000,999999)}
 d2 = Otp.objects.get_or_create(defaults=otpRow, mobileNumber = mobile_number)
 otp = json.loads(serializers.serialize("json",[d2[0],]))[0]["fields"]["otp"]
 if(sendOTPMessage(str(otp),mobile_number) == "OK"):
  c1={"status":"success","message":"otp message sent successfully"}
 else:
  c1={"status":"error","message":"message not sent"}
 return HttpResponse(json.dumps(c1),content_type="application/json")

#@api_view(['POST','GET'])
@csrf_exempt
def verifyOTPMessageAPI(request):
 data = json.loads(request.body)
 mobile_number=data["userNumber"]
 userType=data["userType"]
 fcmToken = data["fcmToken"]
 otpObject = Otp.objects.get(mobileNumber = mobile_number)
 if(data["otpInput"]==otpObject.otp):
  if(userType=="normalUser"):
    userData = {"consumerID" : "no_id","level":"0","referralCount" : "1","referralCode":''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6)),"fcmToken":fcmToken,"userType":userType,"number":mobile_number,"name":"Your Name"}
    p = User.objects.get_or_create(defaults = userData, number = mobile_number)
    if(p[1] == True):
     isUserNew="yes"
    else:
     isUserNew = "no"
     p[0].level = str(int(p[0].level) + 1)
     p[0].fcmToken = fcmToken
  
    if (isUserNew == "no" and p[0].consumerID != "no_id"):
      result = json.loads(getWalletResponse('https://shmart.in/wallet/v1/customers/activation_status/consumer_id/'+ p[0].consumerID,"get","noJson"))
      if (result['status'] != "success"):
       p[0].consumerID = "no_id"
  
    p[0].save()
    finalUserJSON = json.loads(serializers.serialize("json",[p[0],]))[0]["fields"]
    expenses = Expensedetails.objects.filter(persons__contains = mobile_number)
    expenseData = json.loads(serializers.serialize("json",expenses))
    fetchedItems = []
    for expense in expenseData:
      fetchedItems.append(expense["fields"])
  
    groupIDsSet = set()
    for group in expenseData:
      groupID = group["fields"]["object"].split("##")[0]
      groupIDsSet.add(groupID) 
    groupIDsSet.add("|other|")
    groupIDsSet.remove("|other|")
    print groupIDsSet
    finalExpenses = []
    if (len(groupIDsSet) > 0 ):
     idQuery = reduce(operator.or_,(Q(object__contains = groupID)for groupID in groupIDsSet ))
     groups =  Expensedetails.objects.filter(idQuery, id1 = "Group Creation", expenseVersion = "latest").exclude(groupDeletedBy__contains = mobile_number)
     groupsData = json.loads(serializers.serialize("json",groups))
     print groupsData
     for group in groupsData:
       groupID = group["fields"]["object"].split("##")[0]
       print groupID
       if (mobile_number in group["fields"]["persons"]):
         finalExpenses.append(group["fields"])

       for expense in fetchedItems:
         if (groupID in expense["object"] and "Group Creation" not in expense["id1"]):
           finalExpenses.append(expense)
    
    for expense in fetchedItems:
       if ("|other|" in expense["object"]):
         finalExpenses.append(expense)

    c1={"status":"success","user":finalUserJSON,"isUserNew":isUserNew,"expenses":finalExpenses,"message":"verification successful","dynamicValue":getdynamicValue(),"notifications":getNotifications()}
  elif (userType == "merchant"):
    merchantData = {"consumerID" : "no_id","level":"0","referralCount" : "1","referralCode":''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6)),"fcmToken":fcmToken,"userType":userType,"number":mobile_number,"isVerified":"no","status":"0","paymentType":"no:no:no"}
    merchant = Merchant.objects.get_or_create(defaults = merchantData, number=mobile_number)
    merchantJson= json.loads(serializers.serialize("json",[merchant[0],]))[0]["fields"]
    helpersList = []
    ordersList = []
    if(merchant[1] == True):
      isUserNew = "yes"
    else:
      isUserNew = "no"
      merchant[0].level = str(int(merchant[0].level) + 1)
      merchant[0].fcmToken = fcmToken
      merchant[0].save()
      orders = json.loads(serializers.serialize("json",Userorder.objects.filter(merchantNumber = mobile_number)))
      for order in orders:
        ordersList.append(order["fields"])
      helpers = json.loads(serializers.serialize("json",Helper.objects.filter(merchantNumber = mobile_number)))
      for helper in helpers:
        helpersList.append(helper["fields"])
    c1={"status":"success","merchant":merchantJson,"isUserNew":isUserNew,"message":"verification successful","dynamicValue":getdynamicValue(),"helpers":helpersList,"orders":ordersList}
  elif (userType == "helper"):
    merchant_number=data["merchantNumber"]
    helperData = {"fcmToken":fcmToken}
    helper = Helper.objects.update_or_create(defaults = helperData, number=mobile_number,merchantNumber=merchant_number)
    if(helper[1] == True):
      helper[0].delete()
      c1={"status":"error","message":"helper not listed by this merchant"}
    else:
      helperJson= json.loads(serializers.serialize("json",[helper[0],]))[0]["fields"]
      c1={"status":"success","helper":helperJson,"message":"verification successful","dynamicValue":getdynamicValue()}
  otpObject.delete()
 else:
  c1={"status":"error","message":"incorrect otp"}
 return HttpResponse(json.dumps(c1),content_type="application/json")

@api_view(['POST','GET'])
@csrf_exempt
def refreshAPI(request):
 data = json.loads(request.body)
 mobile_number = data["userNumber"]
 syncList = data["syncList"]
 syncExpenses(syncList)
 groupIDs =  Expensedetails.objects.filter(persons__contains = mobile_number, id1 = "Group Creation", expenseVersion = "latest").values_list('object',flat=True)
 groupIDsList = []
 for groupID in groupIDs:
  groupIDsList.append(groupID.split("##")[0])
 groupIDsList.append("|other|")
 
 finalExpenses = []
 idQuery = reduce(operator.or_,(Q(object__contains = groupID)for groupID in groupIDsList))
 syncedString = mobile_number + "_0"
 expenses =  Expensedetails.objects.filter(idQuery, persons__contains = mobile_number, syncedString__contains = syncedString)
 newSyncedString = mobile_number + "_1"
 for expense in expenses:
   expense.syncedString = (expense.syncedString).replace(syncedString, newSyncedString)
   expense.save()
   finalExpenses.append(json.loads(serializers.serialize("json",[expense,]))[0]["fields"])
 #syncedList = []
 #for sync in syncList:
  # Expensedetails.objects.update_or_create(defaults = sync,id1 = sync["id1"], object__contains = sync["object"].split("##")[0],expenseVersion = sync["expenseVersion"])
  # for finalExp in finalExpenses:
   # sync["syncedString"] = (sync["syncedString"]).replace(syncedString, newSyncedString)
   # if(sync["id1"] == finalExp["id1"] and sync["expenseVersion"] == finalExp["expenseVersion"] and sync["object"].split("##")[0] == finalExp["object"].split("##")[0]): 
    # isSame = True
    #else:
    # isSame = False   
   #if (isSame == True):
    #if(sync["id1"] == "Group Creation"):
     #connectFCM("groupUpdate",sync, getFCMTokenList(sync))
    #else:
     #connectFCM("expenseUpdate",sync, getFCMTokenList(sync))
   #else:  
 #syncedList.append(sync)
 #p = User.objects.get(number = mobile_number)
 #finalUserJSON = json.loads(serializers.serialize("json",[p[0],]))[0]["fields"]
 c1={"status":"success","message":"Refresh successfull","updates":finalExpenses,"count":str(len(finalExpenses)),"syncedList":syncList,"dynamicValue":getdynamicValue(),"notifications":getNotifications()}
 #Expensedetails.objects.filter(idQuery, persons__contains = mobile_number, syncedString__contains = syncedString).update(syncedString = F('syncedString').replace(syncedString,newSyncedString))
 return HttpResponse(json.dumps(c1),content_type="application/json")

#AdminApi's
@api_view(['POST','GET'])
@csrf_exempt
def getFilteredMerchantsAdminAPI(request):
   data = json.loads(request.body)
   if(data["password"]=="123456"):
     merchantData = Merchant.objects.filter(status__contains= data["visibility"],isBlocked__contains = data["blocked"],isVerified__contains = data["verified"],location__contains = data["location"] ,name__contains = data["name"],number__contains =data["number"] )
     merchantData = json.loads(serializers.serialize("json",merchantData))
     merchantsList = []
     for merchant in merchantData:
       merchantsList.append(merchant["fields"])
     response = {"status":"success","message":"Merchants fetched successfully","merchants":merchantsList,"count":len(merchantsList)}
   else:
     response = {"status":"error","message":"Incorrect password"}
   return HttpResponse(json.dumps(response),content_type="application/json")


@api_view(['POST','GET'])
@csrf_exempt
def notifyUserAfterRefundAdminAPI(request):
    data = json.loads(request.body)
    notification=data["notification"]
    isSilent = data["isSilent"]
    category = data["category"]
    if(data["password"] =="123456"):
      userFCM = User.objects.filter(number = data["number"]).get().fcmToken
      print userFCM
      subList = []
      subList.append(userFCM)
      fcmResponse  = connectFCM("refund",notification,subList,isSilent)
      response = {"status": "success","message":"user fetch","userData":userFCM}
      return HttpResponse(json.dumps(response),content_type="application/json")
@api_view(['POST','GET'])
@csrf_exempt
def getUserRefundAdminAPI(request):
  data = json.loads(request.body)
  if(data["password"]=="123456"):

   userRefundList = json.loads(serializers.serialize("json",Userorder.objects.filter(refundValue__contains = "P:") ))
   userList = []
   for userLists in userRefundList:
     userList.append(userLists["fields"])
   response = {"status":"success","message":"RefundList fetched successfully","UserRefundList":userList,"count":len(userList)}
  else:
   response =  {"status":"error","message":"password incorrect"}
  return HttpResponse(json.dumps(response),content_type="application/json")

 

@api_view(['POST','GET'])
@csrf_exempt
def addUserAdminAPI(request):
   data = json.loads(request.body)
   if(data["password"]=="123456"):
    user=User.objects.get_or_create(defaults=data, number = data["number"])
    user= json.loads(serializers.serialize("json",user))



@api_view(['POST','GET'])
@csrf_exempt
def getMerchantSettlementAdminAPI(request):
   data = json.loads(request.body)
   if(data["password"]=="123456"):
     settlementData = Settlement.objects.filter(status = "")
     settlementData = json.loads(serializers.serialize("json",merchantData))
     settlementsList = []
     for merchant in settlementData:
       settlementsList.append(merchant["fields"])
     response = {"status":"success","message":"Settlement fetched successfully","settlements":merchantsList}
   else:
     response = {"status":"error","message":"Incorrect password"}
   return HttpResponse(json.dumps(response),content_type="application/json")

@api_view(['POST','GET'])
@csrf_exempt
def getuserListAdminAPI(request):
 data = json.loads(request.body)
 userList =  User.objects.filter(date__range=["2016-11-07", "2016-11-07"])
 userList = json.loads(serializers.serialize("json",userList))
 print userList
@api_view(['POST','GET'])
@csrf_exempt
def updateMerchantAdminAPI(request):
 data = json.loads(request.body)
 if (data["password"] == "Lets89308805786"):
   p=Merchant.objects.update_or_create(defaults= data ,number = data["number"])
   MerchantJson = json.loads(serializers.serialize("json",[p[0],]))[0]["fields"]
   if(p[1]==False):
    c1={"status":"success","message":"Merchant updated successfully","merchant":MerchantJson}
   else:
    p[0].delete()
    c1={"status":"error","message":"Merchant does not exist"}
 else:
   c1={"status":"error","message":"Incorrect password"}
 return HttpResponse(json.dumps(c1),content_type="application/json")

@api_view(['POST','GET'])
@csrf_exempt
def getSingleMerchantAdminAPI(request):
 data = json.loads(request.body)
 if(data["password"] == "123456"):
  merchantNumber = data["merchantNumber"]
  merchantData = json.loads(serializers.serialize("json",Merchant.objects.filter(number = merchantNumber)))
  if(len(merchantData) == 1):
    helperList = json.loads(serializers.serialize("json",Helper.objects.filter(merchantNumber = merchantNumber)))
    helpers = []
    for helper in helperList:
      helpers.append(helper["fields"])
    merchantJson = merchantData[0]["fields"]
    accountsList = json.loads(serializers.serialize("json",MerchantAccounts.objects.filter(merchantNumber = merchantNumber)))
    accounts = []
    for account in accountsList:
      accounts.append(account["fields"])
    settlementsList = json.loads(serializers.serialize("json",Settlement.objects.filter(merchantNumber = merchantNumber).order_by("-dateTime")))
    settlements = []
    for settlement in settlementsList:
      settlements.append(settlement["fields"])
    if (len(settlements) > 0):
      pendingAmount = float(settlements[0]["carriedOver"])
    else:
      pendingAmount = 0.00

    unsettledOrdersList = json.loads(serializers.serialize("json",Userorder.objects.filter(merchantNumber = merchantNumber, isSettled = "no",status = "2")))
    unsettledOrders = []
    for unsettledOrder in unsettledOrdersList:
      unsettledOrders.append(unsettledOrder["fields"])
      pendingAmount = pendingAmount + float(unsettledOrder["fields"]["netPrice"])
    settlement = {"unsettledOrders":unsettledOrders,"pendingAmount":str(pendingAmount),"settlements":settlements}
    c1={"status":"success","message":"Merchant found successfully","settlement":settlement,"helpers":helpers,"accounts":accounts,"merchant":merchantJson}
  else:
    c1={"status":"error","message":"Merchant does not exist"}
 else:
  c1={"status":"error","message":"Incorrect password"}
 return HttpResponse(json.dumps(c1),content_type="application/json")

@api_view(['POST','GET'])
@csrf_exempt
def sendPushNotificationAdminAPI(request):
 data = json.loads(request.body)
 notification=data["notification"]
 isSilent = data["isSilent"]
 category = data["category"]
 if (data["password"] == "Lets8930880578"):
  if(category == "user"):
   fcmTokenList =[x.encode("utf-8")for x in User.objects.exclude(fcmToken = "").values_list('fcmToken',flat=True)]
   subLists = [fcmTokenList[i:i+1000] for i in range(0,len(fcmTokenList),1000)]
   counter = 0
   for subList in subLists:
    counter = counter + int(connectFCM("pushNotification",notification,subList,isSilent)["success"])
   print "gshsjskskkshskaskjsksjsksnksksksj"
   c1={"status":"success","message":"Notifications sent successfully","TotalUsers":User.objects.exclude(fcmToken = "").count(),"NotificationsSent":counter}
   PushNotification.objects.update_or_create(defaults = notification,notificationID = notification["notificationID"])
 
  elif(category == "merchant"):
   print "merchant merchant "
   fcmTokenList =[x.encode("utf-8")for x in Merchant.objects.exclude(fcmToken = "").values_list('fcmToken',flat=True)]
   subLists = [fcmTokenList[i:i+1000] for i in range(0,len(fcmTokenList),1000)]
   counter = 0
   for subList in subLists:
    counter = counter + int(connectFCM("pushNotification",notification,subList,isSilent)["success"])
   print "gshsjskskkshskaskjsksjsksnksksksjmerchantmerchant"
   c1={"status":"success","message":"Notifications sent successfully","TotalUsers":Merchant.objects.exclude(fcmToken = "").count(),"NotificationsSent":counter}
   PushNotification.objects.update_or_create(defaults = notification,notificationID = notification["notificationID"])
  elif(category == "helper"):
   fcmTokenList =[x.encode("utf-8")for x in Helper.objects.exclude(fcmToken = "").values_list('fcmToken',flat=True)]
   subLists = [fcmTokenList[i:i+1000] for i in range(0,len(fcmTokenList),1000)]
   counter = 0
   for subList in subLists:
    counter = counter + int(connectFCM("pushNotification",notification,subList,isSilent)["success"])
   c1={"status":"success","message":"Notifications sent successfully","TotalUsers":Helper.objects.exclude(fcmToken = "").count(),"NotificationsSent":counter}
   PushNotification.objects.update_or_create(defaults = notification,notificationID = notification["notificationID"])
  elif(category == "all"):
   #forUser
   fcmTokenList =[x.encode("utf-8")for x in User.objects.exclude(fcmToken = "").values_list('fcmToken',flat=True)]
   subLists = [fcmTokenList[i:i+1000] for i in range(0,len(fcmTokenList),1000)]
   counter = 0
   for subList in subLists:
    counter = counter + int(connectFCM("pushNotification",notification,subList,isSilent)["success"])
   c1={"status":"success","message":"Notifications sent successfully","TotalUsers":User.objects.exclude(fcmToken = "").count(),"NotificationsSent":counter}
   PushNotification.objects.update_or_create(defaults = notification,notificationID = notification["notificationID"])
   #forMerchant
   fcmTokenList1 =[x.encode("utf-8")for x in Merchant.objects.exclude(fcmToken = "").values_list('fcmToken',flat=True)]
   subLists1 = [fcmTokenList1[i:i+1000] for i in range(0,len(fcmTokenList1),1000)]
   counter = 0
   for subList in subLists1:
    counter = counter + int(connectFCM("pushNotification",notification,subList,isSilent)["success"])
   c1={"status":"success","message":"Notifications sent successfully","TotalUsers":Merchant.objects.exclude(fcmToken = "").count(),"NotificationsSent":counter}
   PushNotification.objects.update_or_create(defaults = notification,notificationID = notification["notificationID"])
   #forHelper
   fcmTokenList2 =[x.encode("utf-8")for x in Helper.objects.exclude(fcmToken = "").values_list('fcmToken',flat=True)]
   subLists2 = [fcmTokenList2[i:i+1000] for i in range(0,len(fcmTokenList2),1000)]
   counter = 0
   for subList in subLists2:
    counter = counter + int(connectFCM("pushNotification",notification,subList,isSilent)["success"])
   c1={"status":"success","message":"Notifications sent successfully","TotalUsers":Helper.objects.exclude(fcmToken = "").count(),"NotificationsSent":counter}
   PushNotification.objects.update_or_create(defaults = notification,notificationID = notification["notificationID"])

 else:
  c1={"status":"error","message":"Incorrect password"}
 return HttpResponse(json.dumps(c1),content_type="application/json")

@api_view(['POST','GET'])
@csrf_exempt
def addUpdateHelperAdminAPI(request):
 data = json.loads(request.body)
 if (data["password"] == "Lets89308805786"):
   p=Helper.objects.update_or_create(defaults = data["helper"] ,number = data["helper"]["number"], merchantNumber = data["helper"]["merchantNumber"])
   HelperJson = json.loads(serializers.serialize("json",[p[0],]))[0]["fields"]
   if(p[1]==False):
    c1={"status":"success","message":"Helper updated successfully","helper":HelperJson}
   else:
    p[0].fcmToken = " "
    p[0].save()
    c1={"status":"success","message":"Helper added successfully","helper":HelperJson}
 else:
  c1={"status":"error","message":"Incorrect password"}
 return HttpResponse(json.dumps(c1),content_type="application/json")

@api_view(['POST','GET'])
@csrf_exempt
def deleteHelperAdminAPI(request):
 data = json.loads(request.body)
 if (data["password"] == "Lets89308805786"):
   p=Helper.objects.filter(number = data["helper"]["number"], merchantNumber = data["helper"]["merchantNumber"])
   if(p.count() == 0):
    c1={"status":"error","message":"Helper does not exist for this merchant"}
   else:
    p.delete()
    c1={"status":"success","message":"Helper deleted successfully"}
 else:
  c1={"status":"error","message":"Incorrect password"}
 return HttpResponse(json.dumps(c1),content_type="application/json")

@api_view(['POST','GET'])
@csrf_exempt
def addUpdateAccountAdminAPI(request):
 data = json.loads(request.body)
 if (data["password"] == "Lets89308805786"):
   p=MerchantAccounts.objects.update_or_create(defaults = data["account"],accountID = data["account"]["accountID"])
   AccountJson = json.loads(serializers.serialize("json",[p[0],]))[0]["fields"]
   if(p[1]==False):
     message = "Account updated successfully"
   else:
     message = "Account added successfully"
   if (AccountJson["defaultCreditAccount"] == "yes"):
     MerchantAccounts.objects.filter(merchantNumber = AccountJson["merchantNumber"]).exclude(accountID = AccountJson["accountID"]).update(defaultCreditAccount = "no")
   c1={"status":"success","message":message,"account":AccountJson}
 else:
  c1={"status":"error","message":"Incorrect password"}
 return HttpResponse(json.dumps(c1),content_type="application/json")

@api_view(['POST','GET'])
@csrf_exempt
def deleteAccountAdminAPI(request):
 data = json.loads(request.body)
 if (data["password"] == "Lets89308805786"):
  p=MerchantAccounts.objects.filter(accountID = data["account"]["accountID"])
  if(p.count() == 0):
    c1={"status":"error","message":"Account does not exist"}
  else:
    p.delete()
    c1={"status":"success","message":"Account deleted successfully"}
 else:
  c1={"status":"error","message":"Incorrect password"}
 return HttpResponse(json.dumps(c1),content_type="application/json")

@api_view(['POST','GET'])
@csrf_exempt
def addSettlementAdminAPI(request):
 data = json.loads(request.body)
 if (data["password"] == "Lets89308805786"):
   Userorder.objects.filter(orderID__in = data["orderIDsList"]).update(isSettled = "yes:" + data["settlement"]["settlementID"])
   p=Settlement.objects.update_or_create(defaults = data["settlement"], settlementID = data["settlement"]["settlementID"])
   SettlementJson = json.loads(serializers.serialize("json",[p[0],]))[0]["fields"]
   c1={"status":"success","message":"Settlement added successfully","settlement":SettlementJson}
 else:
  c1={"status":"error","message":"Incorrect password"}
 return HttpResponse(json.dumps(c1),content_type="application/json")

@api_view(['POST','GET'])
@csrf_exempt
def getSingleSettlementAdminAPI(request):
 data = json.loads(request.body)
 if (data["password"] == "Lets89308805786"):
   p=Settlement.objects.filter(settlementID = data["settlementID"])
   if(p.count() == 1):
     SettlementJson = json.loads(serializers.serialize("json",p))[0]["fields"]
     ordersData =  json.loads(serializers.serialize("json",Userorder.objects.filter(isSettled = "yes:"+ data["settlementID"])))
     orders = []
     for order in ordersData:
       orders.append(order["fields"])
     c1={"status":"success","message":"Settlement found successfully","settlement":SettlementJson,"orders":orders}
   else:
     p.delete()
     c1={"status":"success","message":"Settlement does not exist"}
 else:
  c1={"status":"error","message":"Incorrect password"}
 return HttpResponse(json.dumps(c1),content_type="application/json")

@api_view(['POST','GET'])
@csrf_exempt
def getSingleSettlementMerchantAPI(request):
 data = json.loads(request.body)
 p=Settlement.objects.filter(settlementID = data["settlementID"])
 if(p.count() == 1):
   SettlementJson = json.loads(serializers.serialize("json",p))[0]["fields"]
   ordersData =  json.loads(serializers.serialize("json",Userorder.objects.filter(isSettled = "yes:"+ data["settlementID"])))
   orders = []
   for order in ordersData:
     orders.append(order["fields"])
   c1={"status":"success","message":"Settlement found successfully","settlement":SettlementJson,"orders":orders}
 else:
   p.delete()
   c1={"status":"success","message":"Settlement does not exist"}
 return HttpResponse(json.dumps(c1),content_type="application/json")
@api_view(['POST','GET'])
@csrf_exempt
def walletAPI(request):          #(Wallet API) 
 print "inside api call"
 print request.method
 data = json.loads(request.body)
 requiredFunction= data['requiredFunction']
 domainType= data['domainType']
 userNumber= data['userNumber']
 incomingjson=data['incomingJson']
 
 user = User.objects.filter(number = userNumber)
 user_data = json.loads(serializers.serialize("json",user))
 consumerID = user_data[0]["fields"]["consumerID"]
 
 if(domainType=="sandBox"):
  domain="http://180.179.146.81"
 else:
  domain="https://shmart.in"
 
 if(requiredFunction=="getBalance"):
  return HttpResponse(getWalletResponse(domain +'/wallet/v1/balances/general/consumer_id/'+consumerID,"get",incomingjson ))
  
 elif(requiredFunction=="checkUserActivated"):
  return HttpResponse(getWalletResponse(domain +'/wallet/v1/customers/activation_status/consumer_id/'+consumerID,"get",incomingjson ))

 elif(requiredFunction=="getTransactionHistory"):
  return HttpResponse(getWalletResponse(domain +'/wallet/v1/transactions/list/consumer_id/'+consumerID,"get",incomingjson ))
  
 elif(requiredFunction=="getBeneficiaryList"):
  return HttpResponse(getWalletResponse(domain +'/wallet/v1/customers/list_beneficiary/consumer_id/'+consumerID,"get",incomingjson ))
 
 elif(requiredFunction=="getBalanceLimits"):
  return HttpResponse(getWalletResponse(domain +'/wallet/v1/balances/availableLimit',"post",incomingjson ))

 elif(requiredFunction=="createWalletAccount"):
  return HttpResponse(getWalletResponse(domain +'/wallet/v1/customers/create',"post",incomingjson ))

 elif(requiredFunction=="generateOTP"):
  return HttpResponse(getWalletResponse(domain +'//wallet/v1/customers/generateotp',"post",incomingjson ))

 elif(requiredFunction=="activateWalletAccount"):
  return HttpResponse(getWalletResponse(domain +'//wallet/v1/customers/activate',"post",incomingjson ))

 elif (requiredFunction=="getBalanceAndBalanceLimits"):
  balanceJSON = json.loads(getWalletResponse(domain +'/wallet/v1/balances/general/consumer_id/'+consumerID,"get",incomingjson ))
  limitJSON = json.loads(getWalletResponse(domain +'/wallet/v1/balances/availableLimit',"post",incomingjson ))
  if(balanceJSON["status"] == "success" and limitJSON["status"] == "success"):
    status = "success"
  else:
    status = "error"
  finalResponse = {"balanceJSON" : balanceJSON, "limitJSON" : limitJSON, "status" : status}
  return HttpResponse(json.dumps(finalResponse),content_type="application/json")

 elif(requiredFunction=="doBankTransfer"):
  c1=json.loads(getWalletResponse(domain +'/wallet/v1/transfers/withdraw',"post",incomingjson))
  if(c1["status"] == 'success'):
    status = "success"
    merchantPay = json.loads(getWalletResponse(domain +'/wallet/v1/debits/general',"post",data["merchantJson"]["incomingJson"]))
  else:
    merchantPay = {"status":"bank transfer error"}
    status = "error"
  PBankTransferData= {"consumerID":consumerID,"transactionStatus":status,"userNumber":data["userNumber"],"amount":incomingjson["amount"],"version":data["version"],"userName":data["userName"]}
  PBankTransfer.objects.get_or_create(defaults =PBankTransferData,transactionStatus="ABC,,,,,,")
  finalResponse = {"bankJSON" : c1, "merchantJSON" : merchantPay, "status" : status}
  return HttpResponse(json.dumps(finalResponse),content_type="application/json")
  
 elif(requiredFunction=="doWalletToWalletTransfer"):
  receivers = data["receiversInfo"]
  responseList = []
  successes = 0
  failures = 0
  total = 0.00
  for receiver in receivers:
    walletJson = {"consumer_id":consumerID,"friend_mobileNo":receiver["number"],"friend_email":receiver["email"],"amount":receiver["amount"],"message":receiver["message"],"friend_name":receiver["name"]}
    c1 = json.loads(getWalletResponse(domain +'/wallet/v1/wallet_transfers/',"post",walletJson))
    if(c1["status"] == 'success'):
      expense = receiver["expenseObject"]
      addExpenseObject(expense)
      fcmJSON = {"userNumber":data["userNumber"],"userName":data["userName"],"expense":expense}
      connectFCM("expenseAdd",fcmJSON,getFCMTokenList(expense),"no")
      status="success"
      successes = successes + 1
      total = total + float(receiver["amount"])
    else:
      failures = failures + 1
      status="failed"
    response = {"number":receiver["number"],"amount":receiver["amount"],"status":c1["status"], "expenseObject":receiver["expenseObject"]}
    responseList.append(response)
    PW2WData= {"confreeStatus":data["confreeStatus"],"transactionStatus":status,"userNumber":data["userNumber"],"amount":receiver["amount"],"senderName":data["userName"],"recipientNumber":receiver["number"],"recipientName":receiver["name"],"senderConsumerID":consumerID,"date":data["date"],"model":data["model"],"version":data["version"]}
    PW2W.objects.get_or_create(defaults = PW2WData,transactionStatus="ABC")
  
  if(data["confreeStatus"] == "true"):
    dv = getdynamicValue()
    max = float(dv["maxValue"])
    confreeValueDefault = float(dv["defaultConfreeValue"])
    if (total > max):
      amount = max * confreeValueDefault/100
    else:
      amount = total * confreeValueDefault/100
    requestID = random.randint(1000000000,9999999999)
    confreeJson = {"amount":amount,"consumer_id":consumerID,"request_id": str(requestID)}
    c2 = json.loads(getWalletResponse(domain +'/wallet/v1/credits/general',"post",confreeJson))
    if (c2["status"] == 'success'):
      u = User.objects.get(number = data["userNumber"])
      u.referralCount = str(int(u.referralCount) - 1)
      u.save()
      finalUserJSON = json.loads(serializers.serialize("json",[u,]))[0]["fields"]
      confreeResponse = "success"
    else:
      finalUserJSON = "user not updated"
      confreeResponse = "error"
  else:
    finalUserJSON = "user not updated"
    confreeResponse = "No Confree card used"
  finalResponse = {"responseList":responseList,"successes":str(successes),"failures": str(failures),"confreeStatus":confreeResponse,"finalUserJSON":finalUserJSON} 
  return HttpResponse(json.dumps(finalResponse),content_type="application/json")
 
 elif(requiredFunction=="doWalletToWalletTransferFriend"):
  receiver = data["receiverInfo"]
  walletJson = {"consumer_id":consumerID,"friend_mobileNo":receiver["number"],"friend_email":receiver["email"],"amount":receiver["amount"],"message":receiver["message"],"friend_name": receiver["name"]}
  c1 = json.loads(getWalletResponse(domain +'/wallet/v1/wallet_transfers/',"post",walletJson))
  if(c1["status"] == 'success'):
    expenseObjects = data["expenseObjects"]
    for expense in expenseObjects:
      addExpenseObject(expense)
      fcmJSON = {"userNumber":data["userNumber"],"userName":data["userName"],"expense":expense}
      connectFCM("expenseAdd",fcmJSON,getFCMTokenList(expense),"no")
    status = "success"
  else:
    status="failed"
  PW2WData= {"confreeStatus":data["confreeStatus"],"transactionStatus":status,"userNumber":data["userNumber"],"amount":receiver["amount"],"senderName":data["userName"],"recipientNumber":receiver["number"],"recipientName":receiver["name"],"senderConsumerID":consumerID,"date":data["date"],"model":data["model"],"version":data["version"]}
  PW2W.objects.get_or_create(defaults = PW2WData,transactionStatus="ABC")

  if(data["confreeStatus"] == "true"):
    dv = getdynamicValue()
    max = float(dv["maxValue"])
    confreeValueDefault = float(dv["defaultConfreeValue"])
    total = float(receiver["amount"])
    if (total > max):
      amount = max * confreeValueDefault/100
    else:
      amount = total * confreeValueDefault/100
    requestID = random.randint(1000000000,9999999999)
    confreeJson = {"amount":amount,"consumer_id":consumerID,"request_id": str(requestID)}
    c2 = json.loads(getWalletResponse(domain +'/wallet/v1/credits/general',"post",confreeJson))
    if (c2["status"] == 'success'):
      u = User.objects.get(number = data["userNumber"])
      u.referralCount = str(int(u.referralCount) - 1)
      u.save()
      finalUserJSON = json.loads(serializers.serialize("json",[u,]))[0]["fields"]
      confreeResponse = "success"
    else:
      finalUserJSON = "user not updated"
      confreeResponse = "error"
  else:
    finalUserJSON = "user not updated"
    confreeResponse = "No Confree card used"
  finalResponse = {"status":c1["status"], "expenseObjects":expenseObjects,"confreeStatus":confreeResponse,"finalUserJSON":finalUserJSON}
  return HttpResponse(json.dumps(finalResponse),content_type="application/json")

 elif(requiredFunction=="doMerchantPayment"):
 # c1=json.loads(getWalletResponse(domain +'/wallet/v1/debits/general',"post",data["walletJSON"]["incomingJson"]))
 # if(c1["status"] == "success"):
 #     order=data["order"]
 #     placeOrder(order)
 #     status="success"
 # else:
 #     status="failed"
 # PMerchantPaymentData= {"consumerID":data["consumer_id"],"transactionStatus":status,"userNumber":data["userNumber"],"amount":data["amount"],"orderNo":data["orderNo"],"merchantName":data["merchantName"],"date":data["date"],"userName":data["userName"]}
 # PMerchantPayment.objects.get_or_create(defaults =PMerchantPaymentData,transactionStatus="ABC,,,,,,")
 # return HttpResponse(c1)
  response = placeOrder(data["order"])
  return HttpResponse(json.dumps(response),content_type="application/json")
  
 elif(requiredFunction=="creditUserWallet"):
  return HttpResponse(getWalletResponse(domain +'/wallet/v1/credits/general',"post",incomingjson ))

 elif(requiredFunction=="addBeneficiary"):
  return HttpResponse(getWalletResponse(domain +'/wallet/v1/transfers/create' ,"post",incomingjson ))
 
 elif(requiredFunction=="addFundThroughiFrame"):
  c1=json.loads(getWalletResponse(domain +'/wallet/v1/funds/create_iframe',"post",incomingjson))
  if(c1["status"] == 'success'):
    status="success"
  else:
    status="failed"
  print c1
  PAddCashData= {"consumerID":data["userConsumerID"],"transactionStatus":status,"userNumber":data["userNumber"],"amount":incomingjson["amount"],"version":data["version"],"userName":data["userName"]}
  PAddCash.objects.get_or_create(defaults =PAddCashData,transactionStatus="ABC")
  return HttpResponse(json.dumps(c1))
 
 elif(requiredFunction=="deleteBeneficiary"):
  return HttpResponse(getWalletResponse(domain +'/wallet/v1/transfers/deletebeneficiary',"post",incomingjson ))

def getWalletResponse(urlString, requestMethod, incomingJson):
  MERCHANT_USERNAME="0299af1022b234007dd3e93738d4939d"
  MERCHANT_PASSWORD="ef39f0a342da57b6b30f00ce427c01fc"
  headers = {'content-type':'application/json','Accept':'application/json'}
  if (requestMethod == "get"):
    res=requests.get(urlString, auth=(MERCHANT_USERNAME,MERCHANT_PASSWORD),headers=headers)
  else:
    res=requests.post(urlString,auth=(MERCHANT_USERNAME,MERCHANT_PASSWORD),headers=headers,data=json.dumps(incomingJson))
  return json.loads(json.dumps(res.text,indent=4))

def placeOrder (order):
  addOrderObject(order)
  connectFCMMerchant("orderAdd",order,getFCMTokenListOrder(order,"merchant"),"no")
  if (order["confreeStatus"] != 'no'):
      u = User.objects.get(number = order["userNumber"])
      u.referralCount = str(int(u.referralCount) - 1)
      u.save()
      finalUserJSON = json.loads(serializers.serialize("json",[u,]))[0]["fields"]
  else:
      finalUserJSON = "user not updated"
  finalResponse = {"status":"success","order":order,"updatedUserJSON":finalUserJSON}
  return finalResponse
  
@api_view(['POST','GET'])
@csrf_exempt
def expenseAddAPI(request):
 print request.user
 if request.user.is_authenticated():     
   data = json.loads(request.body)
   expense = data["expense"]
   if(addExpenseObject(expense) == 0):
    c1={"status":"error","message":"Error adding expense"}
   else:
    c1={"status":"success","data":"Expense added successfully"}
    connectFCM("expenseAdd",data,getFCMTokenList(expense),"no")
   return HttpResponse(json.dumps(c1),content_type="application/json")


@api_view(['POST','GET'])
@csrf_exempt
def addExpenseObjectsFriendAPI(request):
 data = json.loads(request.body)
 expenseObjects = data["expenseObjects"]
 for expense in expenseObjects:
  addExpenseObject(expense)
  fcmJSON = {"userNumber":data["userNumber"],"userName":data["userName"],"expense":expense}
  connectFCM("expenseAdd",fcmJSON,getFCMTokenList(expense),"no") 
 c1 = {"status":"success", "expenseObjects":expenseObjects}
 return HttpResponse(json.dumps(c1),content_type="application/json")

@api_view(['POST','GET'])
@csrf_exempt
def expenseUpdateAPI(request):
 data = json.loads(request.body)
 addExpenseObject(data["oldJSON"])
 if(updateExpenseObject(data["newJSON"]) == 0):
  response = {"status":"error","message":"Error updating expense"}
 else:
  connectFCM("expenseUpdate",data,list(set(getFCMTokenList(data["oldJSON"]))|set(getFCMTokenList(data["newJSON"]))),"no")
  response = {"status":"success","message":"Expense updated successfully"}
 return HttpResponse(json.dumps(response),content_type="application/json")

 
@api_view(['POST','GET'])
@csrf_exempt
def expenseDeleteAPI(request):
 data = json.loads(request.body)
 expense = data["expense"]
 if(updateExpenseObject(expense) != 1):
  response = {"status":"error","message":"Error deleting expense"}
 else:
  connectFCM("expenseDelete",data,getFCMTokenList(expense),"no")
  response = {"status":"success","data":"Expense deleted successfully"}
 return HttpResponse(json.dumps(response),content_type="application/json")

def updateExpenseObject (data):
 Expensedetails.objects.update_or_create(defaults = data,id1=data["id1"],expenseVersion = data["expenseVersion"],object__contains = data["object"].split("##")[0]) 
 return 1

def addExpenseObject (data):
 di = Expensedetails.objects.get_or_create(defaults = data,id1=data["id1"],expenseVersion = data["expenseVersion"],object__contains = data["object"].split("##")[0])
 return 1

def addOrderObject (data):
 di = Userorder.objects.get_or_create(defaults = data,orderID = 'randomorderid' )
 return 1

def getFCMTokenList(expense):
 numberList = expense["persons"][:-1].split(":")
 idQuery = reduce(operator.or_,(Q(number = number)for number in numberList))
 fcmTokenList =[x.encode("utf-8")for x in User.objects.filter(idQuery).values_list('fcmToken',flat=True)]
 return fcmTokenList

def getFCMTokenListOrder(order, ofWhom):
 if(ofWhom == "merchant"):
   fcmTokenList =[x.encode("utf-8")for x in Merchant.objects.filter(number = order["merchantNumber"]).values_list('fcmToken',flat=True)]
 elif (ofWhom == "user"):
   fcmTokenList =[x.encode("utf-8")for x in User.objects.filter(number = order["userNumber"]).values_list('fcmToken',flat=True)]
 elif (ofWhom == "helpers"):
   fcmTokenList =[x.encode("utf-8")for x in Helper.objects.filter(merchantNumber = order["merchantNumber"]).values_list('fcmToken',flat=True)]
 elif (ofWhom == "helpers:dircetlySee_yes"):
   fcmTokenList =[x.encode("utf-8")for x in Helper.objects.filter(merchantNumber = order["merchantNumber"],privilege__contains = 'directlySee_yes').values_list('fcmToken',flat=True)]
 print fcmTokenList
 return fcmTokenList

@api_view(['POST','GET'])
@csrf_exempt
def groupAddAPI(request):
 data = json.loads(request.body)
 group = data["group"]
 if(addExpenseObject(group) != 1):
  c1={"status":"error","message":"Error adding group"}
 else:
  connectFCM("groupAdd",data,getFCMTokenList(group),"no")
  c1={"status":"success","data":"Group added successfully"}
 return HttpResponse(json.dumps(c1),content_type="application/json")


@api_view(['POST','GET'])
@csrf_exempt
def groupUpdateAPI(request):
 data = json.loads(request.body)
 addExpenseObject(data["oldJSON"])
 if(updateExpenseObject(data["newJSON"]) != 1):
  response = {"status":"error","message":"Error updating expense"}
 else:
  connectFCM("groupUpdate",data,list(set(getFCMTokenList(data["oldJSON"]))|set(getFCMTokenList(data["newJSON"]))),"no")
  response = {"status":"success","data":"Expense updated successfully"}
 return HttpResponse(json.dumps(response),content_type="application/json")

@api_view(['POST','GET'])
@csrf_exempt
def groupDeleteAPI(request):
 data = json.loads(request.body)
 group=data["group"]
 userNumber=data["userNumber"] 
 group = Expensedetails.objects.get(id1=group["id1"],expenseVersion = group["expenseVersion"],object__contains = group["object"].split("##")[0] )
 if(userNumber in group.persons):
  group.persons = str(group.persons).replace(userNumber+":","")
 if (group.groupDeletedBy is None):
  group.groupDeletedBy = userNumber + ":"
 else:
  group.groupDeletedBy = group.groupDeletedBy + userNumber + ":"
 group.save()
 response = {"status":"success","data":"Group deleted successfully"}
 return HttpResponse(json.dumps(response),content_type="application/json")
@api_view(['POST','GET'])
@csrf_exempt
def updatemerchantvalue(request):
 data = json.loads(request.body)

 number ="8826795054"
 data= Merchant.objects.filter(number=number).update(status="1")
 return HttpResponse("json.dumps(response),content_type=")

 

@api_view(['POST','GET'])
@csrf_exempt
def migration (request):
 data = json.loads(request.body)
 oldExpenses = OldExpenseDetails.objects.all()
 oldMembers = OldExpenseParticipants.objects.all()
 oldUpdates = OldUpdateList.objects.all()
 oldGroups = OldRunningExpenses.objects.all()
 users = User.objects.all()
 
 for oldExpense in oldExpenses:
   expense = Expensedetails()
   expense.expenseVersion = "latest"
   expense.amount = oldExpense.amount
   expense.id1 = oldExpense.ID
   expense.description = oldExpense.description
   expense.addedby = oldExpense.addedby
   expense.owner = oldExpense.owner
   expense.date = oldExpense.date
 
   numberString = ""
   nameString = ""
   if ("other" not in oldExpense.object):
      for oldMember in oldMembers:
         if(oldMember.object == oldExpense.object):
            numberString = numberString + oldMember.participant + ":"
   else:
      if(oldExpense.distribution == "gavegroup"):
        numberString = oldExpense.owner + ":" + oldExpense.persons
      else:
        numberString = oldExpense.persons
   expense.persons = numberString
   for number in numberString[:-1].split(":"):
      name = "No name"
      for user in users:
         if(user.number == number):
           name = user.name
      if(name == "No name"):
        for oldMember in oldMembers:
           if(oldMember.participant == number):
              name = oldMember.participantname
      nameString = nameString + name + ":"
   
   expense.personsNames = nameString
   if(len(oldExpense.date) < 8):
     expense.deleted = "yes" + "##"  + oldExpense.addedby + "##" + "2016-08-19 15:25:26" 
   else:
     expense.deleted = "no"
    
   shareMoneyString = ""
   shareValueString = ""
   syncedString = ""
   if (oldExpense.distribution == "gavegroup"):
     oldNumbers = (oldExpense.owner + ":" + oldExpense.persons)[:-1].split(":")
     oldShares = ( "0.00" + ":" + oldExpense.shares)[:-1].split(":")
   else:
     oldNumbers = oldExpense.persons[:-1].split(":")
     oldShares = oldExpense.shares[:-1].split(":")
   newNumbers = numberString[:-1].split(":")
   oldDistribution = oldExpense.distribution[:1]
   for i in range(len(newNumbers)):
      syncedString = syncedString + newNumbers[i] + "_0:"
      if (newNumbers[i] in oldNumbers):
         for j in range(len(oldNumbers)):
            if (oldNumbers[j] == newNumbers[i]): 
               shareMoneyString = shareMoneyString + oldShares[j] + ":"
               if (oldDistribution == "0"):
                  shareValueString = shareValueString + oldShares[j] + ":"
               elif(oldDistribution == "1"):
                  shareValueString = shareValueString + oldShares[j] + ":"
               elif(oldDistribution == "2"):
                  shareVal = float(oldShares[j])*100/float(oldExpense.amount)
                  shareValueString = shareValueString + str(shareVal) + ":"
               elif(oldDistribution == "3"):
                  shareVal = float(oldShares[j])/float(min(oldShares))
                  shareValueString = shareValueString + str(shareVal) + ":"
               elif(oldDistribution == "g"):
                  shareValueString = shareValueString + oldShares[j] + ":"
      else:
         shareMoneyString = shareMoneyString + "0.00" + ":"
         shareValueString = shareValueString + "0.00" + ":"
   
   expense.shares = shareMoneyString
   expense.sharesValues = shareValueString
   expense.syncedString = syncedString
   if(oldDistribution == "0" and "0.00" in shareMoneyString):
     expense.distribution = "1"
   elif (oldDistribution == "g"):
     expense.distribution = "1"
   else:
     expense.distribution = str(oldDistribution)

   oldObject = oldExpense.object
   if (oldObject == "other"):
     groupIDString = "|other|##Others##|other|"
   else:
     for group in oldGroups:
       if(oldObject == group.ID):
         if("Others" in group.name):
           groupIDString = "|other|##Others##|other|"
         else:
           idValue = oldObject
           groupName = group.name
           if (group.agenda == "null" or group.agenda == ""):
             agenda = "no_agenda"
           else:
             agenda = group.agenda
           groupIDString = idValue + "##" + groupName + "##" + agenda
 
   expense.object = groupIDString 
   expense.save()
 #  particularExUpdates = []
 #  for update in oldUpdates:
 #     if (update.expenseid == oldExpense.ID):
 #        particularExUpdates.append(update)
    
 #  for i in range(len(particularExUpdates)):
 #     update = particularExUpdates[i]
 #     versionNo = i
 #     changedBy = expense.owner
 #     changedAt = update.date
 #     newUpdate = copy.deepcopy(expense)
 #     newUpdate.date = changedAt
 #     newUpdate.expenseVersion = versionNo + "##" + changedBy + "##" + changedAt
    
 #     if (update.type == "amount"):
 #        newUpdate.amount = update.old_val.split("@")[0]
 #     elif (update.type == "desc"):
 #        newUpdate.description = update.old_val

 #     if (i != 0):
 #       dist = particularExUpdates[i-1].dist
 #       if("Equally" in dist):
 #         newUpdate.distribution = "0"
 #       elif ("Manually" in dist):
 #         newUpdate.distribution = "1"      
 #       elif ("By parts" in dist):
 #         newUpdate.distribution = "2"
 #       else:
 #         newUpdate.distribution = "3"
 #     else:
 #       newUpdate.distribution = "0"
 response = {"status":"success","data":"Group deleted successfully"}
 return HttpResponse(json.dumps(response),content_type="application/json")

@api_view(['POST','GET'])
@csrf_exempt
def testAPI(request):
  coming = json.loads(request.body)
  print coming
  fcmToken = User.objects.get(number = "8930810019").fcmToken
  url = "https://fcm.googleapis.com/fcm/send"
  fcmList = []
  fcmList.append(fcmToken)
  data1 = {"data":coming,"registration_ids":fcmList}
  headers = {'content-type':"application/json",'authorization': "key=AIzaSyAyr0ors7D1lVnhescbztbu7Z8F1pKqwEw"}
  response = requests.post(url, data=json.dumps(data1), headers=headers)
  return HttpResponse(response.text,content_type="application/json")

def migrateGroups ():
  oldGroups = OldRunningExpenses.objects.all()
  for group in oldGroups:
    if ("other" not in group.object):
      newGroup = Expensedetails()
      newGroup.id1 = "Group Creation"
      newGroup.distribution = "Group Creation"
      newGroup.owner = "0"
      newGroup.date = group.date
      newGroup.description = group.date 

@api_view(['POST','GET'])
@csrf_exempt
def addUpdateAccountMerchantAPI(request):
 data = json.loads(request.body)
 p=MerchantAccounts.objects.update_or_create(defaults = data ,accountID = data["accountID"])
 AccountJson = json.loads(serializers.serialize("json",[p[0],]))[0]["fields"]
 if(p[1]==False):
  message = "Account updated successfully"
 else:
  message = "Account added successfully"
 if(AccountJson["defaultCreditAccount"] == "yes"):
  MerchantAccounts.objects.filter(merchantNumber = AccountJson["merchantNumber"]).exclude(accountID = AccountJson["accountID"]).update(defaultCreditAccount = "no")
 c1={"status":"success","message":message,"account":AccountJson}
 return HttpResponse(json.dumps(c1),content_type="application/json")

@api_view(['POST','GET'])
@csrf_exempt
def deleteAccountMerchantAPI(request):
 data = json.loads(request.body)
 p=MerchantAccounts.objects.filter(accountID = data["accountID"])
 if(p.count() == 0):
  c1={"status":"error","message":"Account does not exist"}
 else:
  p.delete()
  c1={"status":"success","message":"Account deleted successfully"}
 return HttpResponse(json.dumps(c1),content_type="application/json")
