##### TEST FUNCTIONS - FUNCTIONS HAVE BEEN MODIFIED TO NOT TAKE SELF
#def getNumbers(address):
#  numbers = []
#  while(len(address) > 2):
#    startIndex = address.index("\n")
#    if(address[startIndex-1] in "0123456789"):
#      #Friendly fact. Text messages take 10 length numbers!
#      numbers += [address[startIndex-10:startIndex]]
#      address = address[startIndex+1:]
#    else:
#      address = address[startIndex+1:]
#  return numbers
#
#def testGetNumbers():
#    print "Testing getNumber...,"
#    string = "viveknanagia 2435463736\n vivek pizza@#)(*lkasdj2345325323\n"
#    assert(getNumbers(string)==['2435463736', '2345325323'])
#    string = "348lkasjdasld3lds6473627485\ndjf83klr0330i&^Q(OIH\n"
#    assert(getNumbers(string)==['6473627485'])
#    print "Passed"
#
#testGetNumbers()
    
### CODE ##################################################################
import android, random
import datetime
from fullscreenwrapper2 import *
'''
@copyright: Hariharan Srinath, 2012
fullscreenwrapper2 (c)
http://code.google.com/p/python-for-android/wiki/fullscreenwrapper2
'''
 
viewTextsLayout="""<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
        android:id="@+id/background"
        android:orientation="vertical"
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        android:background="#ff000000">
	android:layout_gravity="center"
    <ListView
	    android:id="@+id/list_texts"
	    android:layout_width="fill_parent"
	    android:layout_height="0px"
	    android:layout_weight="55"/>
    <Button
      android:id="@+id/chooseSrt"
      android:layout_width="fill_parent"
      android:layout_height="wrap_content"
      android:text="Choose Sort"       
      android:layout_marginBottom="5sp"
      android:layout_marginLeft="2sp"
      android:layout_marginRight="5sp"
      android:layout_marginTop="5sp"/>
    <Button
        android:id="@+id/quit"
        android:layout_width="fill_parent"
        android:layout_height="wrap_content"
        android:text="Return"  
        android:layout_marginBottom="5sp"
        android:layout_marginLeft="2sp"
        android:layout_marginRight="5sp"
        android:layout_marginTop="10sp"/>
</LinearLayout>
"""
 
sendTextLayout="""<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
        android:id="@+id/background"
        android:orientation="vertical"
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        android:background="#ff000000">
	android:layout_gravity="center"
    <Button
        android:id="@+id/chooseContact"
        android:layout_width="fill_parent"
        android:layout_height="wrap_content"
        android:text="Choose Contact"  
        android:layout_marginBottom="5sp"
        android:layout_marginLeft="2sp"
        android:layout_marginRight="5sp"
        android:layout_marginTop="50sp"/>
    <LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
        xmlns:tools="http://schemas.android.com/tools"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:orientation="horizontal">
        <TextView
            android:id="@+id/currentContact"
            android:layout_height="wrap_content"
            android:layout_width="wrap_content"
            android:layout_marginLeft="5sp"
            android:layout_marginRight="10sp"
            android:text="Current Contact" />
        <EditText android:id="@+id/contact"
            android:layout_weight="1"
            android:layout_width="0dp"
            android:layout_height="wrap_content"
            android:text= "Type_Contact_Number_Here"
            android:hint="Type Contact Number Here" />
    </LinearLayout>
    <EditText android:id="@+id/edit_SMS"
        android:layout_weight="1"
        android:layout_width="match_parent"
        android:layout_height="0dp"
        android:text="Enter_SMS_Here"
        android:hint="Enter SMS Here" />
    <LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
        xmlns:tools="http://schemas.android.com/tools"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:orientation="horizontal">
        <Button
            android:layout_weight="1"    
            android:id="@+id/checkLength"
            android:layout_width="0dp"
            android:layout_height="wrap_content"
            android:text="Check Message Length"  
            android:layout_marginBottom="5sp"
            android:layout_marginLeft="2sp"
            android:layout_marginRight="5sp"
            android:layout_marginTop="5sp"/>
        <Button
            android:layout_weight="1" 
            android:id="@+id/speechToText"
            android:layout_width="0dp"
            android:layout_height="wrap_content"
            android:text="Speech To Text"  
            android:layout_marginBottom="5sp"
            android:layout_marginLeft="2sp"
            android:layout_marginRight="5sp"
            android:layout_marginTop="5sp"/>
    </LinearLayout>
    <Button
        android:id="@+id/sendSMS"
        android:layout_width="fill_parent"
        android:layout_height="wrap_content"
        android:text="Send Text"  
        android:layout_marginBottom="5sp"
        android:layout_marginLeft="2sp"
        android:layout_marginRight="5sp"
        android:layout_marginTop="5sp"/>
    <Button
        android:id="@+id/backToTitle"
        android:layout_width="fill_parent"
        android:layout_height="wrap_content"
        android:text="Return"  
        android:layout_marginBottom="5sp"
        android:layout_marginLeft="2sp"
        android:layout_marginRight="5sp"
        android:layout_marginTop="5sp"/>
</LinearLayout>
"""
 
aboutLayout="""<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
        android:id="@+id/background"
        android:orientation="vertical"
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        android:background="#ff000000">
	android:layout_gravity="center"
    <TextView
        android:id="@+id/aboutStatement"
        android:layout_width="fill_parent"
        android:layout_height="0dp"
        android:gravity="center"
	android:layout_weight="1"
        android:textSize="10sp"
        android:singleLine="false"
        android:text="Hi" />
    <Button
        android:id="@+id/backToTitle"
        android:layout_width="fill_parent"
        android:layout_height="wrap_content"
        android:text="Return"  
        android:layout_marginBottom="5sp"
        android:layout_marginLeft="2sp"
        android:layout_marginRight="5sp"
        android:layout_marginTop="50sp"/>
</LinearLayout>
"""
 
titleLayout="""<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
        android:id="@+id/background"
        android:orientation="vertical"
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        android:background="#ff000000">
	android:layout_gravity="center"
    <ImageView
        android:id="@+id/title"
        android:layout_width="370dp"
        android:layout_height="185dp"
        android:src="file:///mnt/sdcard/sl4a/scripts/title.png" />
    <Button
        android:id="@+id/sendTextButton"
        android:layout_width="fill_parent"
        android:layout_height="wrap_content"
        android:text="Send Text"
        android:layout_marginBottom="5sp"
        android:layout_marginLeft="5sp"
        android:layout_marginRight="2sp"
        android:layout_marginTop="15sp" />
    <Button
        android:id="@+id/viewTextButton"
        android:layout_width="fill_parent"
        android:layout_height="wrap_content"
        android:text="View Texts" 
        android:layout_marginBottom="5sp"
        android:layout_marginLeft="2sp"
        android:layout_marginRight="5sp"
        android:layout_marginTop="50sp"/>
    <Button
        android:id="@+id/aboutButton"
        android:layout_width="fill_parent"
        android:layout_height="wrap_content"
        android:text="About" 
        android:layout_marginBottom="5sp"
        android:layout_marginLeft="2sp"
        android:layout_marginRight="5sp"
        android:layout_marginTop="50sp"/>
    <Button
        android:id="@+id/closeButton"
        android:layout_width="fill_parent"
        android:layout_height="wrap_content"
        android:text="Quit"  
        android:layout_marginBottom="5sp"
        android:layout_marginLeft="2sp"
        android:layout_marginRight="5sp"
        android:layout_marginTop="50sp"/>
</LinearLayout>
"""
  
###############################################################################
 
class ViewTextLayout(Layout):
    def __init__(self):
        #Create a list to store each text
        self.lst_view_items =[]
        super(ViewTextLayout,self).__init__(viewTextsLayout,"PySMS")
 
    def on_show(self):
        self.chooseSort()
        #Event handler for list clicks
        self.views.list_texts.add_event(itemclick_EventHandler(
            self.views.list_texts, self.returnContact))
        self.views.chooseSrt.add_event(click_EventHandler(
            self.views.chooseSrt, self.chooseSortHelper))
        self.views.quit.add_event(click_EventHandler
                                  (self.views.quit, self.cancel))
    
    def cancel(self,view,eventdata):
        FullScreenWrapper2App.close_layout()
    
    def on_close(self):
        pass
    
    def chooseSortHelper(self,view,eventdata):
       self.chooseSort()
 
    #Create an alart box   
    def chooseSort(self):
        #Define choices
        a = "Date"
        b = "Contact"
        c = "Opened"
        d = "Closed"
        #Create and show dialog
        droid.dialogCreateAlert("Choose Sort")
        droid.dialogSetItems([a,b,c,d])
        droid.dialogShow()
        #Get response and get value of response
        response = droid.dialogGetResponse().result
        #If hit back button, error pops up so use try/except
        try:
            pick = response['item']
            if(pick == 0): self.sortData()
            elif(pick==1): self.sortContact()
            elif(pick==2): self.sortOpened()
            elif(pick==3): self.sortClosed()
        except:
            FullScreenWrapper2App.close_layout()
        
    def sortData(self):  
      a = textDict
      #Sort the keys by time, then name, then type
      keys = sorted(a, key=lambda k: (-a[k][2], a[k][5], a[k][6]))
      self.prepareTexts(keys)
      
    def sortContact(self):
      a = textDict
      #Sort the keys by name, address,time
      keys = sorted(a, key=lambda k: (a[k][5], a[k][0], -a[k][2]))
      self.prepareTexts(keys)
      
    def sortOpened(self):
      a = textDict
      goodKeys = []
      #Sort the keys by opened, then name, then type
      keys = sorted(a, key=lambda k: (-a[k][2], a[k][5], a[k][6]))
      for key in a:
        #Remove keys if unopened
        if(a[key][3]=='1'): goodKeys += [key]
      self.prepareTexts(goodKeys)
    
    def sortClosed(self):
      a = textDict
      goodKeys = []
      #Sort the keys by closed, then name, then type
      keys = sorted(a, key=lambda k: (-a[k][2], a[k][5], a[k][6]))
      for key in a:
        #Remove keys if unopened
        if(a[key][3]=='0'): goodKeys += [key]
      self.prepareTexts(goodKeys)
    
    #Takes a list and tells the xml list view to show the list
    def displayTexts(self,l):
        self.views.list_texts.set_listitems(l)
    
    #Takes sorted keys and prepares list of strings to display in text mode  
    def prepareTexts(self,keys):  
      a = textDict
      finalTexts = []
      for key in keys:
        #Use the global textDict created to get name, date, message
        name = a[key][5]
        date = a[key][4]
        message = a[key][1]
        finalTexts.append(str(name)+ " " + "\n" + str(date) + "\n"
                                     + str(message) + "\n")
        self.displayTexts(finalTexts)
    
    def returnContact(self,view,eventdata):
        print "text clicked on"
 
###############################################################################
    
class SendTextLayout(Layout):
    def __init__(self):
        #Create list for contacts chosen and for numbers to be sent to
        self.contacts_chosen = []
        self.numbers = []
        super(SendTextLayout,self).__init__(sendTextLayout,"PySMS")
    
    def on_show(self):
        self.views.speechToText.add_event(
            click_EventHandler(self.views.speechToText, self.textSpeech))
        self.views.checkLength.add_event(
            click_EventHandler(self.views.checkLength, self.checkLength))  
        self.views.backToTitle.add_event(
            click_EventHandler(self.views.backToTitle, self.cancel))
        self.add_event(key_EventHandler("4", self,self.cancel ))
        self.views.sendSMS.add_event(
            click_EventHandler(self.views.sendSMS, self.sendText))
        self.views.chooseContact.add_event(
            click_EventHandler(self.views.chooseContact, self.contact_chooser))
         
    def cancel(self,view,eventdata):
        FullScreenWrapper2App.close_layout()
    
    def on_close(self):
        pass
    
    #Pulls the text from the id and checks length
    def checkLength(self,view,eventData):
        text = str(self.views.edit_SMS.text)
        length = len(text)
        droid.makeToast(str(length))
        
    #Call upon the speechRecognitionFacade and set text to output
    def textSpeech(self,view,eventdata):
        result = droid.recognizeSpeech("Talk Now",None, None)
        self.views.edit_SMS.text = result[1]    
 
    def sendText(self,view,eventdata):
        #Pulls text by calling upon id of edit_SMS in xml code
        text = str(self.views.edit_SMS.text)
        #Can only send basic text of less than 160 characters
        if(len(text) > 159):
          message = "Please make sure your message is under 160 characters"
          droid.makeToast(message) 
        #Simply if statement to see if anything has been written
        elif(self.views.edit_SMS.text == "Enter_SMS_Here"):
          droid.makeToast("Please write a message")
        #Checks to make sure a number has been inserted
        elif(self.views.contact.text == "Type_Contact_Number_Here"):
	  droid.makeToast("Please select a contact")
        else:
          #Add a \n to make searching for numbers easier   
          addresses = self.views.contact.text + "\n"
          self.numbers = self.getNumbers(addresses)
          #loop through numbers and send message to each number
          for destination in self.numbers:
            droid.smsSend(destination,text)
          #Let the user know this command has been executed
          droid.makeToast("Sending Text!")
          #Close the layout (return to Title screen)
          FullScreenWrapper2App.close_layout()
    
    def contact_chooser(self,view,eventdata):
      #create string to display what contacts have been chosen
      self.final_contacts = ""
      self.display_contacts()
      #Create a pop up list dialoge box
      droid.dialogCreateAlert("Choose Contacts")
      droid.dialogSetPositiveButtonText("Ok")
      droid.dialogSetMultiChoiceItems(self.contacts_chosen)
      #Show the box
      droid.dialogShow()
      #Close the box and get selections
      droid.dialogGetResponse()
      selected = droid.dialogGetSelectedItems()[1]
      #Makes the selections presentable
      for contact in selected:
        self.final_contacts += (str(self.contacts_chosen[contact])) + "\n"
      #delte the last line break in the string to make it look better
      self.final_contacts = self.final_contacts[:len(self.final_contacts)-1]
      #set the text in the contact view box to this string of contacts
      self.views.contact.text = self.final_contacts
 
    #Goes through a strong of names, numbers, letters and pulls out numbers
    def getNumbers(self, address):
      numbers = []
      while(len(address) > 2):
        startIndex = address.index("\n")
        if(address[startIndex-1] in "0123456789"):
          #Friendly fact. Text messages take 10 length numbers!
          numbers += [address[startIndex-10:startIndex]]
          address = address[startIndex+1:]
        else:
          address = address[startIndex+1:]
      return numbers
    
    #Create a list of contacts
    def display_contacts(self):
        d = contactDictionary
        keys = sorted(d, key=lambda k: (d[k][0],d[k][1]))
        for key in keys:
            self.contacts_chosen.append(d[key][0]+"\n"+d[key][1]+" "+str(key))
 
 ##############################################################################
 
class AboutLayout(Layout):
    def __init__(self):
        super(AboutLayout,self).__init__(aboutLayout,"PySMS")
    
    #Create key handlers
    def on_show(self):
        #tell the id that its "text" element is this string
        self.views.aboutStatement.text = '''This is a basic SMS application
        created by Vivek Nangia. \n The GUI was coded in XML and the
        underworkings in python. It runs on an andoird device running android
        2.6 or higher through a scripting layer developed by Google called
        Scripting Layer for Android. The bridge between the GUI and sl4a,
        called fulscreenwrapper2 was created by Hariharan Srinath. \n
        I hope you enjoy!'''
        self.views.backToTitle.add_event(click_EventHandler
                                         (self.views.backToTitle, self.cancel))
        self.add_event(key_EventHandler("4", self,self.cancel ))
    
    def cancel(self,view,eventdata):
        FullScreenWrapper2App.close_layout()
    
    def on_close(self):
        pass
 
############################################################################### 
class TitleLayout(Layout):
    def __init__(self):
        super(TitleLayout,self).__init__(titleLayout,"PySMS")
    
    #Event Handlers that search for specific event,either touch or button event    
    def on_show(self):
        self.add_event(key_EventHandler(handler_function=self.close_app))
        self.views.closeButton.add_event(
            click_EventHandler(self.views.closeButton, self.close_app))
        self.views.aboutButton.add_event(
            click_EventHandler(self.views.aboutButton,self.about_layout))
        self.views.sendTextButton.add_event(
            click_EventHandler(self.views.sendTextButton,self.sms_layout)) 
        self.views.viewTextButton.add_event(
            click_EventHandler(self.views.viewTextButton,self.viewText_layout))
        
    def on_close(self):
        pass
    
    #Functions that open new layouts
    def close_app(self,view,event):
        FullScreenWrapper2App.exit_FullScreenWrapper2App()
 
    def about_layout(self,view,eventdata):
        FullScreenWrapper2App.show_layout(AboutLayout())
        
    def sms_layout(self,view,eventdata):
        FullScreenWrapper2App.show_layout(SendTextLayout())
    
    def viewText_layout(self,view,eventdata):
        FullScreenWrapper2App.show_layout(ViewTextLayout())
 
#############################################################################
 
if __name__ == '__main__':
    #Start and initialize sl4a droid class
    droid = android.Android()
    random.seed()
    FullScreenWrapper2App.initialize(droid)
    
    #Create and show spinner. Allows for dictionaries to load
    droid.dialogCreateSpinnerProgress("Please wait while application loads.")
    droid.dialogShow()
    
    #Andoird stores time as seconds from the year. Use built in functions
    #to convert to normal date time
    def getDate(time):
        millis = int(time)/1000
        strtime = datetime.datetime.fromtimestamp(millis)
        date = strtime.strftime("%m/%d/%y %H:%M:%S")
        return date
    
    #Match number with dictionary, if not in there, return unknow contact
    def getName(number):
        num = str(number)    
        try: return [contactDictionary[num][0],contactDictionary[num][1]]
        except: return "Unknown:","Unknown"  
    
    #Create a dictionary before app opens (for speed purposes) that links a
    #persons number to their name and type of phone number
    contactDictionary = dict()
    #Call on the contacts facade and wish to desire only contact information
    #of display_name, data1(number) and data2(type of number(cell,work,etc))
    allContacts = droid.queryContent(
        'content://com.android.contacts/data/phones',\
        ['display_name','data1','data2'],None,None,None).result
    for c in allContacts:
      #Take the integer repersentation of data2 and use it to define what type
      #of number
      type = "Other:"
      if(int(c['data2'])==1): type = 'Home:'
      elif(int(c['data2'])==2): type = 'Cell:'
      elif(int(c['data2'])==3): type = 'Work:'
      contactData = []
      contactData += [c['display_name']] + [type]
      #Add entry to dictionary
      contactDictionary[c['data1']] = contactData
    
    #Create a dictionary where the key is the text id, and the list holds
    #information on the  address,body,time,open/unopen,
    #date, name, type(cell, work, etc)   
    textDict = dict()
    messages= droid.smsGetMessageIds(0)[1]
    for ids in messages:
        info = []
        message = droid.smsGetMessageById(ids)
        id = message[0]
        #These are stored as unicode. Convert to string and choose to ignore
        #(remove) parts that are unicode and convert the rest to ascii string
        address = message[1]['address'].encode('ascii','ignore')
        time = message[1]['date'].encode('ascii','ignore')
        body = message[1]['body'].encode('ascii','ignore')
        date = getDate(time)
        name,type = getName(address)
        info += [address] + [body] + [int(time)] + [message[1]['read']]
        info += [date] + [name] + [type]
        textDict[id] = info
    
    #Dismiss the spinning dialog
    droid.dialogDismiss()
    
    #Calls upon the first layout: title layout
    FullScreenWrapper2App.show_layout(TitleLayout())
    FullScreenWrapper2App.eventloop()
    
