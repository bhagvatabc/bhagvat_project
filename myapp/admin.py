from django.contrib import admin
from django.db import models

# Register your models here.
#from .models import Merchantofferings
#from .models import Notifications
#from .models impor
from .models import OldRunningExpenses
#from .models import Getpaidback
from .models import Expensedetails
from .models import OldExpenseDetails
from .models import OldExpenseParticipants
from .models import OldUpdateList

from .models import Fcm
from .models import Otp


#from .models import Groups
#from .models import Pw2W                       Updatelist
#from .models import Userorder
#from .models import Dynamicvalue
#from .models import Deviceid
#from .models import Contree
#from .models import Pbanktransfer
from .models import User
from .models import Userfinal


admin.site.register(OldUpdateList)

admin.site.register(OldExpenseParticipants)
#admin.site.register(st2)
#admin.site.register(Notifications)
#admin.site.register(Merchantofferings)
#admin.site.register(Referral)
#admin.site.register(Waste)
admin.site.register(OldRunningExpenses)
#admin.site.register(Getpaidback)
admin.site.register(Expensedetails)
#admin.site.register(Groups)
#admin.site.register(Pw2W)
#admin.site.register(Userorder)
#admin.site.register(Dynamicvalue)
#admin.site.register(Deviceid)
#admin.site.register(Contree)
#admin.site.register(Pbanktransfer)
admin.site.register(User)
admin.site.register(Userfinal)
admin.site.register(Fcm)




