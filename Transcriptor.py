# -*- coding: utf-8 -*-
from PyQt5.QtGui     import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore    import *
from gui import *

import speech_recognition as sr
import random
import sys
import csv
import os

class MyWin(QtWidgets.QMainWindow):
	def __init__(self, parent=None):
		QtWidgets.QWidget.__init__(self, parent)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

		# Buttons
		self.ui.Speeker1Button.clicked.connect(self.SpeekerOneFunction)
		self.ui.Speeker2Button.clicked.connect(self.SpeekerTwoFunction)
		self.ui.Speeker2Button.setEnabled(False)

		self.ui.ApplayButton.clicked.connect(self.ApplayFunction)

		# Variable
		self.TopicValue = ""
		self.LanguageValue = "en-EN"
		self.TempTranscription = ""
		self.TranscriptFilePath = 'C:\\Users\\Public\\Documents\\Transcriptor'

	# Collect all input parameters
	def ApplayFunction(self):
		self.TopicValue = self.ui.TopicLineEdit.text()
		self.LanguageValue = self.ui.LanguageLineEdit.text()

	def TranscriptionWriter(self, transcript):
		if not os.path.exists(self.TranscriptFilePath):
			os.makedirs(self.TranscriptFilePath)

		with open(self.TranscriptFilePath+"\\transcript.csv", mode="a+", newline="", encoding="utf-8") as f:
			write_csv = csv.writer(f)
			write_csv.writerow([self.TopicValue, transcript])

	# Speech to text
	def stt(self):
		r = sr.Recognizer()
		correct = 0
		while correct==0:
			with sr.Microphone() as source:
				audio_text = r.listen(source)
				try:
					self.TempTranscription = r.recognize_google(audio_text, language= self.LanguageValue)
					self.ui.StatusLabel.setText('Successful')
					QApplication.processEvents()
					correct = 1
				 
				except:
					 self.ui.StatusLabel.setText(random.choice(["Sorry... try again", "Please, try again", "Try again"]))
					 QApplication.processEvents()
					 self.TempTranscription = ""
					 correct = 0
		self.TranscriptionWriter(self.TempTranscription)

	def SpeekerOneFunction(self):
		self.ui.StatusLabel.setText('Talk...')
		QApplication.processEvents()
		self.ui.Speeker2Button.setEnabled(False)
		self.stt()
		self.ui.Speeker1Result.setText(self.TempTranscription)
		self.ui.Speeker1Button.setEnabled(False)
		self.ui.Speeker2Button.setEnabled(True)

	def SpeekerTwoFunction(self):
		self.ui.StatusLabel.setText('Talk...')
		QApplication.processEvents()
		self.ui.Speeker1Button.setEnabled(False)
		self.stt()
		self.ui.Speeker2Result.setText(self.TempTranscription)
		self.ui.Speeker2Button.setEnabled(False)
		self.ui.Speeker1Button.setEnabled(True)
		


if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	myapp = MyWin()
	myapp.show()
	sys.exit(app.exec_())