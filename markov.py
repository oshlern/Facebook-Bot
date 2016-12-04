import random

# Extend to more than just one word
# makeSpeech() and generateText are the only important functions

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
    lineLength = '~null'
    word = lastWord
    for i in xrange(numLines):
        lineLength = pickItem(lineLengths, lineLength)
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
    return text

def generateText(info):
    words, lineLengths, speechLengths, speakers = info
    return makeDialogue(words, lineLengths, speechLengths, speakers, [1,1], [1], 1)