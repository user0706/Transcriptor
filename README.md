# TRANSCRIPTOR

Transcriptor is a simple tool for transcribing dialogues (conversations) between two people. It supports multiple languages, as well as the ability to specify a dialogue topic.

## Instructions
**Statusbar**
<br>The status bar is located in the upper central part of the window. By following the instructions written on it, it is possible to notice whether the transcription is successful or needs to be repeated again.
<p>**Topic**
<br>There is a possibility to define a certain topic of dialogue. This is possible by entering the topic in the field provided for that. *(Initially, the topic was not defined)*
<p>**Language**
<br>English is the initial language. So if the dialogue is in English, no additional initialization is required.
<br>You can also change the desired language by entering the [code](https://cloud.google.com/translate/docs/languages) for that language in the **language** input field.
<br>In order to apply the desired settings, it is necessary to confirm with the Apply button.

**Rule**
<br>When one speaker speaks, it is necessary to activate the button in order for the transcription to begin. In that case, the other speaker needs to be quiet.
<br>When one speaker finishes saying the sentence, "successful" will be written on the status bar, and only then will the other speaker be able to repeat the same action.

**Transcription database**
<br>The database file is automatically created in the `C:\Users\Public\Documents\Transcriptor` folder, in csv format called `transcript.csv`.
<br>After each successful transcription of any of the speakers, the sentence is automatically added to the same database. Sentences will be added to the same dataset until the file name is changed or moved from the original directory.
<br>The dataset has two columns. One is for the topic that defines the sentence, while the other is the column for the sentence.

Example:
|Topic|Sentence  |
|--|--|
| greeting | Hi |
| greeting | Hello, how are you?|
| personally| I'm fine. How are you?|

>**Note 1**: The database is initially headerless.

>**Note 2**: The encoding type is `utf-8`.


## "Under the hood"

The Transcriptor tool was created in the Python *3.6.0* programming language. The GUI was created in QtDesigner and [PyQt5](https://pypi.org/project/PyQt5/) *v.5.14.2*. [SpeechRecognition](https://pypi.org/project/SpeechRecognition/) *3.8.1* was used as the basic library for speech-to-text conversion

## Screenshot
![Screenshot](https://github.com/user0706/Transcriptor/blob/master/ignore/Screenshot.png?raw=true)
