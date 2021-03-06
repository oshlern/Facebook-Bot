import random, re

# Extend to more than just one word
# generateResponse() and generateText are the only important functions

def findTotal(weights):
    total = 0
    for weight in weights:
        if type(weight) == int or type(weight) == float:
            total += weight
    return total

def pickItem(items, lastItem):
    if len(items[lastItem]) == 0:
        lastItem = '~null'
    lastItem = items[lastItem]
    total = findTotal(lastItem.values())
    rand = random.random()*total
    for item in lastItem:
        if type(lastItem[item]) == int or type(lastItem[item]) == float:
            if rand<lastItem[item]:
                return item
            rand -= lastItem[item]

def printAct(act):
    return '                 ACT ' + str(act) + ':\n'

def printScene(scene):
    return '                SCENE ' + str(scene) + ':\n'

def printSpeaker(speaker):
    return speaker.capitalize() + ':\n'

def printLine(line):
    return line + '\n'

def printWord(word):
    if word in '.,;:-!?_()':
        return word
    elif word == 'i':
        word = 'I'
    elif word[:2] == 'i\'':
        word = 'I\''
    return ' ' + word

def firstWord(words, lastWord):
    word = pickItem(words, lastWord)
    if word in '.,;:-!?_()':
        for word in words[lastWord]:
            if not word in '.,;:-!?_()':
                return word
        return pickItem(words, '~null')
    else:
        return word

def makeLine(words, lineLength, lastWord):
    text = ''
    word = firstWord(words, lastWord)
    text += ' ' + word.capitalize()
    for i in xrange(lineLength-1):
        word = pickItem(words, word)
        text += printWord(word)
    return (text, word)

def makeSpeech(words, lineLengths, numLines, lastWord):
    text = ''
    lastLineLength = '~null'
    word = lastWord
    for i in xrange(numLines):
        lastLineLength = pickItem(lineLengths, lastLineLength)
        lineLength = max(3, lastLineLength + random.randint(2, 7))
        line, word = makeLine(words, lineLength, word)
        text += printLine(line)
    return text + '\n', word

# Possibly don't use this function (just small dialogue)
def makeDialogue(words, lineLengths, speechLengths, speakers, sceneLengths, actLengths, playLength):
    text = ''
    speaker = '~null'
    for act in range(1, playLength + 1):
        text += printAct(act)
        actLength = random.choice(actLengths)
        for scene in range(1, actLength + 1):
            text += printScene(scene)
            sceneLength = random.choice(sceneLengths)
            for speech in xrange(sceneLength):
                speaker = pickItem(speakers, speaker)
                speechLength = pickItem(speechLengths[speaker], speechLengths[speaker]['~last'])
                speechText, words[speaker]['~last'] = makeSpeech(words[speaker], lineLengths[speaker], speechLength, words[speaker]['~last'])
                speechLengths[speaker]['~last'] = speechLength
                text += printSpeaker(speaker) + speechText
    text += '\nEND'
    return text

class Markov:
    def __init__(self, info):
        self.words, self.lineLengths, self.speechLengths, self.speakers = info
        # print self.lineLengths

    def generateText(self, sceneLengths=[3,3,5,6,7,2,4], actLengths=[2,2,3,4], playLength=3):
        return makeDialogue(self.words, self.lineLengths, self.speechLengths, self.speakers, sceneLengths, actLengths, playLength)

    def generateResponse(self, text):
        if len(text) == 1:
            text = text[0]
        if type(text) == str:
            text = text.split()
            for i in range(len(text)):
                if not re.search(r'\w', text[i]):
                    text = text.splice(i)

        numWords = len(text)
        responseLength = max(2, numWords/3 + random.randint(-1,2))
        print "TEXT", text
        # speaker = random.choice(self.words.keys())
        speaker = random.choice(["othello", "desdemona", "iago", "iago", "iago", "othello"])
        # speaker = "othello"
        print speaker
        index = 1
        while not text[-index] in self.words[speaker].keys() and index < numWords:
            index += 1
        if index == numWords:
            lastWord = "~null"
        else:
            lastWord = re.sub(text[-index], '.,?!', '')
        return "Response by: " + speaker + "\n" + makeSpeech(self.words[speaker], self.lineLengths[speaker], responseLength, lastWord)[0]
