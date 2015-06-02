from PySide.QtCore import *
from PySide.QtGui import *
import sys
import random
import reset
import submit
import about
from ui_files import showMainGui


class Main(QMainWindow, showMainGui.Ui_mainWindow):

    # create a dictionary with states and capitals
    capitals = {
        'Alabama': 'Montgomery',
        'Alaska': 'Juneau',
        'Arizona': 'Phoenix',
        'Arkansas': 'Little Rock',
        'California': 'Sacramento',
        'Colorado': 'Denver',
        'Connecticut': 'Hartford',
        'Delaware': 'Dover',
        'Florida': 'Tallahassee',
        'Georgia': 'Atlanta',
        'Hawaii': 'Honolulu',
        'Idaho': 'Boise',
        'Illinois': 'Springfield',
        'Indiana': 'Indianapolis',
        'Iowa': 'Des Moines',
        'Kansas': 'Topeka',
        'Kentucky': 'Frankfort',
        'Louisiana': 'Baton Rouge',
        'Maine': 'Augusta',
        'Maryland': 'Annapolis',
        'Massachusetts': 'Boston',
        'Michigan': 'Lansing',
        'Minnesota': 'Saint Paul',
        'Mississippi': 'Jackson',
        'Missouri': 'Jefferson City',
        'Montana': 'Helena',
        'Nebraska': 'Lincoln',
        'Nevada': 'Carson City',
        'New Hampshire': 'Concord',
        'New Jersey': 'Trenton',
        'New Mexico': 'Santa Fe',
        'New York': 'Albany',
        'North Carolina': 'Raleigh',
        'North Dakota': 'Bismark',
        'Ohio': 'Columbus',
        'Oklahoma': 'Oklahoma City',
        'Oregon': 'Salem',
        'Pennsylvania': 'Harrisburg',
        'Rhode Island': 'Providence',
        'South Carolina': 'Columbia',
        'South Dakota': 'Pierre',
        'Tennessee': 'Nashville',
        'Texas': 'Austin',
        'Utah': 'Salt Lake City',
        'Vermont': 'Montpelier',
        'Virginia': 'Richmond',
        'Washington': 'Olympia',
        'West Virginia': 'Charleston',
        'Wisconsin': 'Madison',
        'Wyoming': 'Cheyenne'
    }

# create a dictionary with number and states
    states = {
        1:'Alabama',
        2:'Alaska',
        3:'Arizona',
        4:'Arkansas',
        5:'California',
        6:'Colorado',
        7:'Connecticut',
        8:'Delaware',
        9:'Florida',
        10:'Georgia',
        11:'Hawaii',
        12:'Idaho',
        13:'Illinois',
        14:'Indiana',
        15:'Iowa',
        16:'Kansas',
        17:'Kentucky',
        18:'Louisiana',
        19:'Maine',
        20:'Maryland',
        21:'Massachusetts',
        22:'Michigan',
        23:'Minnesota',
        24:'Mississippi',
        25:'Missouri',
        26:'Montana',
        27:'Nebraska',
        28:'Nevada',
        29:'New Hampshire',
        30:'New Jersey',
        31:'New Mexico',
        32:'New York',
        33:'North Carolina',
        34:'North Dakota',
        35:'Ohio',
        36:'Oklahoma',
        37:'Oregon',
        38:'Pennsylvania',
        39:'Rhode Island',
        40:'South Carolina',
        41:'South Dakota',
        42:'Tennessee',
        43:'Texas',
        44:'Utah',
        45:'Vermont',
        46:'Virginia',
        47:'Washington',
        48:'West Virginia',
        49:'Wisconsin',
        50:'Wyoming',
    }

    # list for Capitals in A
    As = []

    # list for Capitals in B

    Bs = []

    # list for Capitals in C
    Cs = []

    # list for Capitals in D
    Ds = []

    # list for Capitals in E
    Es = []

    # list for correct answers
    corrAnswer = []

    # list for users answers
    userAnswer = ['z', 'z', 'z', 'z', 'z', 'z', 'z', 'z', 'z', 'z']

    # list for users capitals
    userCaps = ['z', 'z', 'z', 'z', 'z', 'z', 'z', 'z', 'z', 'z']

    # get 10 random states
    tenstates = random.sample(states.values(), 10)

    # global counter
    x = 0

    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)

        self.actionNew.triggered.connect(self.newApp)
        self.actionExit.triggered.connect(self.exitApp)
        self.actionAbout.triggered.connect(self.aboutApp)
        self.btnNext.clicked.connect(self.nxtButton)
        self.btnPrev.clicked.connect(self.prevButton)
        self.rbAnswerOne.clicked.connect(self.radioButtonClicked)
        self.rbAnswerTwo.clicked.connect(self.radioButtonClicked)
        self.rbAnswerThree.clicked.connect(self.radioButtonClicked)
        self.rbAnswerFour.clicked.connect(self.radioButtonClicked)
        self.rbAnswerFive.clicked.connect(self.radioButtonClicked)
        self.btnSubmit.clicked.connect(self.clickSubmit)
        self.btnReset.clicked.connect(self.clickReset)


        self.rbNone.setVisible(False)

        # load initial data
        self.load_initial_settings()

    def load_initial_settings(self):
        """Loads the initial settings for the application"""

        self.btnSubmit.setEnabled(False)

        # place the 10 random state with other random states
        for state in self.tenstates:
            placeNumber = random.randint(0, 4)
            selState = state
            listState = []
            for i in range(0, 5):
                while selState == state: # will loop if the state was already picked
                    ranNumber = random.randint(1, 50)
                    selState = self.states[ranNumber]
                    # check to see if state has been picked before
                    if selState in listState:
                        selState = state
                    else:
                        listState.append(selState)
                # place the selected capital in the random place number
                if i == 0:
                    if i == placeNumber:
                        self.corrAnswer.append('a')
                        self.As.append(self.capitals[state])
                    else:
                        self.As.append(self.capitals[selState])
                elif i == 1:
                    if i == placeNumber:
                        self.corrAnswer.append('b')
                        self.Bs.append(self.capitals[state])
                    else:
                        self.Bs.append(self.capitals[selState])
                elif i == 2:
                    if i == placeNumber:
                        self.corrAnswer.append('c')
                        self.Cs.append(self.capitals[state])
                    else:
                        self.Cs.append(self.capitals[selState])
                elif i == 3:
                    if i == placeNumber:
                        self.corrAnswer.append('d')
                        self.Ds.append(self.capitals[state])
                    else:
                        self.Ds.append(self.capitals[selState])
                elif i == 4:
                    if i == placeNumber:
                        self.corrAnswer.append('e')
                        self.Es.append(self.capitals[state])
                    else:
                        self.Es.append(self.capitals[selState])
                selState = state

        self.nxtButton()

    def exitApp(self):
        self.close()

    def newApp(self):
        del self.corrAnswer[:]
        del self.As[:]
        del self.Bs[:]
        del self.Cs[:]
        del self.Ds[:]
        del self.Es[:]
        del self.userAnswer[:]
        self.userAnswer = ['z', 'z', 'z', 'z', 'z', 'z', 'z', 'z', 'z', 'z']
        del self.userCaps[:]
        self.userCaps = ['z', 'z', 'z', 'z', 'z', 'z', 'z', 'z', 'z', 'z']
        self.tenstates = random.sample(self.states.values(), 10)
        self.load_initial_settings()
        self.startOver()
        self.btnSubmit.setEnabled(False)

    def aboutApp(self):
        strAbout = "Copyright 2015 - Orlando Viera \n\n"
        strAbout = strAbout + "email: orlando.g.viera@gmail.com \n\n"
        strAbout = strAbout + "This program is free software: you can redistribute it and/or modify \n"
        strAbout = strAbout + "it under the terms of the GNU General Public License as published by \n"
        strAbout = strAbout + "the Free Software Foundation, either version 3 of the License, or \n"
        strAbout = strAbout + "(at your option) any later version. \n\n"
        strAbout = strAbout + "This program is distributed in the hope that it will be useful, \n"
        strAbout = strAbout + "but WITHOUT ANY WARRANTY; without even the implied warranty of \n"
        strAbout = strAbout + "MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. \n\n"
        strAbout = strAbout + "See the GNU General Public License for more details: http://www.gnu.org/licenses/gpl.txt"
        dlg = about.About(self, strAbout)
        dlg.exec_()

    def nxtButton(self):
        txtCounterLabel = self.lblCounter.text()
        i = txtCounterLabel.find("of")
        txtnumber = txtCounterLabel[:i]
        if int(txtnumber) < 10:
            j = int(txtnumber)+1
            self.lblQuestion.setText("What's the capital " + self.tenstates[j-1] + " ?")
            txtNewString = txtCounterLabel.replace(txtnumber.strip(), str(j), 1)
            self.lblCounter.setText(txtNewString)
            self.rbAnswerOne.setText("A) " + self.As[j-1])
            self.rbAnswerTwo.setText("B) " + self.Bs[j-1])
            self.rbAnswerThree.setText("C) " + self.Cs[j-1])
            self.rbAnswerFour.setText("D) " + self.Ds[j-1])
            self.rbAnswerFive.setText("E) " + self.Es[j-1])

            if len(self.userAnswer) > 0:
                #print "something has been selected before"
                if self.userAnswer[j-1] == "a":
                    self.rbAnswerOne.toggle()
                elif self.userAnswer[j-1] == "b":
                    self.rbAnswerTwo.toggle()
                elif self.userAnswer[j-1] == "c":
                    self.rbAnswerThree.toggle()
                elif self.userAnswer[j-1] == "d":
                    self.rbAnswerFour.toggle()
                elif self.userAnswer[j-1] == "e":
                    self.rbAnswerFive.toggle()
                else:
                    self.rbNone.toggle()

            self.x = j-1   # to let the rest of the app know what question it is on
        self.checkIfAllAnswered()


    def prevButton(self):
        txtCounterLabel = self.lblCounter.text()
        i = txtCounterLabel.find("of")
        txtnumber = txtCounterLabel[:i]
        if int(txtnumber) > 1:
            j = int(txtnumber)-1
            self.lblQuestion.setText("What's the capital " + self.tenstates[j-1] + " ?")
            txtNewString = txtCounterLabel.replace(txtnumber.strip(), str(j), 1)
            self.lblCounter.setText(txtNewString)
            self.rbAnswerOne.setText("A) " + self.As[j-1])
            self.rbAnswerTwo.setText("B) " + self.Bs[j-1])
            self.rbAnswerThree.setText("C) " + self.Cs[j-1])
            self.rbAnswerFour.setText("D) " + self.Ds[j-1])
            self.rbAnswerFive.setText("E) " + self.Es[j-1])

            if len(self.userAnswer) > 0:
                # print "something has been selected before"
                if self.userAnswer[j-1] == "a":
                    self.rbAnswerOne.toggle()
                elif self.userAnswer[j-1] == "b":
                    self.rbAnswerTwo.toggle()
                elif self.userAnswer[j-1] == "c":
                    self.rbAnswerThree.toggle()
                elif self.userAnswer[j-1] == "d":
                    self.rbAnswerFour.toggle()
                elif self.userAnswer[j-1] == "e":
                    self.rbAnswerFive.toggle()
                else:
                    self.rbNone.toggle()

            self.x = j-1   # to let the rest of the app know what question it is on
        self.checkIfAllAnswered()

    def radioButtonClicked(self):
        if self.rbAnswerOne.isChecked():
            self.userAnswer[self.x] = 'a'
            self.userCaps[self.x] = self.As[self.x]
        elif self.rbAnswerTwo.isChecked():
            self.userAnswer[self.x] = 'b'
            self.userCaps[self.x] = self.Bs[self.x]
        elif self.rbAnswerThree.isChecked():
            self.userAnswer[self.x] = 'c'
            self.userCaps[self.x] = self.Cs[self.x]
        elif self.rbAnswerFour.isChecked():
            self.userAnswer[self.x] = 'd'
            self.userCaps[self.x] = self.Ds[self.x]
        elif self.rbAnswerFive.isChecked():
            self.userAnswer[self.x] = 'e'
            self.userCaps[self.x] = self.Es[self.x]
        else:
            pass
        self.checkIfAllAnswered()

    def clickSubmit(self):
        results = ""
        intright = 0
        for s in range(0, 10):
            if self.userAnswer[s] == self.corrAnswer[s]:
                intright += 1
            else:
                results = results + "The capital of " + self.tenstates[s] + " is " + self.capitals[self.tenstates[s]]
                results = results + ". You selected " + self.userCaps[s] + ". \n"
        results = "You answered " + str(intright) + " out 10 correctly. \n" + results
        dlg = submit.Submit(self, results)
        dlg.exec_()

    def clickReset(self):
        dlg = reset.Reset(self)
        sig = dlg.pButton
        sig.connect(self.ResetSaid)
        dlg.exec_()

    def ResetSaid(self, param):
        if param == 1:
            del self.userAnswer[:]
            self.userAnswer = ['z', 'z', 'z', 'z', 'z', 'z', 'z', 'z', 'z', 'z']
            del self.userCaps[:]
            self.userCaps = ['z', 'z', 'z', 'z', 'z', 'z', 'z', 'z', 'z', 'z']
            self.startOver()
            self.btnSubmit.setEnabled(False)

    def startOver(self):
        self.lblCounter.setText("1 of 10")
        self.x = 0
        self.lblQuestion.setText("What's the capital " + self.tenstates[0] + " ?")
        self.rbAnswerOne.setText("A) " + self.As[0])
        self.rbAnswerTwo.setText("B) " + self.Bs[0])
        self.rbAnswerThree.setText("C) " + self.Cs[0])
        self.rbAnswerFour.setText("D) " + self.Ds[0])
        self.rbAnswerFive.setText("E) " + self.Es[0])
        self.rbNone.toggle()


    def checkIfAllAnswered(self):
        cntAnswers = 0
        anyz = 0
        for answer in self.userAnswer:
            cntAnswers += 1
            if answer == 'z':
                anyz = 1
        if cntAnswers > 9 and anyz == 0:
            self.btnSubmit.setEnabled(True)
        else:
            #pass
            self.btnSubmit.setEnabled(False)

app = QApplication(sys.argv)
form = Main()
form.show()
app.exec_()