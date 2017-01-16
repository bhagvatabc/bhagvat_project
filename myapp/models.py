from __future__ import unicode_literals
from django.contrib import admin
from django.db import models
from django.db.models.signals import post_save#new
from django.dispatch import receiver#new
from rest_framework.authtoken.models import Token#new
from django.conf import settings#new
# Create your models here.
@receiver(post_save, sender=settings.AUTH_USER_MODEL)#
def create_auth_token(sender, instance=None, created=False, **kwargs):#
    if created:#
        Token.objects.create(user=instance)#  
class User(models.Model):
    p_id = models.AutoField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    number  = models.TextField(blank=True, null=True)
    consumerID  = models.TextField(blank=True, null=True)
    email  = models.TextField(blank=True, null=True)
    referredFrom  = models.TextField(blank=True, null=True)
    level  = models.TextField(blank=True, null=True)
    regId = models.TextField(blank=True, null=True)
    fcmToken  = models.TextField(blank=True, null=True)
    versionName  = models.TextField(blank=True, null=True)
    androidVersion = models.TextField(blank=True, null=True)
    brandName = models.TextField(blank=True, null=True)
    modelName  = models.TextField(blank=True, null=True)
    loginVersionName  = models.TextField(blank=True, null=True)
    userType  = models.TextField(blank=True, null=True)
    referralCode  = models.TextField(blank=True, null=True)
    referralCount = models.TextField(blank=True, null=True)
    date= models.TextField(blank=True, null=True)
    vpa = models.TextField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'User'

#admin.site.register(User) 
class Userfinal(models.Model):
    p_id = models.AutoField(primary_key=True)
    id = models.TextField(blank=True, null=True)
    level = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    email = models.TextField(blank=True, null=True)
    consumerid = models.TextField(blank=True, null=True)
    created_at = models.TextField(blank=True, null=True)
    perishable_token = models.TextField(blank=True, null=True)
    session_token = models.TextField(blank=True, null=True)
    regid = models.TextField(blank=True, null=True)
    username = models.TextField(blank=True, null=True)
    updated_at = models.TextField(blank=True, null=True)
    totalreferalcount = models.TextField(blank=True, null=True)
    referalused = models.TextField(blank=True, null=True)
    column_12 = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'userfinal'

class OldExpenseParticipants(models.Model):
    p_id = models.AutoField(primary_key=True)
    ID = models.TextField(blank=True, null=True)
    share = models.TextField(blank=True, null=True)
    object = models.TextField(blank=True, null=True)
    settled = models.TextField(blank=True, null=True)
    participantname = models.TextField(blank=True, null=True)
    participant = models.TextField(blank=True, null=True)
    saved = models.TextField(blank=True, null=True)

    def __unicode__(self):
     return self.object
    class Meta:
        managed = False
        db_table = 'oldExpenseParticipants'


class Expensedetails(models.Model):
    p_id = models.AutoField(primary_key=True)
    id1 = models.TextField( blank=True, null=True)  # Field renamed because it started with '_'.
    description = models.TextField(blank=True, null=True)
    amount = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    object = models.TextField(blank=True, null=True)
    addedby = models.TextField(blank=True, null=True)
    shares = models.TextField(blank=True, null=True)
    persons = models.TextField(blank=True, null=True)
    distribution = models.TextField(blank=True, null=True)
    owner = models.TextField(blank=True, null=True)
    date = models.TextField(blank=True, null=True)
    personsNames =  models.TextField(blank=True, null=True)
    sharesValues =  models.TextField(blank=True, null=True)
    expenseVersion =  models.TextField(blank=True, null=True)
    syncedString =  models.TextField(blank=True, null=True)
    deleted =  models.TextField(blank=True, null=True)
    groupDeletedBy =  models.TextField(blank=True, null=True)
    def __unicode__(self):
     return self.object
 
    class Meta:
        managed = False
        db_table = 'expensedetails'

class OldExpenseDetails(models.Model):
    p_id = models.AutoField(primary_key=True)
    ID = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    amount = models.TextField(blank=True, null=True)
    object = models.TextField(blank=True, null=True)
    addedby = models.TextField(blank=True, null=True)
    shares = models.TextField(blank=True, null=True)
    persons = models.TextField(blank=True, null=True)
    distribution = models.TextField(blank=True, null=True)
    owner = models.TextField(blank=True, null=True)
    date = models.TextField(blank=True, null=True)
    def __unicode__(self):
     return self.object

    class Meta:
        managed = False
        db_table = 'oldExpenseDetails'

class OldRunningExpenses(models.Model):
    p_id = models.AutoField(primary_key=True)
    saved = models.TextField(blank=True, null=True)
    agenda = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    contreemoney = models.TextField(blank=True, null=True)
    date = models.TextField(blank=True, null=True)
    ID = models.TextField(blank=True, null=True)
    def __unicode__(self):
     return self.object

    class Meta:
        managed = False
        db_table = 'oldRunningExpenses'

  
class OldUpdateList(models.Model):
    p_id = models.AutoField(primary_key=True)
    ID = models.TextField(blank=True, null=True)
    object = models.TextField(blank=True, null=True)
    dist = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)
    expenseid = models.TextField(blank=True, null=True)
    new_val = models.TextField(blank=True, null=True)
    date = models.TextField(blank=True, null=True)
    old_val = models.TextField(blank=True, null=True)
    def __unicode__(self):
     return self.object

    class Meta:
        managed = False
        db_table = 'oldUpdateList'

class Fcm(models.Model):
    instance_token = models.TextField(blank=True, null=True)
    p_id = models.AutoField(primary_key=True)
    def __unicode__(self):
     return self.instance_token

    class Meta:
        managed = False
        db_table = 'FCM'

class Merchantofferings(models.Model):
    p_id = models.AutoField(primary_key=True)

    id = models.TextField(blank=True, null=True)
    rperm = models.TextField(blank=True, null=True)
    itemslist = models.TextField(blank=True, null=True)
    created_at = models.TextField(blank=True, null=True)
    acl = models.TextField(blank=True, null=True)
    wperm = models.TextField(blank=True, null=True)
    updated_at = models.TextField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    merchantname = models.TextField(blank=True, null=True)
    available = models.TextField(blank=True, null=True)
    itemprice = models.TextField(blank=True, null=True)
    merchantnumber = models.TextField(blank=True, null=True)
    conveniencefee = models.TextField(blank=True, null=True)
    netamount = models.IntegerField(blank=True, null=True)
    settledamount = models.IntegerField(blank=True, null=True)
    column_16 = models.IntegerField(blank=True, null=True)
#    p_id = models.AutoField()

    class Meta:
        managed = False
        db_table = 'merchantofferings'
class Referral(models.Model):
    p_id = models.AutoField(primary_key=True)

    id = models.TextField(blank=True, null=True)
    referralcount = models.IntegerField(blank=True, null=True)
    rperm = models.TextField(blank=True, null=True)
    referralcode = models.TextField(blank=True, null=True)
    acl = models.TextField(blank=True, null=True)
    wperm = models.TextField(blank=True, null=True)
    created_at = models.TextField(blank=True, null=True)
    username = models.TextField(blank=True, null=True)
    updated_at = models.TextField(blank=True, null=True)
    column_10 = models.TextField(blank=True, null=True)
    totalreferalcount = models.TextField(blank=True, null=True)
    referalused = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'referral'
class Userorder(models.Model):
    p_id = models.AutoField(primary_key=True)

    ETA = models.TextField(blank=True, null=True)
    itemsQuantity = models.TextField(blank=True, null=True)
    itemsAvailability = models.TextField(blank=True, null=True)
    category = models.TextField(blank=True, null=True)
    confreeStatus = models.TextField(blank=True, null=True)
    dateTime = models.TextField(blank=True, null=True)
    itemsPrice = models.TextField(blank=True, null=True)
    itemsName = models.TextField(blank=True, null=True)
    merchantName = models.TextField(blank=True, null=True)
    merchantNumber = models.TextField(blank=True, null=True)
    netPrice = models.TextField(blank=True, null=True)
    orderID = models.TextField(blank=True, null=True)
    orderNo = models.TextField(blank=True, null=True)
    status = models.TextField(blank=True, null=True)
    userName = models.TextField(blank=True, null=True)
    userNumber = models.TextField(blank=True, null=True)
    isSettled = models.TextField(blank=True, null=True)
    paymentMode = models.TextField(blank=True, null=True)
    refundValue = models.TextField(blank=True, null=True)
    convenienceFee = models.TextField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'userorder'


class Otp(models.Model):
    mobileNumber = models.TextField(blank=True, null=True)
    otp = models.TextField(blank=True, null=True)
    p_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'otp'
    def __unicode__(self):
     return self.otp


class PushNotification(models.Model):
    p_id = models.AutoField(primary_key=True)
    title = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    information = models.TextField(blank=True, null=True)
    time = models.TextField(blank=True, null=True)
    notificationID = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pushNotification'

class Merchant(models.Model):
    name = models.TextField(blank=True, null=True)
    number = models.TextField(blank=True, null=True)
    consumerID = models.TextField( blank=True, null=True)  # Field name made lowercase.
    email = models.TextField(blank=True, null=True)
    referredFrom = models.TextField( blank=True, null=True)  # Field name made lowercase.
    level = models.TextField(blank=True, null=True)
    regId = models.TextField(blank=True, null=True)  # Field name made lowercase.
    fcmToken = models.TextField(blank=True, null=True)  # Field name made lowercase.
    versionName = models.TextField(blank=True, null=True)  # Field name made lowercase.
    androidVersion = models.TextField( blank=True, null=True)  # Field name made lowercase.
    brandName = models.TextField(blank=True, null=True)  # Field name made lowercase.
    modelName = models.TextField(blank=True, null=True)  # Field name made lowercase.
    loginVersionName = models.TextField( blank=True, null=True)  # Field name made lowercase.
    userType = models.TextField(blank=True, null=True)  # Field name made lowercase.
    referralCode = models.TextField( blank=True, null=True)  # Field name made lowercase.
    referralCount = models.TextField( blank=True, null=True)  # Field name made lowercase.
    p_id = models.AutoField(primary_key=True)
    isVerified = models.TextField(blank=True, null=True)  # Field name made lowercase.
    location = models.TextField(blank=True, null=True)
    paymentType = models.TextField(blank=True, null=True)  # Field name made lowercase.
    status = models.TextField(blank=True, null=True)
    itemsName = models.TextField( blank=True, null=True)  # Field name made lowercase.
    convenienceFee = models.TextField(blank=True, null=True)  # Field name made lowercase.
    itemsPrice = models.TextField( blank=True, null=True)  # Field name made lowercase.
    itemsAvailability = models.TextField(blank=True, null=True)
    address = models.TextField(blank=True, null=True) 
    personName = models.TextField(blank=True, null=True)
    mobileNo = models.TextField(blank=True, null=True)
    isBlocked = models.TextField(blank=True, null=True)
    pin = models.TextField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'Merchant'


class DynamicValue(models.Model):
    defaultConfreeValue = models.TextField(blank=True, null=True)  
    maxValue = models.TextField(blank=True, null=True)  
    contactNumber = models.TextField(blank=True, null=True)  
    updateInfo = models.TextField(blank=True, null=True)  
    maxBankTransactionOneGo = models.TextField( blank=True, null=True)  
    minBankTransactionOneGo = models.TextField( blank=True, null=True)
    bankTransactionCharges = models.TextField(blank=True, null=True)  
    maxFreeBankTransaction = models.TextField( blank=True, null=True)  
    minFixedBankTransferCharges = models.TextField(blank=True, null=True)
    identifier = models.TextField(blank=True, null=True)
    connectionToken= models.TextField(blank=True, null=True)  
    p_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'DynamicValue'

class PW2W(models.Model):
    confreeStatus = models.TextField( blank=True, null=True)  # Field name made lowercase.
    senderName = models.TextField(blank=True, null=True)  # Field name made lowercase.
    recipientNumber = models.TextField(blank=True, null=True)  # Field name made lowercase.
    recipientName = models.TextField( blank=True, null=True)  # Field name made lowercase.
    senderConsumerID = models.TextField( blank=True, null=True)  # Field name made lowercase.
    model = models.TextField(blank=True, null=True)
    date = models.TextField(blank=True, null=True)
    transactionStatus = models.TextField(blank=True, null=True)  # Field name made lowercase.
    userNumber = models.TextField(blank=True, null=True)  # Field name made lowercase.
    amount = models.TextField(blank=True, null=True)
    version = models.TextField(blank=True, null=True)
    p_id = models.AutoField(primary_key=True)


    class Meta:
        managed = False
        db_table = 'PW2W'

class PMerchantPayment(models.Model):
    date = models.TextField(blank=True, null=True)
    transactionStatus = models.TextField(blank=True, null=True)  # Field name made lowercase.
    userNumber = models.TextField(blank=True, null=True)  # Field name made lowercase.
    amount = models.TextField(blank=True, null=True)
    orderID = models.TextField(blank=True, null=True)  # Field name made lowercase.
    orderNo = models.TextField(blank=True, null=True)  # Field name made lowercase.
    merchantNumber = models.TextField(blank=True, null=True)  # Field name made lowercase.
    consumerID = models.TextField(blank=True, null=True)  # Field name made lowercase.
    merchantName = models.TextField(blank=True, null=True)  # Field name made lowercase.
    userName = models.TextField(blank=True, null=True)  # Field name made lowercase.
    p_id = models.AutoField(primary_key=True)


    class Meta:
        managed = False
        db_table = 'PMerchantPayment'


class PAddCash(models.Model):
    consumerID = models.TextField(blank=True, null=True)  # Field name made lowercase.
    transactionStatus = models.TextField(blank=True, null=True)  # Field name made lowercase.
    userNumber = models.TextField( blank=True, null=True)  # Field name made lowercase.
    amount = models.TextField(blank=True, null=True)
    version = models.TextField(blank=True, null=True)
    userName = models.TextField(blank=True, null=True)  # Field name made lowercase.
    p_id = models.AutoField(primary_key=True)


    class Meta:
        managed = False
        db_table = 'PAddCash'


class PBankTransfer(models.Model):
    consumerID = models.TextField(blank=True, null=True)  # Field name made lowercase.
    transactionStatus = models.TextField(blank=True, null=True)  # Field name made lowercase.
    userNumber = models.TextField(blank=True, null=True)  # Field name made lowercase.
    amount = models.TextField(blank=True, null=True)
    version = models.TextField(blank=True, null=True)
    userName = models.TextField(blank=True, null=True)  # Field name made lowercase.
    p_id = models.AutoField(primary_key=True)


    class Meta:
        managed = False
        db_table = 'PBankTransfer'



class Olduser(models.Model):
    level = models.TextField(blank=True, null=True)
    Name = models.TextField(blank=True, null=True)  
    email = models.TextField(blank=True, null=True)
    consumerID = models.TextField(blank=True, null=True)  
    regID = models.TextField(blank=True, null=True)  
    username = models.TextField(blank=True, null=True)
    referredFrom = models.TextField(blank=True, null=True)  
    referresdFrom = models.TextField( blank=True, null=True)  
    p_id = models.AutoField(primary_key=True)


    class Meta:
        managed = False
        db_table = 'oldUser'



class Oldreferral(models.Model):
    referralcount = models.TextField(blank=True, null=True)
    referralcode = models.TextField(blank=True, null=True)
    username = models.TextField(blank=True, null=True)
    p_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'oldReferral'

class Helper(models.Model):
    name = models.TextField(blank=True, null=True)
    number  = models.TextField(blank=True, null=True)
    designation = models.TextField(blank=True, null=True)
    privilege = models.TextField(blank=True, null=True)
    fcmToken = models.TextField(blank=True, null=True)
    merchantNumber = models.TextField(blank=True, null=True)
    p_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'Helper'

class MerchantAccounts(models.Model):
    name = models.TextField(blank=True, null=True)
    number = models.TextField(blank=True, null=True)
    bank = models.TextField(blank=True, null=True)
    ifscCode = models.TextField(db_column='ifscCode', blank=True, null=True) 
    accountID = models.TextField(db_column='accountID', blank=True, null=True)
    merchantNumber = models.TextField(db_column='merchantNumber', blank=True, null=True)
    defaultCreditAccount = models.TextField(db_column='defaultCreditAccount', blank=True, null=True)
    contactNumber = models.TextField(db_column='contactNumber', blank=True, null=True) 
    contactAddress = models.TextField(db_column='contactAddress', blank=True, null=True)
    accountType = models.TextField(db_column='accountType', blank=True, null=True) 
    category = models.TextField(blank=True, null=True)
    p_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'MerchantAccounts'

class Settlement(models.Model):
    merchantNumber = models.TextField(blank=True, null=True)  # Field name made lowercase.
    amount = models.TextField(blank=True, null=True)
    dateTime = models.TextField(blank=True, null=True)  # Field name made lowercase.
    settlementID = models.TextField(blank=True, null=True)  # Field name made lowercase.
    merchantAccount = models.TextField(blank=True, null=True)  # Field name made lowercase.
    companyAccount = models.TextField(blank=True, null=True)
    p_id = models.AutoField(primary_key=True)
    carriedOver = models.TextField(blank=True, null=True)  # Field name made lowercase.
    numberOfOrders= models.TextField(blank=True, null=True)
    carriedFromLast = models.TextField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'Settlement'

class Location(models.Model):
    name = models.TextField(blank=True, null=True)
    state = models.TextField(blank=True, null=True)
    pin = models.TextField( blank=True, null=True)
    p_id = models.AutoField(primary_key=True)
    class Meta:
        managed = False
        db_table = 'Location'
