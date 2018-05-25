# -*- coding: utf-8 -*-
"""
Created on Sun May 20 11:20:25 2018

@author: Administrator
"""

import urllib

#Cookie: anonymid=jg4i053e-z6m31j; _r01_=1; _de=7113E26C6AAF3646A83FD76533146E3C; depovince=BJ; jebecookies=5d5ffcea-8df5-47c4-932a-dbe9879e2bb2|||||; JSESSIONID=abcyv2N_xFr-ldAz9H7nw; ick_login=126373ff-22bd-47ab-9616-f1ebfa04ddca; p=1e7dc40576dee829a88a8984e33432449; first_login_flag=1; ln_uact=18210577472; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; t=5d5ea5d8c2b4623c1882bb04cf1ced0e9; societyguester=5d5ea5d8c2b4623c1882bb04cf1ced0e9; id=961482489; xnsid=8477e635; loginfrom=syshome; ch_id=10016; jebe_key=8a0b5944-91f1-4788-a8ca-732ded5f4ba8%7C65617699d9107c4fa92a82edbc369e2a%7C1526785908966%7C1%7C1526785698167; wp_fold=0


# 这样管理cookie，可维护性差；
url = "http://www.renren.com/961482489/profile"
headers = {"Connection": "keep-alive",
           "Cookie":"anonymid=jg4i053e-z6m31j; _r01_=1; _de=7113E26C6AAF3646A83FD76533146E3C; depovince=BJ; jebecookies=5d5ffcea-8df5-47c4-932a-dbe9879e2bb2|||||; JSESSIONID=abcyv2N_xFr-ldAz9H7nw; ick_login=126373ff-22bd-47ab-9616-f1ebfa04ddca; p=1e7dc40576dee829a88a8984e33432449; first_login_flag=1; ln_uact=18210577472; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; t=5d5ea5d8c2b4623c1882bb04cf1ced0e9; societyguester=5d5ea5d8c2b4623c1882bb04cf1ced0e9; id=961482489; xnsid=8477e635; loginfrom=syshome; ch_id=10016; jebe_key=8a0b5944-91f1-4788-a8ca-732ded5f4ba8%7C65617699d9107c4fa92a82edbc369e2a%7C1526785908966%7C1%7C1526785698167; wp_fold=0",
           "Host":"www.renren.com",
           "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36"}

req = urllib.request.Request(url, headers=headers)
response = urllib.request.urlopen(req)

with open("myRenren.html","wb") as f:
    f.write(response.read())

