#coding: utf-8
import sys
import os
import datetime 
import traceback
import decimal
import simplejson
from hashlib import sha256
from hmac import HMAC

def safe_new_datetime(d):
    kw = [d.year, d.month, d.day]
    if isinstance(d, datetime.datetime):
        kw.extend([d.hour, d.minute, d.second, d.microsecond, d.tzinfo])
    return datetime.datetime(*kw)

def safe_new_date(d):
    return datetime.date(d.year, d.month, d.day)

class DatetimeJSONEncoder(simplejson.JSONEncoder):
    """可以序列化时间的JSON"""

    DATE_FORMAT = "%Y-%m-%d"
    TIME_FORMAT = "%H:%M:%S"

    def default(self, o):
        if isinstance(o, datetime.datetime):
            d = safe_new_datetime(o)
            return d.strftime("%s %s" % (self.DATE_FORMAT, self.TIME_FORMAT))
        elif isinstance(o, datetime.date):
            d = safe_new_date(o)
            return d.strftime(self.DATE_FORMAT)
        elif isinstance(o, datetime.time):
            return o.strftime(self.TIME_FORMAT)
        elif isinstance(o, decimal.Decimal):
            return str(o)
        else:
            return super(DatetimeJSONEncoder, self).default(o)
            
def print_err():
    '''
    @todo: 打印错误信息
    '''
    sys.stderr.write('=='*30+os.linesep)
    sys.stderr.write('err time: '+str(now())+os.linesep)
    sys.stderr.write('--'*30+os.linesep)
    traceback.print_exc(file=sys.stderr)
    sys.stderr.write('=='*30+os.linesep)
    
def now():
    return datetime.datetime.now()

def form2dic(form):
    temp_dic = {}
    for i in form:
        temp_dic[i] = form[i]
    return temp_dic

def encrypt_password(password, salt=None):
    """Hash password on the fly."""
    if salt is None:
        salt = os.urandom(8) # 64 bits.
    
    assert 8 == len(salt)
    assert isinstance(salt, str)
    
    if isinstance(password, unicode):
        password = password.encode('UTF-8')
    
    assert isinstance(password, str)
    
    result = password
    for i in xrange(10):
        result = HMAC(result, salt, sha256).digest()
    
    return salt + result