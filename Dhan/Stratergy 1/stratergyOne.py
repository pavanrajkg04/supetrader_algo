# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 11:28:09 2024

@author: Administrator
"""
from dhanhq import dhanhq
from dhanhq import marketfeed 

access_token = ""
client_ID = ""

dhan = dhanhq(client_ID,access_token)

Fund_details = dhan.get_fund_limits()

print(Fund_details['data']['availabelBalance'])