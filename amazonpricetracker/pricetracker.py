import smtplib
from selenium import webdriver
from  selenium.webdriver.chrome.options import Options

email_1=input("Enter Your Primary Email")
pass_1=input("Enter Your Primary email's Password")
email_2=input("Enter Your Secondry Email")


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com')
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(email_1, pass_1)
    subject = "Price Of the Product has been dropped!!!"
    body = "The item have been droped.Check Out at\n" + URL[8:]
    msg = f"Subject:{subject}\n\n{body}"
    server.sendmail(email_1, email_2, msg)
    print("Email Sent")
    server.quit()

URL='https://www.amazon.in/Test-Exclusive-547/dp/B078BNQ318/ref=sr_1_1?crid=12RY3094ZREOK&dchild=1&keywords=oneplus+nord&qid=1595365065&sprefix=One%2Caps%2C604&sr=8-1'
options = Options()
options.headless = True
driver=webdriver.Chrome(executable_path="G:\\chromedriver_win32\\chromedriver.exe",chrome_options=options);
print(URL)
driver.get(URL)
MRP=driver.find_element_by_id('priceblock_ourprice').text
MRP=MRP.replace(',','').replace('.','')
MRP=float(MRP[1:])/100
if MRP > 41000:
    print("Email Sending")
    send_mail()
