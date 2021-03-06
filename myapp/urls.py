
from django.conf.urls import url 
from . import views
import myapp.views
from myapp import views
#from django.views.generic import TemplateView
urlpatterns = [
        
        url(r'^walletAPI', views.walletAPI, name='walletAPI'),
        url(r'^expenseAddAPI', views.expenseAddAPI, name='expenseAddAPI'),
        url(r'^addExpenseObjectsFriendAPI', views.addExpenseObjectsFriendAPI, name='addExpenseObjectsFriendAPI'),
        url(r'^expenseUpdateAPI', views.expenseUpdateAPI, name='expenseUpdateAPI'),
        url(r'^groupAddAPI', views.groupAddAPI, name='groupAddAPI'),
        url(r'^groupUpdateAPI', views.groupUpdateAPI, name='groupUpdateAPI'),
        url(r'^expenseDeleteAPI', views.expenseDeleteAPI, name='expenseDeleteAPI'),
        url(r'^groupDeleteAPI', views.groupDeleteAPI, name='groupDeleteAPI'),
        url(r'^verifyOTPMessageAPI', views.verifyOTPMessageAPI, name='verifyOTPMessageAPI'),
        url(r'^sendOTPMessageAPI', views.sendOTPMessageAPI, name='sendOTPMessageAPI'),     
        url(r'^refreshAPI', views.refreshAPI, name='refreshAPI'),
        url(r'^verifyReferralAPI', views.verifyReferralAPI, name='verifyReferralAPI'),
        url(r'^remindAPI', views.remindAPI, name='remindAPI'),
        url(r'^updateUserAPI', views.updateUserAPI, name='updateUserAPI'),
        url(r'^deleteUser', views.deleteUser, name='deleteUser'),
        url(r'^DeleteExpenseAllVersions',views.DeleteExpenseAllVersions, name = 'DeleteExpenseAllVersions'),
        url(r'^deleteExpense',views.deleteExpense, name = 'deleteExpense'),
        url(r'^sync',views.sync, name = 'sync'),
        url(r'^deleteAllExpenses',views.deleteAllExpenses, name = 'deleteAllExpenses'),
        url(r'^sendPushNotification',views.sendPushNotification, name = 'sendPushNotification'),
        url(r'^updateDynamicValue',views.updateDynamicValue, name = 'updateDyanamicValue'),
        url(r'^getAllMerchantsAPI',views.getAllMerchantsAPI, name = 'getAllMerchantsAPI'),
        url(r'^getMerchantUserAPI',views.getMerchantUserAPI, name = 'getMerchantUserAPI'),
        url(r'^refreshLiveOrdersUserAPI',views.refreshLiveOrdersUserAPI, name = 'refreshLiveOrdersUserAPI'),
        url(r'^merchantOfringAPI',views.merchantOfringAPI, name = 'merchantOfringAPI'),
        url(r'^placeOrderAPI',views.placeOrderAPI, name = 'placeOrderAPI'),
        url(r'^updateOrderUserAPI',views.updateOrderUserAPI, name = 'updateOrderUserAPI'),
        url(r'^migration',views.migration, name = 'migration'),     
        url(r'^testAPI',views.testAPI, name = 'testAPI'),
        url(r'^pushDynamicValues',views.pushDynamicValues, name = 'pushDynamicValues'),
        url(r'^getMerchantOrderAPI',views.getMerchantOrderAPI, name = 'getMerchantOrderAPI'),
        url(r'^sendQueryAPI',views.sendQueryAPI, name = 'sendQueryAPI'),
        url(r'^updateOrderStatusAPI',views.updateOrderStatusAPI, name = 'updateOrderStatusAPI'),
        url(r'^addMerchantOfferingAPI',views.addMerchantOfferingAPI, name = 'addMerchantOfferingAPI'),
        
        url(r'^addUpdateAccountAdminAPI',views.addUpdateAccountAdminAPI, name = 'addUpdateAccountAdminAPI'),
        url(r'^updateMerchantAPI',views.updateMerchantAPI, name = 'updateMerchantAPI'),
        url(r'^addUpdateHelperMerchantAPI',views.addUpdateHelperMerchantAPI, name = 'addUpdateHelperMerchantAPI'),
        url(r'^deleteHelperMerchantAPI',views.deleteHelperMerchantAPI, name = 'deleteHelperMerchantAPI'),
        url(r'^getMerchantAPI',views.getMerchantAPI, name  = 'getMerchantAPI'), 
        url(r'^updateOrderMerchantAPI',views.updateOrderMerchantAPI, name = 'updateOrderMerchantAPI'),
        url(r'^updateBulkOrdersMerchantAPI',views.updateBulkOrdersMerchantAPI, name = 'updateBulkOrdersMerchantAPI'),
        url(r'^refreshOrdersMerchantAPI',views.refreshOrdersMerchantAPI, name = 'refreshOrdersMerchantAPI'),
        url(r'^updatemerchantvalue',views.updatemerchantvalue, name = 'updatemerchantvalue'),

        url(r'^refreshOrdersHelperAPI',views.refreshOrdersHelperAPI, name = 'refreshOrdersHelperAPI'),
        url(r'^updateHelperAPI',views.updateHelperAPI, name = 'updateHelperAPI'),
        url(r'^updateOrderHelperAPI', views.updateOrderHelperAPI, name = 'updateOrderHelperAPI'),
        url(r'^test',views.test, name = 'test'),
        url(r'^updateHelperAPI',views.updateHelperAPI, name = 'updateHelperAPI'),        
        url(r'^addUpdateAccountMerchantAPI', views.addUpdateAccountMerchantAPI, name = 'addUpdateAccountMerchantAPI'),
        url(r'^deleteAccountMerchantAPI', views.deleteAccountMerchantAPI, name = 'deleteAccountMerchantAPI'),
        url(r'^getFilteredMerchantsAdminAPI',views.getFilteredMerchantsAdminAPI, name = 'getFilteredMerchantsAdminAPI'),
        url(r'^getSingleMerchantAdminAPI',views.getSingleMerchantAdminAPI, name = 'getSingleMerchantAdminAPI'),
        url(r'^updateMerchantAdminAPI',views.updateMerchantAdminAPI, name = 'updateMerchantAdminAPI'),
        url(r'^addUpdateHelperAdminAPI',views.addUpdateHelperAdminAPI, name = 'addUpdateHelperAdminAPI'),
        url(r'^deleteHelperAdminAPI',views.deleteHelperAdminAPI, name = 'deleteHelperAdminAPI'),
        url(r'^deleteAccountAdminAPI',views.deleteAccountAdminAPI, name = 'deleteAccountAdminAPI'),
        url(r'^getuserListAdminAPI',views.getuserListAdminAPI, name = 'getuserListAdminAPI'),        
        url(r'^sendPushNotificationAdminAPI',views.sendPushNotificationAdminAPI, name = 'sendPushNotificationAdminAPI'),

        url(r'^addSettlementAdminAPI', views.addSettlementAdminAPI, name = 'addSettlementAdminAPI'),
        url(r'^getSingleSettlementAdminAPI', views.getSingleSettlementAdminAPI, name = 'getSingleSettlementAdminAPI'),
        url(r'^getSingleSettlementMerchantAPI', views.getSingleSettlementMerchantAPI, name = 'getSingleSettlementMerchantAPI'),
        url(r'^addUserAdminAPI', views.addUserAdminAPI, name = 'addUserAdminAPI'),
        url(r'^getUserVPAUserAPI', views.getUserVPAUserAPI, name = 'getUserVPAUserAPI'),
        url(r'^getUserRefundAdminAPI', views.getUserRefundAdminAPI, name = 'getUserRefundAdminAPI'),
        url(r'^getLocationListAPI', views.getLocationListAPI, name = 'getLocationListAPI'),
        url(r'^addUpdateLocationAdminAPI', views.addUpdateLocationAdminAPI, name = 'addUpdateLocationAdminAPI'),
        url(r'^deleteLocationAdminAPI', views.deleteLocationAdminAPI, name = 'deleteLocationAdminAPI'),
        url(r'^notifyUserAfterRefundAdminAPI',views.notifyUserAfterRefundAdminAPI, name = 'notifyUserAfterRefundAdminAPI'),
        url(r'^getMerchantsInLocationAPI', views.getMerchantsInLocationAPI, name = 'getMerchantsInLocationAPI'),
]
