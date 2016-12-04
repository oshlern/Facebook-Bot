import re, random

def openData(doc):
    text = open(doc, 'r')
    text = text.read()
    return text

def cleanText(text):
    # text = re.sub('xxx:', '', text)
    text = re.sub('\n\n\n', '\n', text)
    # stageText = re.findall(r'\[.*\]')
    text = re.sub(r'\[.*\]', '', text) #stage instructions
    return text

def tally(item, superset): # for word, speaker, lineLengths etc.
    if not item in superset:
        superset[item] = {}
    if not item in superset[superset['~last']]:
        superset[superset['~last']][item] = 1
    else:
        superset[superset['~last']][item] += 1
    superset['~last'] = item
    return superset

class Parser:
    def __init__(self, doc):
        self.speakers = {'~null': {}, '~last': '~null'}
        self.words, self.speechLengths, self.lineLengths = {}, {}, {} # Test if = = = works
        self.actLengths, self.sceneLengths, self.playLength = [], [], 0 # not super important
        self.form = {
            'act': r'Act \d+:\n',
            'scene': r'Scene \d+:\n',
            'speaker': r'\n([a-z1-9]+):\n',
            'line': r'([^\n]+)\n',
            'stage': r'\[(.*)\]'
        }
        self.text = openData(doc)

    def exportInfo(self):
        return (self.words, self.speechLengths, self.lineLengths, self.speakers)

    # change to if not last in set: set[last] = {}
    def parseText(self):
        text = cleanText(self.text)
        for act in re.split(self.form['act'], text)[1:]:
            actLength = 0
            for scene in re.split(self.form['scene'], act)[1:]:
                sceneLength = 0
                scene = re.sub(self.form['speaker'], r'\n|speaker|\1|lines|', scene)
                speeches = scene.split('|speaker|')[1:]
                for speech in speeches:
                    speakerAndLines = speech.split('|lines|')
                    speaker = speakerAndLines[0]
                    lines = speakerAndLines[1].split('\n')[:-1]
                    self.addSpeaker(speaker)
                    self.speakers = tally(speaker, self.speakers)
                    lineNum = 0
                    for line in lines:
                        # chars = re.sub(r'([a-zA-z-\'])([^a-zA-z-\'])', r'\1', line)
                        chars = re.sub(r'([^\'])\b([^\'])', r'\1|break|\2', line)
                        chars = re.sub(' ', '', chars)
                        chars = chars.lower()
                        chars = chars.split('|break|')
                        wordNum = 0
                        for word in chars:
                            self.words[speaker] = tally(word, self.words[speaker])
                            wordNum += 1
                        self.lineLengths[speaker] = tally(wordNum, self.lineLengths[speaker])
                        lineNum += 1
                    self.speechLengths[speaker] = tally(lineNum, self.speechLengths[speaker])
                    sceneLength += 1
                self.sceneLengths += [sceneLength]
                actLength += 1
            self.actLengths += [actLength]
            self.playLength += 1

    def addSpeaker(self, speaker):
        # for superset in [self.words, self.lineLengths, self.speechLengths]:
        #     if not speaker in superset:
        #         superset[speaker] = {'~null': {}, '~last': '~null'}
        if not speaker in self.words:
                self.words[speaker] = {'~null': {}, '~last': '~null'}
        if not speaker in self.lineLengths:
                self.lineLengths[speaker] = {'~null': {}, '~last': '~null'}
        if not speaker in self.speechLengths:
                self.speechLengths[speaker] = {'~null': {}, '~last': '~null'}
