
import StimToolLib, os, random, operator
from psychopy import visual, core, event, data, gui, sound

# Future Thinking Task

class GlobalVars:
    #This class will contain all module specific global variables
    #This way, all of the variables that need to be accessed in several functions don't need to be passed in as parameters
    #It also avoids needing to declare every global variable global at the beginning of every function that wants to use it
    def __init__(self):
        self.win = None #the window where everything is drawn
        self.clock = None #global clock used for timing
        self.x = None #X fixation stimulus
        self.output = None #The output file
        self.msg = None
        self.ideal_trial_start = None #ideal time the current trial started
        self.this_trial_output = '' #will contain the text output to print for the current trial
        self.trial = None #trial number
        self.trial_type = None #current trial type
        self.offset = 0.008 #8ms offset--request window flip this soon before it needs to happen->should get precise timing this way
        self.break_instructions = ['''You may now take a short break.''']
        self.line_location_range = 24
        #self.line_location_range = 0.7 #amount the lines (vertical and horizontal) can move left/right and up/down


event_types = {
    'INSTRUCT_ONSET':1,
    'TASK_ONSET':2,
    'TRIAL_ONSET':3,
    'FIXATION_ONSET':4, 
    'IMAGINE_CUE_ONSET': 5,
    'SENTENCE_CUE_ONSET':6,
    'DETAIL_RATING_ONSET': 7,
    'PLEASSANTNESS_RATING_ONSET': 8,
    'DIFFICULTY_RATING_ONSET': 9,
    'RESPONSE':10,
    'TASK_END':StimToolLib.TASK_END
    }


def show_fixation(trial_start, duration):
    """
    Show Fixation 
    """
    
    StimToolLib.mark_event(g.output, g.trial, g.trial_type, event_types['FIXATION_ONSET'], trial_start, 'NA', 'NA', duration, g.session_params['signal_parallel'], g.session_params['parallel_port_address'])
    g.background.draw()
    g.fixation.draw()
    g.win.flip()
    StimToolLib.just_wait(g.clock, trial_start + duration - g.offset) # wait



def show_future_cues(cue_word_1, cue_word_2, cue_word_3):
    """
    Show the Imagine Future Cues
    """
    now = g.clock.getTime()
    StimToolLib.mark_event(g.output, g.trial, g.trial_type, event_types['IMAGINE_CUE_ONSET'], now, 'NA', 'NA', cue_word_1 + '|' + cue_word_2 + '|' + cue_word_3, g.session_params['signal_parallel'], g.session_params['parallel_port_address'])

    text_stim = visual.TextStim(g.win, text = 'Imagine Future', color = 'black', units = 'norm', pos = (0,0.65), height = .15)

    cue_word_1_stim = visual.TextStim(g.win, text = cue_word_1.upper(), color = 'blue', units = 'norm', pos = (0,0.3), height = .1)
    cue_word_2_stim = visual.TextStim(g.win, text = cue_word_2.upper(), color = 'blue', units = 'norm', pos = (0,0), height = .1)
    cue_word_3_stim = visual.TextStim(g.win, text = cue_word_3.upper(), color = 'blue', units = 'norm', pos = (0,-0.3), height = .1)

    g.background.draw()
    text_stim.draw()
    cue_word_1_stim.draw()
    cue_word_2_stim.draw()
    cue_word_3_stim.draw()

    g.win.flip()
    StimToolLib.just_wait(g.clock, now + 15 - g.offset) # wait

def show_control_cues(cue_word_1, cue_word_2, cue_word_3):
    """
    Show the Imagine Future Cues
    """
    now = g.clock.getTime()

    StimToolLib.mark_event(g.output, g.trial, g.trial_type, event_types['SENTENCE_CUE_ONSET'], now, 'NA', 'NA', cue_word_1 + '|' + cue_word_2 + '|' + cue_word_3, g.session_params['signal_parallel'], g.session_params['parallel_port_address'])
    text_stim = visual.TextStim(g.win, text = 'Create Sentence', color = 'black', units = 'norm', pos = (0,0.65), height = .15)

    cue_word_1_stim = visual.TextStim(g.win, text = cue_word_1.upper(), color = 'blue', units = 'norm', pos = (0,0.3), height = .1)
    cue_word_2_stim = visual.TextStim(g.win, text = cue_word_2.upper(), color = 'blue', units = 'norm', pos = (0,0), height = .1)
    cue_word_3_stim = visual.TextStim(g.win, text = cue_word_3.upper(), color = 'blue', units = 'norm', pos = (0,-0.3), height = .1)

    g.background.draw()
    text_stim.draw()
    cue_word_1_stim.draw()
    cue_word_2_stim.draw()
    cue_word_3_stim.draw()

    g.win.flip()
    StimToolLib.just_wait(g.clock, now + 15 - g.offset) # wait

def show_detail_rating_scale():
    """
    Function to call the Detail Rating Scale
    """
    rating_start = g.clock.getTime()
    
    StimToolLib.mark_event(g.output, g.trial, g.trial_type, event_types['DETAIL_RATING_ONSET'], rating_start, 'NA', 'NA', 'NA', g.session_params['signal_parallel'], g.session_params['parallel_port_address'])
    
    text_stim = visual.TextStim(g.win, text = 'Rate Detail', color = 'black', units = 'norm', pos = (0,0.65), height = .15)

    rate_0 = visual.TextStim(g.win, text = '[0]', color = 'black', units = 'norm', pos = (-.6,0), height = .2)
    rate_1 = visual.TextStim(g.win, text = '[1]', color = 'black', units = 'norm', pos = (-.2,0), height = .2)
    rate_2 = visual.TextStim(g.win, text = '[2]', color = 'black', units = 'norm', pos = (.2,0), height = .2)
    rate_3 = visual.TextStim(g.win, text = '[3]', color = 'black', units = 'norm', pos = (.6,0), height = .2)

    sub_text_rate_0 = visual.TextStim(g.win, text = 'Not Vivid at All', color = 'black', units = 'norm', pos = (-.6,-.25), height = .05)
    sub_text_rate_1 = visual.TextStim(g.win, text = 'Little Vivid', color = 'black', units = 'norm', pos = (-.2,-.25), height = .05)
    sub_text_rate_2 = visual.TextStim(g.win, text = 'Somewhat Vivid', color = 'black', units = 'norm', pos = (.2,-.25), height = .05)
    sub_text_rate_3 = visual.TextStim(g.win, text = 'Extremely Vivid', color = 'black', units = 'norm', pos = (.6,-.25), height = .05)
    
    
    event.clearEvents() #clear old keypresses
    responded = False
    while g.clock.getTime() < rating_start + 4:
        if event.getKeys(["escape"]):
            raise StimToolLib.QuitException()
        #the g.run_params['select_X'] is needed to handle left/right button boxes with 4 buttons
        resp = event.getKeys([g.session_params[g.run_params['select_1']], g.session_params[g.run_params['select_2']], g.session_params[g.run_params['select_3']], g.session_params[g.run_params['select_4']]])
        if resp: #subject pressed a 
            response = resp[0]
            # Don't allow them to change their responses
            if not responded:
                if response == g.session_params[g.run_params['select_1']]:
                    rate_0.color = 'red'
                    sub_text_rate_0.color = 'red'
                    r = 0
                if response == g.session_params[g.run_params['select_2']]:
                    rate_1.color = 'red'
                    sub_text_rate_1.color = 'red'
                    r = 1
                if response == g.session_params[g.run_params['select_3']]:
                    rate_2.color = 'red'
                    sub_text_rate_2.color = 'red'
                    r = 2
                if response == g.session_params[g.run_params['select_4']]:
                    rate_3.color = 'red'
                    sub_text_rate_3.color = 'red'
                    r = 3
                now = g.clock.getTime()
                StimToolLib.mark_event(g.output, g.trial, g.trial_type, event_types['RESPONSE'], now, now - rating_start, r, 'NA', g.session_params['signal_parallel'], g.session_params['parallel_port_address'])
                responded = True
        g.background.draw()
        text_stim.draw()
        rate_0.draw()
        rate_1.draw()
        rate_2.draw()
        rate_3.draw()

        sub_text_rate_0.draw()
        sub_text_rate_1.draw()
        sub_text_rate_2.draw()
        sub_text_rate_3.draw()
        g.win.flip()
        StimToolLib.short_wait()
    if not responded: #mark that the subject missed the response, so it's easy to find later (instead of having to look for a BOX_ONSE
        StimToolLib.mark_event(g.output, g.trial, g.trial_type, event_types['RESPONSE'], g.clock.getTime(), 'NA', 'NA', 'NA', g.session_params['signal_parallel'], g.session_params['parallel_port_address'])    
    StimToolLib.just_wait(g.clock, rating_start + 4)
    g.win.flip()
    

def show_pleasant_rating_scale():
    """
    Function to call the Pleassantness Rating Scale
    """
    rating_start = g.clock.getTime()
    
    StimToolLib.mark_event(g.output, g.trial, g.trial_type, event_types['PLEASSANTNESS_RATING_ONSET'], rating_start, 'NA', 'NA', 'NA', g.session_params['signal_parallel'], g.session_params['parallel_port_address'])
    
    text_stim = visual.TextStim(g.win, text = 'Rate Pleasantness', color = 'black', units = 'norm', pos = (0,0.65), height = .15)

    rate_0 = visual.TextStim(g.win, text = '[0]', color = 'black', units = 'norm', pos = (-.6,0), height = .2)
    rate_1 = visual.TextStim(g.win, text = '[1]', color = 'black', units = 'norm', pos = (-.2,0), height = .2)
    rate_2 = visual.TextStim(g.win, text = '[2]', color = 'black', units = 'norm', pos = (.2,0), height = .2)
    rate_3 = visual.TextStim(g.win, text = '[3]', color = 'black', units = 'norm', pos = (.6,0), height = .2)

    sub_text_rate_0 = visual.TextStim(g.win, text = 'Unpleasant', color = 'black', units = 'norm', pos = (-.6,-.25), height = .05)
    sub_text_rate_1 = visual.TextStim(g.win, text = 'Little Unpleasant', color = 'black', units = 'norm', pos = (-.2,-.25), height = .05)
    sub_text_rate_2 = visual.TextStim(g.win, text = 'Somewhat Pleasant', color = 'black', units = 'norm', pos = (.2,-.25), height = .05)
    sub_text_rate_3 = visual.TextStim(g.win, text = 'Pleasant', color = 'black', units = 'norm', pos = (.6,-.25), height = .05)
    
    
    event.clearEvents() #clear old keypresses
    responded = False
    while g.clock.getTime() < rating_start + 4:
        if event.getKeys(["escape"]):
            raise StimToolLib.QuitException()
        #the g.run_params['select_X'] is needed to handle left/right button boxes with 4 buttons
        resp = event.getKeys([g.session_params[g.run_params['select_1']], g.session_params[g.run_params['select_2']], g.session_params[g.run_params['select_3']], g.session_params[g.run_params['select_4']]])
        if resp: #subject pressed a 
            response = resp[0]
            # Don't allow them to change their responses
            if not responded:
                if response == g.session_params[g.run_params['select_1']]:
                    rate_0.color = 'red'
                    sub_text_rate_0.color = 'red'
                    r = 0
                if response == g.session_params[g.run_params['select_2']]:
                    rate_1.color = 'red'
                    sub_text_rate_1.color = 'red'
                    r = 1
                if response == g.session_params[g.run_params['select_3']]:
                    rate_2.color = 'red'
                    sub_text_rate_2.color = 'red'
                    r = 2
                if response == g.session_params[g.run_params['select_4']]:
                    rate_3.color = 'red'
                    sub_text_rate_3.color = 'red'
                    r = 3
                now = g.clock.getTime()
                StimToolLib.mark_event(g.output, g.trial, g.trial_type, event_types['RESPONSE'], now, now - rating_start, r, 'NA', g.session_params['signal_parallel'], g.session_params['parallel_port_address'])
                responded = True
        g.background.draw()
        text_stim.draw()
        rate_0.draw()
        rate_1.draw()
        rate_2.draw()
        rate_3.draw()

        sub_text_rate_0.draw()
        sub_text_rate_1.draw()
        sub_text_rate_2.draw()
        sub_text_rate_3.draw()
        g.win.flip()
        StimToolLib.short_wait()
    if not responded: #mark that the subject missed the response, so it's easy to find later (instead of having to look for a BOX_ONSE
        StimToolLib.mark_event(g.output, g.trial, g.trial_type, event_types['RESPONSE'], g.clock.getTime(), 'NA', 'NA', 'NA', g.session_params['signal_parallel'], g.session_params['parallel_port_address'])    
    StimToolLib.just_wait(g.clock, rating_start + 4)
    g.win.flip()


def show_difficulty_rating_scale():
    """
    Function to call the Difficulty Rating Scale
    Should be shown after each trial type
    """
    rating_start = g.clock.getTime()
    
    StimToolLib.mark_event(g.output, g.trial, g.trial_type, event_types['DIFFICULTY_RATING_ONSET'], rating_start, 'NA', 'NA', 'NA', g.session_params['signal_parallel'], g.session_params['parallel_port_address'])
    
    text_stim = visual.TextStim(g.win, text = 'Rate Difficulty', color = 'black', units = 'norm', pos = (0,0.65), height = .15)

    rate_0 = visual.TextStim(g.win, text = '[0]', color = 'black', units = 'norm', pos = (-.6,0), height = .2)
    rate_1 = visual.TextStim(g.win, text = '[1]', color = 'black', units = 'norm', pos = (-.2,0), height = .2)
    rate_2 = visual.TextStim(g.win, text = '[2]', color = 'black', units = 'norm', pos = (.2,0), height = .2)
    rate_3 = visual.TextStim(g.win, text = '[3]', color = 'black', units = 'norm', pos = (.6,0), height = .2)

    sub_text_rate_0 = visual.TextStim(g.win, text = 'Very Easy', color = 'black', units = 'norm', pos = (-.6,-.25), height = .05)
    sub_text_rate_1 = visual.TextStim(g.win, text = 'Easy', color = 'black', units = 'norm', pos = (-.2,-.25), height = .05)
    sub_text_rate_2 = visual.TextStim(g.win, text = 'Difficult', color = 'black', units = 'norm', pos = (.2,-.25), height = .05)
    sub_text_rate_3 = visual.TextStim(g.win, text = 'Extremely Difficult', color = 'black', units = 'norm', pos = (.6,-.25), height = .05)
    
    
    event.clearEvents() #clear old keypresses
    responded = False
    while g.clock.getTime() < rating_start + 4:
        if event.getKeys(["escape"]):
            raise StimToolLib.QuitException()
        #the g.run_params['select_X'] is needed to handle left/right button boxes with 4 buttons
        resp = event.getKeys([g.session_params[g.run_params['select_1']], g.session_params[g.run_params['select_2']], g.session_params[g.run_params['select_3']], g.session_params[g.run_params['select_4']]])
        if resp: #subject pressed a 
            response = resp[0]
            # Don't allow them to change their responses
            if not responded:
                if response == g.session_params[g.run_params['select_1']]:
                    rate_0.color = 'red'
                    sub_text_rate_0.color = 'red'
                    r = 0
                if response == g.session_params[g.run_params['select_2']]:
                    rate_1.color = 'red'
                    sub_text_rate_1.color = 'red'
                    r = 1
                if response == g.session_params[g.run_params['select_3']]:
                    rate_2.color = 'red'
                    sub_text_rate_2.color = 'red'
                    r = 2
                if response == g.session_params[g.run_params['select_4']]:
                    rate_3.color = 'red'
                    sub_text_rate_3.color = 'red'
                    r = 3
                now = g.clock.getTime()
                StimToolLib.mark_event(g.output, g.trial, g.trial_type, event_types['RESPONSE'], now, now - rating_start, r, 'NA', g.session_params['signal_parallel'], g.session_params['parallel_port_address'])
                responded = True
        g.background.draw()
        text_stim.draw()
        rate_0.draw()
        rate_1.draw()
        rate_2.draw()
        rate_3.draw()

        sub_text_rate_0.draw()
        sub_text_rate_1.draw()
        sub_text_rate_2.draw()
        sub_text_rate_3.draw()
        g.win.flip()
        StimToolLib.short_wait()
    if not responded: #mark that the subject missed the response, so it's easy to find later (instead of having to look for a BOX_ONSE
        StimToolLib.mark_event(g.output, g.trial, g.trial_type, event_types['RESPONSE'], g.clock.getTime(), 'NA', 'NA', 'NA', g.session_params['signal_parallel'], g.session_params['parallel_port_address'])    
    StimToolLib.just_wait(g.clock, rating_start + 4)
    g.win.flip()
    

def do_one_trial(trial):
    """
    Function for displaying 1 trial
    """ 
    
    g.trial_type = trial[0]
    cue_word_1 = trial[1]
    cue_word_2 = trial[2]
    cue_word_3 = trial[3]
    iti_duration = int(trial[4])

    g.win.flip()
    trial_start = g.clock.getTime()
    #mark trial start
    StimToolLib.mark_event(g.output, g.trial, g.trial_type, event_types['TRIAL_ONSET'], trial_start, 'NA', 'NA', 'NA', g.session_params['signal_parallel'], g.session_params['parallel_port_address'])

    show_fixation(trial_start, iti_duration) # Show Fixation

    # Negative, Positive, Neutral Condition
    if g.trial_type != 'd':
        show_future_cues(cue_word_1, cue_word_2, cue_word_3) # Show Imagine Future Cues
        show_detail_rating_scale() # Show the Detail Rating Scale
        show_pleasant_rating_scale() # Show the Pleasant Ratin Scale
    
    # Control Condition
    else:
        show_control_cues(cue_word_1, cue_word_2, cue_word_3)
        show_difficulty_rating_scale() # Show the Difficulty Scale

    g.win.flip()
    g.trial = g.trial + 1 # increment trial number 

def run(session_params, run_params):
    global g
    g = GlobalVars()
    g.session_params = session_params
    g.run_params = StimToolLib.get_var_dict_from_file(os.path.dirname(__file__) + '/EFT.Default.params', {})
    g.run_params.update(run_params)
    
    print os.path.exists(os.path.dirname(__file__) + '/EFT.Default.params')
    try:
        run_try()
        g.status = 0
    except StimToolLib.QuitException as q:
        g.status = -1
    StimToolLib.task_end(g)
    return g.status


def getCueWordsList(cuewords):
    """
    Show Dialogue for getting the Cue words
    """
    cueDlg = gui.Dlg(title = 'Enter Cue Words')
    cueDlg.addText('Negative Future Event 1')
    cueDlg.addField('Cue Word 1', initial = cuewords[0] )
    cueDlg.addField('Cue Word 2', initial = cuewords[1] )
    cueDlg.addField('Cue Word 3', initial = cuewords[2] )
    cueDlg.addText('Negative Future Event 2')
    cueDlg.addField('Cue Word 1', initial = cuewords[3])
    cueDlg.addField('Cue Word 2', initial = cuewords[4] )
    cueDlg.addField('Cue Word 3', initial = cuewords[5] )
    cueDlg.addText('Negative Future Event 3')
    cueDlg.addField('Cue Word 1', initial = cuewords[6])
    cueDlg.addField('Cue Word 2', initial = cuewords[7] )
    cueDlg.addField('Cue Word 3', initial = cuewords[8] )
    cueDlg.addText('Positive Future Event 1')
    cueDlg.addField('Cue Word 1', initial = cuewords[9])
    cueDlg.addField('Cue Word 2', initial = cuewords[10] )
    cueDlg.addField('Cue Word 3', initial = cuewords[11] )
    cueDlg.addText('Positive Future Event 2')
    cueDlg.addField('Cue Word 1', initial = cuewords[12])
    cueDlg.addField('Cue Word 2', initial = cuewords[13] )
    cueDlg.addField('Cue Word 3', initial = cuewords[14] )
    cueDlg.addText('Positive Future Event 3')
    cueDlg.addField('Cue Word 1', initial = cuewords[15])
    cueDlg.addField('Cue Word 2', initial = cuewords[16] )
    cueDlg.addField('Cue Word 3', initial = cuewords[17] )
    cueDlg.addText('Neutral Future Event 1')
    cueDlg.addField('Cue Word 1', initial = cuewords[18])
    cueDlg.addField('Cue Word 2', initial = cuewords[19] )
    cueDlg.addField('Cue Word 3', initial = cuewords[20] )
    cueDlg.addText('Neutral Future Event 2')
    cueDlg.addField('Cue Word 1', initial = cuewords[21])
    cueDlg.addField('Cue Word 2', initial = cuewords[22] )
    cueDlg.addField('Cue Word 3', initial = cuewords[23] )
    cueDlg.addText('Neutral Future Event 3')
    cueDlg.addField('Cue Word 1', initial = cuewords[24])
    cueDlg.addField('Cue Word 2', initial = cuewords[25] )
    cueDlg.addField('Cue Word 3', initial = cuewords[26] )
    cueDlg.addField('Test', choices=['yes', 'no'], initial= 'no')
    cueDlg.show()

    if cueDlg.OK:  # then the user pressed OK
        cuewordsnew = cueDlg.data
        if cuewordsnew[-1] == 'yes': 
            cuewordsnew[0:9] = ['ne1_1', 'ne1_2', 'ne1_3','ne2_1', 'ne2_2', 'ne2_3' ,'ne3_1','ne3_2','ne3_3']
            cuewordsnew[9:18] = ['pe1_1', 'pe1_2', 'pe1_3','pe2_1', 'pe2_2', 'pe2_3' ,'pe3_1','pe3_2','pe3_3']
            cuewordsnew[18:27] = ['nu1_1', 'nu1_2', 'nu1_3','nu2_1', 'nu2_2', 'nu2_3' ,'nu3_1','nu3_2','nu3_3']

        # Check if there is an empty blank fied
        if  '' in cuewordsnew:
            errorDlg = gui.Dlg(title = 'Empy Field')
            errorDlg.addText('There is an empy field. Please fill in all the fields Elisabeth/Zsofi -_-')
            errorDlg.show()
            if errorDlg.OK:
                return getCueWordsList(cuewordsnew) # Show the Dlg again with filled in data

            else:
                print 'QUIT!'
                return -1#the user hit cancel so exit 

        negativeCues = cuewordsnew[0:9]
        positiveCues = cuewordsnew[9:18]
        neutralCues = cuewordsnew[18:27]
        print 'neagtiveCues', negativeCues
        print 'positiveCues', positiveCues
        print 'neutralCues', neutralCues
        return cuewordsnew
    else:
        print 'QUIT!'
        return -1#the user hit cancel so exit 
 
    

def getCueWords(trial_type):
    """
    Get The unused cue words from the global Events
    """
    isUsed =True
    cue_word_1 = ''
    cue_word_2 = ''
    cue_word_3 = ''

    while isUsed:
        eventidx = random.randrange(0,3,1) # Corresponds to an event in various trialtype cues
        print g.eventUsed[trial_type] 
        if not eventidx in g.eventUsed[trial_type]:
            g.eventUsed[trial_type].append(eventidx)
            cue_word_1 = g.cuewords[trial_type][eventidx][0]
            cue_word_2 = g.cuewords[trial_type][eventidx][1]
            cue_word_3 = g.cuewords[trial_type][eventidx][2]
            #print cue_word_1, cue_word_2, cue_word_3
            isUsed = False
    return cue_word_1, cue_word_2, cue_word_3

def run_try():  
#def run_try(SID, raID, scan, resk, run_num='Practice'):
    schedules = [f for f in os.listdir(os.path.dirname(__file__)) if f.endswith('.schedule')]
    if not g.session_params['auto_advance']:
        myDlg = gui.Dlg(title="EFT")
        myDlg.addField('Run Number', choices=schedules, initial=str(g.run_params['run']))
        myDlg.show()  # show dialog and wait for OK or Cancel
        if myDlg.OK:  # then the user pressed OK
            thisInfo = myDlg.data
        else:
            print 'QUIT!'
            return -1#the user hit cancel so exit 
        g.run_params['run'] = thisInfo[0]
    
    #g.x = visual.TextStim(g.win, text="+", units='pix', height=25, color=[-1,-1,-1], pos=[0,0], bold=True)
    
    g.clock = core.Clock()
    start_time = data.getDateStr()
    param_file = g.run_params['run'][0:-9] + '.params' #every .schedule file can (probably should) have a .params file associated with it to specify running parameters (including part of the output filename)
    StimToolLib.get_var_dict_from_file(os.path.join(os.path.dirname(__file__), param_file), g.run_params)
    g.prefix = StimToolLib.generate_prefix(g)

    print '###### Session Params #######'
    print g.session_params
    print '###############################'

    cue_words = []

    # Get the Cue Words
    print '#### Run Params #####'
    print g.run_params
    print '#####################'
    if g.run_params['practice']:
        # If Practice, Entere the words
        cue_words = getCueWordsList( [ '' for i in range(0,27)] )

        # Save the cuue words
        subj_cue_words_file_path = os.path.join(os.path.dirname(g.prefix), g.session_params['SID'] + '-EFT-_cuewords.txt')
        subj_cue_words_file = open(subj_cue_words_file_path, 'w+')
        for word in cue_words:
            subj_cue_words_file.write(word + '\n')
    else:
        # If Not Practice, this words should already be saved
        subj_cue_words_file_path = os.path.join(os.path.dirname(g.prefix), g.session_params['SID'] + '-EFT-_cuewords.txt')

        if not os.path.exists(subj_cue_words_file_path):
            # Word not saved, probably becuase they haven't ran the practice sessions
             StimToolLib.error_popup('Cannot find cuewords file.  Did you run practice session first?')

        print 'EFT: Cue Words File Path: ', subj_cue_words_file_path
        subj_cue_words_file = open(subj_cue_words_file_path, 'r')

        #print subj_cue_words_file.readlines()
        for line in subj_cue_words_file.readlines():
            cue_words.append(line.replace('\n', ''))
        
        getCueWordsList(cue_words)
        

    g.cuewords = {}
    g.cuewords['a'] = [cue_words[0:3],cue_words[3:6], cue_words[6:9] ] # Array of negative Event cues
    g.cuewords['b'] = [cue_words[9:12],cue_words[12:15], cue_words[15:18] ] # Array of positive Event cuese
    g.cuewords['c'] = [cue_words[18:21],cue_words[21:24], cue_words[24:27] ] # Array of neutral Event cues

    print g.cuewords['a']
    print g.cuewords['b']
    print g.cuewords['c']

    # Global Dictionary For the Events Used
    g.eventUsed = {}
    g.eventUsed['a'] = []
    g.eventUsed['b'] = []
    g.eventUsed['c'] = []

    StimToolLib.general_setup(g)

    g.fixation = visual.TextStim(g.win, text = '+', units = 'norm', pos = (0,0), height = .3, color = (-1,-1,-1)) # Save the fixation stmiulus
    g.background = visual.Rect(g.win, units = 'norm', height = 2, width = 2, fillColor = (1,1,1))
    
    schedule_file = os.path.join(os.path.dirname(__file__), g.run_params['run'])
    


    schedule = open(schedule_file, 'r')

    print schedule
    trials = []
    for idx,line in enumerate(schedule):
        if idx == 0:
            continue
        row = line.replace('\n','').split(',')
        trial = []
        trial.append(row[0]) # Trial Types
        trial.append(row[1]) # Cue Word 1
        trial.append(row[2]) # Cue Word 2
        trial.append(row[3]) # Cue Word 3
        trial.append(row[4]) # ITI Duration
        trials.append(trial)

    # Fill in Place Holder with entered cues
    for idx,trial in enumerate(trials):
        trialtype = trial[0]
        if trialtype != 'd':
            cue_word_1, cue_word_2, cue_word_3 = getCueWords(trialtype)
            trials[idx][1] = cue_word_1
            trials[idx][2] = cue_word_2
            trials[idx][3] = cue_word_3
 
    ## 
    print '########'
    for i in trials:
        print i

    
    
    fileName = os.path.join(g.prefix + '.csv')
    #g.prefix = 'DP-' + g.session_params['SID'] + '-Admin_' + g.session_params['raID'] + '-run_' + str(g.run_params['run']) + '-' + start_time
    #fileName = os.path.join(os.path.dirname(__file__), 'data/' + g.prefix +  '.csv')
    g.output = open(fileName, 'w')
    
    sorted_events = sorted(event_types.iteritems(), key=operator.itemgetter(1))
    g.output.write('Administrator:,' + g.session_params['admin_id'] + ',Original File Name:,' + fileName + ',Time:,' + start_time + ',Parameter File:,' +  schedule_file + ',Event Codes:,' + str(sorted_events) + ',Trial Types are coded as follows: 8 bits representing [valence neut/neg/pos] [target_orientation H/V] [target_side left/right] [duration .5/1] [valenced_image left/right] [cue_orientation H/V] [cue_side left/right]\n')
    g.output.write('trial_number,trial_type,event_code,absolute_time,response_time,response,result\n')
    StimToolLib.task_start(StimToolLib.EFT_CODE, g)
    instruct_start_time = g.clock.getTime()
    StimToolLib.mark_event(g.output, 'NA', 'NA', event_types['INSTRUCT_ONSET'], instruct_start_time, 'NA', 'NA', 'NA', g.session_params['signal_parallel'], g.session_params['parallel_port_address'])
    #StimToolLib.show_title(g.win, g.title)
    #g.output.write('Trial_Type:-1:negative;0:neutral;1:positive,Image,ITI_Onset,ITI_startle,Stimulus_onset,Stimulus_startle,Valence_Rating,Valence_rating_time,Arousal_rating,Arousal_rating_time\n')
    

    

    # Run Instructions
    #StimToolLib.run_instructions(os.path.join(os.path.dirname(__file__), g.run_params['instruction_schedule']), g)
    StimToolLib.run_instructions_keyselect(os.path.join(os.path.dirname(__file__), g.run_params['instruction_schedule']), g)

    g.trial = 0
    if g.session_params['scan']:
        StimToolLib.wait_scan_start(g.win)
    else:
        StimToolLib.wait_start(g.win)
    g.win.flip()

    instruct_end_time = g.clock.getTime()
    StimToolLib.mark_event(g.output, 'NA', 'NA', event_types['TASK_ONSET'], instruct_end_time, instruct_end_time - instruct_start_time, 'NA', 'NA', g.session_params['signal_parallel'], g.session_params['parallel_port_address'])
    
    print 'session params'
    print g.session_params
    
    g.trial = 0
    ## Run Trials
    # Block 1
    for idx,trial in enumerate(trials):
        do_one_trial(trial)
    
    
  
 


