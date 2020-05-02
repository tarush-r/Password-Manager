import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import os
import security
from tkinter import messagebox
from tkinter import *



def initialize():
	global loginid, loginpass, boxCreated
	loginid, loginpass, boxCreated= "default", "default", False
	print("befwERFVwfvgwrgfwRFW", boxCreated)


def display(frame, lbx):
	global loginid, loginpass, counter, boxCreated
	print(loginid)
	apps=list(db.collection(loginid).stream())
	print(len(apps))
	print(boxCreated)
	if boxCreated==True:
		# lbx.listNodes.delete(0,'end')
		lbx.delete(0, END)
		lbx.pack_forget()
		
		# lbx = Listbox(frame, width=50, height=15)
	
	if len(apps)!=0:
		print(loginid,loginpass)
		# if apps[0].to_dict()['username']==loginid and apps[0].to_dict()['password']==loginpass:
		for app in apps:
			if app.id != '0':
				lbx.insert(counter, "--------------------------------------------------------------------------------------------------")
				counter+=1
				lbx.insert(counter, "#"+app.id)
				counter+=1
				lbx.insert(counter, "                                                                                                  ")
				counter+=1
				lbx.insert(counter, "Username:                          "+str(security.decrypt(app.to_dict()['username'], loginpass))[2:-1])
				counter+=1
				lbx.insert(counter, "Password :                          "+str(security.decrypt(app.to_dict()['password'], loginpass))[2:-1])
				counter+=1
				lbx.insert(counter, "--------------------------------------------------------------------------------------------------")
				counter+=1
				# print(app.id)
				# print("\t", str(security.decrypt(app.to_dict()['username'], loginpass))[2:-1], "   ", str(security.decrypt(app.to_dict()['password'], loginpass))[2:-1])
		lbx.pack(side=LEFT)
		frame.pack(side=LEFT)
		boxCreated=True
		# else:
		# 	print("invalid credentials")
	# for app in apps:
	# 	print(app.to_dict()['username'], "  ", app.to_dict()['password'])
	# 	print(type(app.to_dict()['username']), "  ", type(app.to_dict()['password']))

	# 	if app.to_dict()['username']==loginid and app.to_dict()['password']==loginpass:
	# 		print('access granted')
	# 	break
	# if apps[0].to_dict().username==loginid and apps[0].to_dict().password==loginpass:
	# 	print("access granted")

def addApp(newappname, newappuser, newapppass):

	appname=newappname.get()
	appusername=security.encrypt(newappuser.get(), loginpass)
	apppassword=security.encrypt(newapppass.get(), loginpass)
	appref=db.collection(loginid).document(appname)
	appref.set({
		'username':appusername,
		'password':apppassword,
		})
	newappname.delete(0, END)
	newappuser.delete(0, END)
	newapppass.delete(0, END)
	messagebox.showinfo("Success", "Password Successfully Encrypted And Stored In Firebase")


def createUser(userfield, passfield, controller):
	global loginid
	global loginpass
	# loginid=input("Enter Username: ")
	loginid=userfield.get()
	if loginid=='':
		messagebox.showinfo("Error", "The Fields Can Not Be Empty")
	print(list(db.collection(loginid).stream()))
	if list(db.collection(loginid).stream()):
		# print('username taken')
		messagebox.showinfo("Error", "Username Taken")
	else:
		# loginpass=input('Enter Password: ')
		loginpass=passfield.get()
		if loginpass=="":
			messagebox.showinfo("Error", "The Fields Can Not Be Empty")
		db.collection(loginid).document('0').set({
			'username':security.encrypt(loginid, loginpass),
			'password':security.encrypt(loginpass, loginpass),
			})
		controller.show_frame("LoginPage")
		
def backToStart(controller):
	controller.show_frame("StartPage")

def logout(controller):
	loginid="default"
	loginpass="default"
	loginSuccess=False
	controller.show_frame("StartPage")


def takeMeTo(controller, name):
	controller.show_frame(name)

def login(userfield, passfield, controller):
	global loginid, loginpass, loginSuccess, counter
	counter=0
	loginSuccess=False
	# loginid=input("Enter username: ")
	# loginpass=input("Enter password: ")
	loginid=str(userfield.get())
	loginpass=str(passfield.get())
	if loginid=='' or loginpass=='':
		messagebox.showinfo("Error", "Empty fields cannot be accepted!")
	else:
		apps=list(db.collection(loginid).stream())
		if len(apps)!=0:
			print(str(security.decrypt(apps[0].to_dict()['username'], loginpass)[2:-1]))
			if str(security.decrypt(apps[0].to_dict()['username'], loginpass))[2:-1]==loginid and str(security.decrypt(apps[0].to_dict()['password'], loginpass))[2:-1]==loginpass:
				loginSuccess=True
				controller.show_frame("Choice")
				messagebox.showinfo("Success", "Login Successful")
			else:
				messagebox.showinfo("Error", "Invalid Credentials")
		else:
			messagebox.showinfo("Error", "User Does Not Exist")
		

	# while True:
	# 	choice=input("x to exit")
	# 	if choice=='x':
	# 		break
	# 	if int(choice)==1:
	# 		display(loginid, loginpass)
	# 	if int(choice)==2:
# 	# 		addApp(loginid, loginpass)
# credential_path = 'money-manager-333ad-firebase-adminsdk-r1tsm-4f4feeddf0.json'
# os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path
cred=credentials.Certificate({
  "type": "service_account",
  "project_id": "money-manager-333ad",
  "private_key_id": "4f4feeddf00a8aa83d8c014f1c07b03a79d06f54",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCVpNgTDaShu6DD\nfe2qdOQxTwms2/2uwAgWeMr/rxWew4a9y855H3M9kjNUreZgpHp8PyHV/MkIe1UR\n1nAExsLaS/GhuoEGbqNcgGepAfJr2z6hzc5CQqSQox+ZQq3kpMPHc3OPxdU5tUBY\n+l1fyF9WgxuMIxrELLdGbnKwAR025x8Rlx93KNp3u4TM25V+BjWhwMiABr+VR4l9\nXAgCQevnp9zjUhdoHSvCc4u6piSQacEBh66Q8/wLgAwU/cOdmnwuPnKPGEezQfHC\nAkGgpfO37HUHPFa0S32vFuITizJA+60R13/Di8NqyCdt0OFMJC7eN+N2kIQ5OFGn\n7+Z0Ij8jAgMBAAECggEASF5WGLDKY2Tn1GL8IykwiiAdH7msL2yy/JsiIRC9NfB9\nIyCDE9R/2NDxfgwzk503lwq5BFGhrzZl56B6v/SXmxaLHpmheEjdPAjlGLjWUg7P\ndVSgYS71gvVAfM/gZOjBvZ05z9fuzF+5ZM5/hajTYnU5R0Za1XCCmc8kK7X+OORD\nsoIlFL/cyuzDYtg8WhKEphk+Zaniq6lUpkn8jFeEzpK0BzeGe79HMag9bfYuyD/s\n+q31EcYz6+JZtSy4ieezkmn2a8qspdoOIfhwx5nsPKwV0g1WJWe3Vk4VVo/DLFMY\nZmRyDy4OultgByuT9ZaIPuYhhk7hCCsg9pUdctHS4QKBgQDFgF0oFsJvtKsNybl5\n0VeKOGO2lltR/9IeaeIIeNY52Mk7bDdP1feRJmbX95K0n9QkJtVGT5NNTukWdgNM\n4KeLiVHIsUiCEMEe8HmGHt32cRIwf2hZwuU+Ygrfc8+iFyTMstzZ7ssGR6drA3b7\nI1QRarE6EKwwGJGpLRVMXSd5qwKBgQDB96nKed4460bB8JtrJu6vFv4kayEcWLvl\n0iSIxDTPO3ni9MYdyw+gUhlXpcZbtfyF4LLk10PI37k10p7rMM6UnHq8RLTvlW22\nf95cfGmJEqOEJVMrsCLs8f0ihhpPsLHcVibkKHblvwityo3kJZgf/fumJb09eHME\n7y6CDWwIaQKBgG2RZx0Ec14RdwwxK2q/jrcpzXfQNl1pdSJWT4Wvs/lnoUwMHyt1\nYuDt0wRhXsxCFyjvOkbFgszSyFEjq3UM9SZeSjby020E6n7FnkWf/jfoRtUM+dFC\nZHeVYL7SuxALkujVGdz1s0CKpACkbW+qC8uVyziRY1VTbAvU7QnubCX9AoGBAKCZ\npk0OgK/SJoD37kdXMfNo7z5KMV0eH12XlEZlZnBbh30iPFN4yVRuBaurh8Rxt0dG\nF/kgP3C3xMtKu+hyPemQcpMltEZXDEM6NmuPW3ZyJ0+H9AhNS22yo2wNawWmgG22\nK3doBaIOfWogN0G62u1KRy13O+wEqf9g5rop0NRZAoGADFYjyH5OvO+Jpmz5xkED\nGjmW/IqWZfYIc/WiR1RoPx4PVOrZ+gZvIB+/tBcG8jGnRhaB2AGedw6s5yz3TB2K\nHbV+dTvEIJixQT16uaXQN4niYVZxktEGuIvU/P/otCo7itNxp4yGRo7nCgeFcd9q\nh7Fj4sHgZY/zj2lphxeBPSk=\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-r1tsm@money-manager-333ad.iam.gserviceaccount.com",
  "client_id": "102193214011524047346",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-r1tsm%40money-manager-333ad.iam.gserviceaccount.com"
}
)
# cred=credentials.Certificate('https://money-manager-333ad.firebaseio.com')
myApp=firebase_admin.initialize_app(cred)
db=firestore.client()

# while True:
# 	x=int(input("Enter 1 to login or 2 to create user: "))
# 	if x==1:
# 		login()
# 	else:
# 		createUser()



	# if int(choice)==3:
	# 	apps=list(db.collection(loginid).stream())
	# 	print(str(security.decrypt(apps[1].to_dict()['password'], loginpass))[2:-1])


# appUsername=input("Enter the username: ")
# appPassword=input("Enter the password: ")

# docs=db.collection("users").stream()
# for doc in docs:
# 	print(doc.id, ": ")
# 	print("\t")



# userRef=db.collection("users").document("user2")
# c=userRef.collection("gmail").document("id")
# print("hedvcasdvllo")
# userRef=db.collection("users")
# docs=userRef.stream()

# userRef.set({
# 	'username':'suernafaravc',
# 	'password':'passacfrv',
# 	'email':'heaefva',
# 	})  