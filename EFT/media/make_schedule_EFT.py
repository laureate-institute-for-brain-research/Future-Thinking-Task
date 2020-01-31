#/usr/bin/env python

# Make The schedule for EFT Task

# 4 Trial Types
# a. negative future
# b. positive future
# c. neutral future
# d. control 

# 3 Blocks. After Each Block, set Boolean to True

import os,random


# Get Controlw Word List
controlf = open('control_word_list.csv', 'r')
control_words = []
for line in controlf.readlines():
    control_words.append(line.replace('\n',''))

used_control_words = []

def getJitteredITI():
    """
    Fixation Cross is jittered to 2-12 seconds
    return number from 2,12 inclusive
    """
    return random.randrange(2,12,1)


def getUnusedControlWord():
    """
    Returns a control word not already used
    """
    isUsed = True
    while isUsed:
        randomControlWord = random.choice(control_words)
        if not randomControlWord in used_control_words:
            used_control_words.append(randomControlWord)
            isUsed = False
    
    return randomControlWord


def placeHolder(trial_type):
    """
    Return 3 words with placeholder words unless it's a control
    """
    if trial_type == 'a':
        return 'Negative_Cue_1,Negative_Cue_2,Negative_Cue_3'
    if trial_type == 'b':
        return 'Positive_Cue_1,Positive_Cue_2,Positive_Cue_3'
    if trial_type == 'c':
        return 'Neutral_Cue_1,Neutral_Cue_2,Neutral_Cue_3'
    if trial_type == 'd':
        # Control Get 3 random words not already used
        controlcues = [ getUnusedControlWord() for i in range(0,3)] # 3 control words not used
        return ','.join(controlcues)


def getDifficultyRating(idx):
    """
    Difficult Rating needs to be shown after each block
    """
    if idx == 3:
        return True
    else:
        return False

# Make the Sequence
final = []
# 3 blocks
for i in range(1,4):
    row = ['a','b','c','d']
    random.shuffle(row)
    
    for idx,trial_type in enumerate(row):
        finalrow = []
        finalrow.append(trial_type)
        finalrow.append(placeHolder(trial_type))
        finalrow.append(str(getJitteredITI()))
        #finalrow.append(str(getDifficultyRating(idx)))
        #print idx,trial_type,getJitteredITI()
        final.append(finalrow)


# Write Schedule to File
schedulef = open('EFT_R1.schedule', 'w+')
schedulef.write('Trial Type, cue_word1,cue_word2, cue_word3,iti_duration\n') # Wrte Header
for row in final:
    schedulef.write(','.join(row) + '\n')
