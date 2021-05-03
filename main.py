import os
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton
from kivymd.uix.textfield import MDTextField
from datetime import datetime

from android.permissions import request_permissions, Permission
request_permissions([Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE])



kv2 = """

Screen:
    BoxLayout:
        id:box
        orientation: 'vertical'

        MDToolbar:
            title: "Rental Managment App"
            left_action_items: [["menu", lambda x: nav_draw.set_state()]]
        
              
        Widget:
    NavigationLayout: 
        id: navigation   
        ScreenManager:
            id: screen_manager
            Screen: 
                name: "scr4" 
                MDLabel: 
                    text: " WELCOME TO RENTAL AND PROPERTY MANAGEMENT SYSTEM APP HOW TO USE THE APP-  "
                    pos_hint:{"center_x":0.5,"center_y":0.75}
                MDLabel:
                    text: "   1, IF YOU'RE THE MANAGER OR A WORKER OF THE ESTABLISHMENT CHOOSE THE *realtor* OPTION FROM TOOL BAR"
                    pos_hint:{"center_x":0.5,"center_y":0.63}
                    width:50
                MDLabel:
                    text: "   2, IF YOU'RE A CUSTOMER USE THE *customer* OPTION FROM THE TOOL BAR"
                    pos_hint:{"center_x":0.5,"center_y":0.47}
                MDLabel:
                    text: "   3, IF YOU WANT TO KNOW ABOUT THE CREATORS OR HAVE QUESTIONS CH0OSE THE *info* OPTION FROM TOOL BAR"
                    pos_hint:{"center_x":0.5,"center_y":0.28}
                    width:50
            Screen:
                
                name: "scr1"    
                MDLabel:
                    text: ""
                    halign: "center"
                MDRectangleFlatButton:
                    text: 'NEW DOCUMENT'
                    pos_hint:{"center_x":0.5,"center_y":0.7}
                    size_hint:(1,0.1)
                    on_press:
                        app.name()  
                MDRectangleFlatButton:
                    text: 'RENTAL AGE'
                    pos_hint:{"center_x":0.5,"center_y":0.3}
                    size_hint:(1,0.1)
                    on_press:
                        app.RENTAGE()  
                MDRectangleFlatButton:
                    text: 'DOCUMENTATION'
                    pos_hint:{"center_x":0.5,"center_y":0.5}
                    size_hint:(1,0.1)
                    on_press:
                        app.DOCUMENT()  
            Screen:
                name: "scr2"
                MDLabel:
                    text: "work still in progress"
                    halign: "center"
                MDRectangleFlatButton:
                    text:"DEVS"
                    pos_hint:{"center_x":0.5, "center_y":0.3} 
                    on_press:
                        app.info()
                        
            Screen:
                name: "scr3"
                MDLabel:
                    text: "on development"
                    halign: "center"
                      

        MDNavigationDrawer:
            id: nav_draw
            orientation: "vertical"
            padding: "8dp"
            spacing: "8dp"

            AnchorLayout:
                anchor_x: "left"
                size_hint_y: None
                height: avatar.height

                Image:
                    id: avatar
                    size_hint: None, None
                    size: "56dp", "56dp"
                    source: "./icon.png"

            MDLabel:
                text: "USER INTERFERENCE"
                font_style: "Button"
                size_hint_y: None
                height: self.texture_size[1]

            MDLabel:
                text: "project 01"
                font_style: "Caption"
                size_hint_y: None
                height: self.texture_size[1]

            ScrollView:
                MDList:
                    OneLineAvatarListItem:
                        on_press:
                            nav_draw.set_state("close")
                            screen_manager.current = "scr4"
                            
                        text: "HOME"
                        IconLeftWidget:
                            icon: 'home'
                
                    OneLineAvatarListItem:
                        on_press:
                            nav_draw.set_state("close")
                            screen_manager.current = "scr1"
                            
                        text: "realtor"
                        IconLeftWidget:
                            icon: "information"
                            
                    OneLineAvatarListItem:
                        on_press:
                            nav_draw.set_state("close")
                            screen_manager.current = "scr3"
                            
                        text: "customer"
                        IconLeftWidget:
                            icon: 'information'
                            
                    OneLineAvatarListItem:
                        on_press:
                            nav_draw.set_state("close")
                            screen_manager.current = "scr2"
                            
                        text: "About"
                        IconLeftWidget:
                            icon: 'information'

            Widget:
"""


class Main(MDApp):

    def build(self):
        self.front = Builder.load_string(kv2)
        return self.front



    # NEW RENTER'S FILES CREATOR

    def name(self):
        self.channelx = MDDialog(title="NEW RENTERS", text="Name", size_hint=(0.8, 1),
                                 buttons=[MDFlatButton(text='Close', on_release=self.close1),
                                          MDFlatButton(text='next', on_release=self.location1)]
                                 )
        self.z = MDTextField(text="", size_hint=(0.4, 0.4))
        self.channelx.add_widget(self.z)
        self.channelx.open()

    def location1(self, obj):
        self.loc = MDDialog(title="NEW RENTERS", text="Location", size_hint=(0.8, 1),
                            buttons=[MDFlatButton(text='Close', on_release=self.close11),
                                     MDFlatButton(text='Next', on_release=self.date)])
        self.inputlocation = MDTextField(text="", size_hint=(0.4, 0.4))
        self.loc.add_widget(self.inputlocation)
        self.loc.open()

    def date(self, obj):
        self.datei = MDDialog(title="NEW RENTERS", text="Date", size_hint=(0.8, 1),
                              buttons=[MDFlatButton(text='Close', on_release=self.close9),
                                       MDFlatButton(text='proceed', on_release=self.base)])
        self.inputdate = MDTextField(text="", size_hint=(0.4, 0.4))
        self.datei.add_widget(self.inputdate)
        self.datei.open()

    def base(self, obj):
        self.basec = MDDialog(title="NEW RENTERS", text="Proposed Payment base", size_hint=(0.8, 1),
                              buttons=[MDFlatButton(text='Close', on_release=self.close10),
                                       MDFlatButton(text='create', on_release=self.launch)])
        self.proposedbase = MDTextField(text="", size_hint=(0.4, 0.4))
        self.basec.add_widget(self.proposedbase)
        self.basec.open()

    def launch(self, obj):
        self.filePath ="/storage/emulated/0/appdocs/file "

        self.filep = self.filePath+str(self.z.text) + " .doc"
        self.filea = self.filePath+str(self.z.text) + " 1.doc"

        try:
            os.mkdir(self.filePath)
        except:
            print("a")

        log = open(self.filep,"w+")
        log.write(self.z.text)
        log.write("\n")
        log.write(self.inputlocation.text)
        log.write("\n")
        log.write(self.inputdate.text)
        log.write("\n")
        log.write(self.proposedbase.text)
        self.words = log.read()
        filea = open(self.filea, "w+")
        filea.write("NAME: " + self.z.text)
        filea.write("\n")
        filea.write("LOCATION: " + self.inputlocation.text)
        filea.write("\n")
        filea.write("DATE: " + self.inputdate.text)
        filea.write("\n")
        filea.write("YEALY PAYMENT: " + self.proposedbase.text)
        self.datei.dismiss()
        self.basec.dismiss()
        self.loc.dismiss()
        self.channelx.dismiss()

    # DOCUMENTATION FINDER

    def DOCUMENT(self):

        self.channely = MDDialog(title="DOCUMENTATION", text="Name", size_hint=(0.8, 1),
                                 buttons=[MDFlatButton(text='Close', on_release=self.close2),
                                          MDFlatButton(text='find', on_release=self.find1)])
        self.name = MDTextField(text="", size_hint=(0.4, 0.4))
        self.channely.add_widget(self.name)
        self.channely.open()

    def find1(self, obj):
        self.doc = self.name.text + " 1.doc"
        self.file = open(self.filePath+self.doc)
        self.read = self.file.read()
        self.x = MDDialog(text=self.read)
        self.x.open()

    # END
    # RENTAL CALCULATOR

    def RENTAGE(self):
        self.channelz = MDDialog(title="RENTAL AGE", text="Name", size_hint=(0.8, 1),
                                 buttons=[MDFlatButton(text='Close', on_release=self.close3),
                                          MDFlatButton(text='next', on_release=self.calc)])

        self.input = MDTextField(text="", size_hint=(0.4, 0.4))
        self.channelz.add_widget(self.input)
        self.channelz.open()

    def calc(self, obj):
        self.vv = self.input.text+" .doc"
        self.file = open(self.filePath+self.vv)
        self.read = self.file.readlines()

        self.yx = self.read[2]
        self.dx = self.yx.split("/")
        self.dx = list(map(int, self.dx))
        self.year = self.dx[2]
        self.month = self.dx[1]
        self.day = self.dx[0]
        self.d2 = datetime.now()

        self.d1 = datetime(self.year, self.month, self.day)
        self.d2 = datetime(self.d2.year, self.d2.month, self.d2.day)
        self.days = abs((self.d1 - self.d2).days)
        self.reminder = self.days % 30
        self.months = (self.days - self.reminder) / 30
        self.reminder2 = int(self.months % 12)
        self.years = int((self.months - self.reminder2) / 12)
        self.datey = str(self.years) + " years/" + str(self.reminder2) + " Months/" + str(self.reminder) + " Days"

        self.show = MDDialog(title="Rented for",size_hint=(0.8,1), text=self.datey)
        self.but = MDFlatButton(text="NEXT", on_press=self.calc3)
        self.show.add_widget(self.but)
        self.show.open()
        self.remaindera = int(self.years) % 5
        self.readx = int(self.dx[2])
        self.Monthly_base = "${:,}".format(self.readx)
        self.payment_time = ((self.years * 12) + self.reminder2) * self.readx
        self.baseTime = "12 months"
        
    def calc3(self, obj):
        self.g = self.baseTime
        self.x = self.g.split(" ")
        self.baseTime = self.x[0]

        if self.x[1] != "":
            self.baseTime = int(self.x[0])
            if self.x[1] == 'year' or self.x[1] == 'years':
                self.baseTime = self.baseTime * 12
            elif self.x[1] == "month" or self.x[1] == 'months':
                self.baseTime = self.baseTime
            else:
                self.error = MDDialog(text="please enter date type correctly")
                self.error.open()
            self.xprint = MDDialog(text="-------------PAYMENTS ARE CALCULATED PER " + str(self.g)
                                        + " -----------\n"
                                        + "\n THE CURRENT SET BASE OF THE PAYMENT PER MONTH IS: "
                                        + str(self.Monthly_base),
                                   buttons=[MDFlatButton(text='Close', on_release=self.close7),
                                            MDFlatButton(text='click', on_release=self.calc4)])
            self.xprint.open()
        else:
            self.error = MDDialog(text="please enter date number correctly")
            self.error.open()

    def calc4(self, obj):
    
        if self.remaindera != 0:
            self.payment_time2 = ((self.years - self.remaindera) * 12) * self.readx
            self.payment2 = "${:,}".format(self.payment_time2)
            self.z = ("Total paid in exception of coming pay date: ", self.payment2)
            self.bad_print = MDDialog(text="\n///Payment day hasn't been reached yet ///\n")
            
            self.bad_print.open()
            self.ddialog.dismiss()
            self.show.dismiss()
            self.xprint.dismiss()
        else:
            self.Divided_payment = self.payment_time / 12 * self.baseTime
            self.payment = "${:,}".format(self.Divided_payment)
            self.read = self.read[3]
            self.print = MDDialog(text=("\nCurrent Payment: " + str(self.payment) + "\n" + self.read))
            self.ddialog.dismiss()
            self.show.dismiss()
            self.print.open()

    def info(self):
        self.inffo = MDDialog(title="DEVELOPERS", text="Names:\n EYOEL ABEBAW\n MOHAMMEDAMIN SULTAN \n TESNIM SELAHADIN",
                              size_hint=(0.8, 1), buttons=[MDFlatButton(text="close", on_release=self.close4),
                                                           MDFlatButton(text='contribute', on_release=self.close4)])
        self.inffo.open()

    # END
    # CLOSE FUNCTIONS
    def close1(self, obj):
        self.channelx.dismiss()

    def close2(self, obj):
        self.channely.dismiss()

    def close3(self, obj):
        self.channelz.dismiss()

    def close4(self, obj):
        self.inffo.dismiss()

    def close6(self, obj):
        self.show.dismiss()

    def close7(self, obj):
        self.xprint.dismiss()

    def close8(self, obj):
        self.ddialog.dismiss()

    def close9(self, obj):
        self.datei.dismiss()

    def close10(self, obj):
        self.basec.dismiss()

    def close11(self, obj):
        self.loc.dismiss()


Main().run()
