
import mechanicalsoup
import time
from bs4 import BeautifulSoup
print("Enter user id")
rid= input()
print("Enter password")
pwd= raw_input()
browser = mechanicalsoup.StatefulBrowser()
browser.open("http://14.139.108.229/W27/login.aspx?ReturnUrl=%2fW27%2fMyInfo%2fw27MyInfo.aspx")
browser.select_form()
browser["txtUserName"] = rid
browser["Password1"] = pwd

browser.submit_selected() #login


submit = browser.get_current_page().find('input', id='ctl00_ContentPlaceHolder1_CtlMyLoans1_grdLoans_ctl02_Button1') 
form = browser.select_form()
form.choose_submit(submit)
response = browser.submit_selected() #REISSUE
soup=BeautifulSoup(response.text,'html.parser')
output = soup.findAll("span", {"id": "ctl00_ContentPlaceHolder1_CtlMyLoans1_grdLoans_ctl02_lblFine"})[0].string #displays finedue now
print(output) #DISPLAY FINEDUE NOW

