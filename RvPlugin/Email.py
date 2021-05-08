#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import smtplib
from email.mime.text      import MIMEText
from email.header         import Header
from email.mime.image     import MIMEImage
from email.mime.multipart import MIMEMultipart


class SendEmail():
    G_Is_Connect = False
    G_Is_Login   = False
    def Connect( self, ServerIp="192.168.1.183", ServerPort=25 ):
        try:
            self.G_Server_Ip   = ServerIp
            self.G_Server_Port = ServerPort
            self.G_SMTP        = smtplib.SMTP() 
            self.G_SMTP.connect( self.G_Server_Ip, self.G_Server_Port )
            self.G_Is_Connect  = True
            return True
        except Exception,e:
            self.G_Is_Connect  = False
            return False
    def Login( self, Account, Password="123" ):
        try:
            if self.G_Is_Connect:
                self.G_Account  = Account
                self.G_Password = Password
                self.G_SMTP.login( self.G_Account, self.G_Password )  
                self.G_Is_Login = True
                return True
            else:
                return False
        except Exception,e:
            self.G_Is_Login = False
            return False   
    def SendEmail( self, Receivers, Title, Details, Type="plain", Attachments=[], Images=[] ):
        if self.G_Is_Connect and self.G_Is_Login:
            try:
                Message = MIMEMultipart()
                Message['Subject'] = Header( Title, 'utf-8' )        
                #内容
                Message.attach( MIMEText( Details, Type, 'utf-8' ) )
                #附件
                for Attachment in Attachments:
                    AttachmentObj = MIMEText( open(Attachment, 'rb').read(), 'base64', 'utf-8')
                    AttachmentObj["Content-Type"] = 'application/octet-stream'
                    AttachmentObj["Content-Disposition"] = 'attachment; filename="%s"'%( os.path.basename(Attachment) )
                    Message.attach( AttachmentObj )    
                #图片
                for Image in Images:
                    ImageObj = open( Image["File"], 'rb' )
                    EmailImage = MIMEImage( ImageObj.read() )
                    ImageObj.close()            
                    EmailImage.add_header( 'Content-ID', Image["ID"] )
                    Message.attach( EmailImage )
                #接收,发送
                for Receiver in Receivers:
                    Message['From']    = Header( self.G_Account , 'utf-8')
                    Message['To']      = Header( Receiver, 'utf-8' )
                    Message['Subject'] = Header( Title, 'utf-8')    
                    self.G_SMTP.sendmail( self.G_Account, Receiver, Message.as_string() )     
            except Exception,e:
                print e
                return False
        else:
            return False


def send(html, title, sender, recevier):

    # Html = """
    #      <p>Python 邮件发送测试...</p>
    #      <p><a href="file:///N:/sound">这是一个超链接</a></p>
    #      <p>图片演示：</p>
    #      <p><img src="cid:image1"></p>
    #      """
    Email = SendEmail()
    Email.Connect()
    Email.Login(sender)
    # Email.SendEmail( ['zhangtianshun@ccc.net'], u"测试邮件2", Html, "html", Attachments=[r"C:\Users\wangchenfei\Desktop\test\nz_e_130001grass001_tex.jpg"],Images=[ {"File":r"C:\Users\wangchenfei\Desktop\test\nz_e_130001grass001_tex.jpg","ID":"<image1>"} ] )
    recevier.append( sender )
    Email.SendEmail( recevier, title, html, "html", Attachments=[], Images=[])