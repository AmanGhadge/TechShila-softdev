from __future__ import print_function
import grpc
import os
import subprocess
# import the generated classes
import comProto_pb2_grpc as comProto_pb2_grpc
import comProto_pb2 as comProto_pb2

import remoteFunctions
import server
import sys
from PyQt5.QtWidgets import (QMessageBox,QGridLayout,QLabel,QLineEdit,QPushButton,QApplication,QWidget)

class ConnectionForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Connection Form')
        self.resize(400,120)
        layout=QGridLayout()
        label_id=QLabel('<font size="4"> ID </font>')
        self.id=QLineEdit()
        self.id.setPlaceholderText('Enter the ID')
        layout.addWidget(label_id,0,0)
        layout.addWidget(self.id,0,1)
        label_passcode=QLabel('<font size="4"> Passcode </font>')
        self.passcode=QLineEdit()
        self.passcode.setPlaceholderText('Enter the passcode')
        layout.addWidget(label_passcode,1,0)
        layout.addWidget(self.passcode,1,1)
        global idd
        global password
        self.button=QPushButton('Submit')
        self.button.clicked.connect(self.run)
        layout.addWidget(self.button,2,0,1,2)
        layout.setRowMinimumHeight(2,75)
        self.setLayout(layout)
            
    
    def run(self):
        idd=self.id.text()
        password=self.passcode.text()
        password=server.hashPass(password)
        msg=QMessageBox()
        b=remoteFunctions.checkUser(idd,password)
        if b==[]:
            remoteFunctions.newUser(idd,password)
            msg.setText('Wrong ID or password, new data saved')
            msg.exec_()
            app.startingUp()
        else:
            msg.setText('Success')
            msg.exec_()
            with grpc.insecure_channel('localhost:50051') as channel:
                # Getting commands
                stub=comProto_pb2_grpc.getCommandsServiceStub(channel)
                command=comProto_pb2.commandMessage(id=idd,passcode=password,uidLatest='23')
                commands=stub.getCommands(command)      
                for commandss in commands:
                    print(commandss)
                    r=comResponse(commandss.one)
                    stub=comProto_pb2_grpc.sendResponseStub(channel)
                    response=comProto_pb2.latestCommand(id=idd,passcode=password,command=commandss.one,response=r,uid=commandss.five)
                    responses=stub.setCommandResponse(response)
                    print(responses)

# executing the command and sending its response back
def comResponse(com):
    pipe=subprocess.Popen(com,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True)
    res=pipe.communicate()
    if(res[1]==''):
        return res[0]
    else:
        str=res[1].replace("\n","")
        s=str.replace("'","")
        return s
                
if __name__=='__main__':
    app=QApplication(sys.argv)
    form=ConnectionForm()
    form.show()
    sys.exit(app.exec_())
    
    
        
        