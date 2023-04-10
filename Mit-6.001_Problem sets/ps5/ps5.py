# 6.0001/6.00 Problem Set 5 - RSS Feed Filter
# Name:
# Collaborators:
# Time: 5 hours 0 min (15 minutes wasted fixing 1 error in the feedparser module)
#code not finished, given code for the problem is not longer functioning, will maybe
#return later, the classes work fine, the only thing not working is the display of the news
#in a window.

import feedparser
import string
import time
import threading
from project_util import translate_html
from mtTkinter import *
from datetime import datetime
import pytz


#-----------------------------------------------------------------------

#======================
# Code for retrieving and parsing
# Google and Yahoo News feeds
# Do not change this code
#======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        description = translate_html(entry.description)
        pubdate = translate_html(entry.published)

        try:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %Z")
            pubdate.replace(tzinfo=pytz.timezone("GMT"))
          #  pubdate = pubdate.astimezone(pytz.timezone('EST'))
          #  pubdate.replace(tzinfo=None)
        except ValueError:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %z")

        newsStory = NewsStory(guid, title, description, link, pubdate)
        ret.append(newsStory)
    return ret

#======================
# Data structure design
#======================

# Problem 1

# TODO: NewsStory

class NewsStory(object):
    def __init__(self, guid, title, description, link, pubdate):
        """
        Initializes a NewStory object
        self.guid = Global unique identifier of the NewsStory - String
        self.title = title of the NewsStory - String
        self.description = descrption of the NewsStory - String
        self.link = URL to the NewsStory - String
        self.pubdate = date of publication of the NewsStory - datetime
        """
        self.guid = guid
        self.title = title
        self.description = description
        self.link  = link 
        self.pubdate = pubdate

    def get_guid(self):
        '''
        Returns: self.guid
        -------
        Used to safely access self.guid outside of the class

        '''
        return self.guid
    
    def get_title(self):
        '''
        Returns: self.title
        -------
        Used to safely access self.title outside of the class
        '''
        return self.title
    
    def get_description(self):
        '''
        Returns: self.description
        -------
        Used to safely access self.description outside of the class
        '''
        return self.description
    
    def get_link(self):
        '''
        Returns: self.link
        -------
        Used to safely access self.link outside of the class
        '''
        return self.link
    
    def get_pubdate(self):
        '''
        Returns: self.pubdate
        -------
        Used to safely access self.pubdate outside of the class
        '''
        return self.pubdate
        
#======================
# Triggers
#======================

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        # DO NOT CHANGE THIS!
        raise NotImplementedError

# PHRASE TRIGGERS

# Problem 2
# TODO: PhraseTrigger



class PhraseTrigger(Trigger):
    def __init__(self, phrase):
        '''
        Initializes a PhraseTrigger object.
        self.phrase = the pharse with no punctuation. ex ("this is a phrase")

        '''
        assert string.punctuation not in phrase , "Phrase contains punctuation"
        phrase = phrase.lower()
        self.phrase = phrase
        
    def get_phrase(self):
        '''
        Returns: self.phrase
        -------
        Used to safely access self.phrase outside of the class
        '''
        return self.phrase
    
    # def set_phrase(self, newphrase):
    #     '''
    #     Returns: None
    #     -------
    #     Used to safely change the phrase variable of the object
    #     '''
    #     self.phrase = newphrase
    
    def is_phrase_in(self, text):
        '''
        text : String

        Returns: True if self.phrase is present in the text, False otherwise
        -------
        Used to search if self.phrase is present in text, the function is not 
        case sensitive and will detect the phrase even if instead of white spaces
        has other tipe of punctuation to separate the words. ex: "this is a phrase" == "this.is.A.phRase"
        '''
        #Function that check that the words are the same not very similar ones and that they are in the same order
        def is_word_in_order(phrase, text):
            '''
            phrase : String 
            text : String
                Both String must contain only white spaces and letters/number, any special symbol will return a incorrect boolean.
            ----------
            Returns: True if the words in phrase are contained in the same order in text, False otherwise
            '''
            
            phrase_split = phrase.split()
            text_split  = text.split()
            first_word = phrase_split[0]
            if first_word not in text_split:
                return False
            else:
                word_index = text_split.index(first_word)
                #Loop checking for the next word in both the phrase and the text
                for i in range(1, len(phrase_split)):
                    #if the code raises an error that means that the words are not in the same order, normally because the text has the first word at the end of the text
                    try:
                        if phrase_split[i] != text_split[word_index + i]:
                            return False
                    except:
                        return False
                return True
                    
                
        #transform to lower case because the phrase is also in lower case
        text_lower = text.lower()
        
        #Loop that replaces all the punctuation with a space, to make them work as word separators
        for char in string.punctuation:
            text_lower = text_lower.replace(char, " ")
        
        return is_word_in_order(self.phrase, text_lower)                

# Problem 3
# TODO: TitleTrigger
class TitleTrigger(PhraseTrigger):
    def __init__(self, phrase):
        PhraseTrigger.__init__(self, phrase)
    
    def evaluate(self, story):
        '''
        Returns True if an alert should be generated
        for the given news item title, or False otherwise.

        '''
        return self.is_phrase_in(story.get_title())
        
# Problem 4
# TODO: DescriptionTrigger

class DescriptionTrigger(PhraseTrigger):
    def __init__(self, phrase):
        PhraseTrigger.__init__(self, phrase)

    def evaluate(self, story):
        '''
        Returns True if an alert should be generated
        for the given news item description, or False otherwise.

        '''
        return self.is_phrase_in(story.get_description())
    
# TIME TRIGGERS

# Problem 5
# TODO: TimeTrigger
# Constructor:
#        Input: Time has to be in EST and in the format of "%d %b %Y %H:%M:%S".
#        Convert time from string to a datetime before saving it as an attribute.

class TimeTrigger(Trigger):
    def __init__(self, date):
        '''
    
        Parameters
        ----------
        pubdate : String in the format of: day-month(abreviated)-year-hour:minute:second
        Example. "3 Oct 2016 17:00:10 " the datetime needs to be in EST timezone
        -------
        Initializes a timetrigger object wich has 1 pubdate attribute

        '''
        date = datetime.strptime(date, "%d %b %Y %H:%M:%S")
        # date = date.replace(tzinfo=pytz.timezone("EST"))
        self.date = date
    
    def get_date(self):
        '''
        Returns: self.date
        -------
        Used to safely access self.phrase outside of the class
        '''
        
        return self.date
# Problem 6
# TODO: BeforeTrigger and AfterTrigger
class BeforeTrigger(TimeTrigger):
    def __init__(self, date):
        '''

        Parameters
        ----------
        pubdate : String in the format of: day-month(abreviated)-year-hour:minute:second
        Example. "3 Oct 2016 17:00:10 " the datetime needs to be in EST timezone
        -------
        Initializes a BeforeTrigger object

        '''
        TimeTrigger.__init__(self, date)
        
    def evaluate(self, story):
        '''
        
        Parameters
        ----------
        pubdate : String in the format of: day-month(abreviated)-year-hour:minute:second
        Example. "3 Oct 2016 17:00:10 " the datetime needs to be in EST timezone
        -------
        Returns True if the pubdate of the given object is before the trigger date,
        returns False otherwise

        '''
        date = self.get_date()
        story_pubdate = story.get_pubdate()
        
        if story_pubdate.tzinfo != None:
            date = date.replace(tzinfo=pytz.timezone("EST"))
        
        if story_pubdate < date :
            return True
        else:
            return False
        
        
class AfterTrigger(TimeTrigger):
    def __init__(self, date):
        '''

        Parameters
        ----------
        pubdate : String in the format of: day-month(abreviated)-year-hour:minute:second
        Example. "3 Oct 2016 17:00:10 " the datetime needs to be in EST timezone
        -------
        Initializes a AfterTrigger object

        '''
        TimeTrigger.__init__(self, date)
        
    def evaluate(self, story):
        '''
        
        Parameters
        ----------
        trigger : String in the format of: day-month(abreviated)-year-hour:minute:second
        Example. "3 Oct 2016 17:00:10 " the datetime needs to be in EST timezone
        -------
        Returns True if the pubdate of the given object is after the trigger date,
        returns False otherwise

        '''
        date = self.get_date()
        story_pubdate = story.get_pubdate()
 
        if story_pubdate.tzinfo != None:
            date = date.replace(tzinfo=pytz.timezone("EST"))
        
        if date < story_pubdate :
            return True
        else:
            return False
        
        
# COMPOSITE TRIGGERS

# Problem 7
# TODO: NotTrigger
class NotTrigger(Trigger):
    def __init__(self, trigger):
        '''
        Parameters
        ----------
        trigger : Trigger object
        -------
        initializes the NotTrigger class
        '''
        self.trigger = trigger
        
    def evaluate(self, story):
        '''
        Parameters
        ----------
        story : newstory object
        
        Returns : True if the trigger condition is false, returns False if the 
        trigger condition is True

        '''    
        if  not self.trigger.evaluate(story):
            return True
        else:
            return False
        
# Problem 8
# TODO: AndTrigger
class AndTrigger(Trigger):
    def __init__(self, trigger1, trigger2):
        '''
        Parameters
        ----------
        trigger1 : Trigger object
        trigger2 : Trigger object
        -------
        initializes the AndTrigger class
        '''
        self.trigger1 = trigger1
        self.trigger2 = trigger2
        
    def evaluate(self, story):
        '''
        Parameters
        ----------
        story : newstory object
        
        Returns : True if both triggers are true, False otherwise
        '''    
        if self.trigger1.evaluate(story) and self.trigger2.evaluate(story):
            return True
        else:
            return False
        
# Problem 9
# TODO: OrTrigger
class OrTrigger(Trigger):
    def __init__(self, trigger1, trigger2):
        '''
        Parameters
        ----------
        trigger1 : Trigger object
        trigger2 : Trigger object
        -------
        initializes the OrTrigger class
        '''
        self.trigger1 = trigger1
        self.trigger2 = trigger2
        
    def evaluate(self, story):
        '''
        Parameters
        ----------
        story : newstory object
        
        Returns : True if one of the triggers is true, returns False if both 
        triggers are False
        '''    
        if self.trigger1.evaluate(story) or self.trigger2.evaluate(story):
            return True
        else:
            return False

#======================
# Filtering
#======================

# Problem 10
def filter_stories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances.

    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """
    # TODO: Problem 10
    # This is a placeholder
    # (we're just returning all the stories, with no filtering)
    stories_trigger = []
    for story in stories:
        for trigger in triggerlist:
            if trigger.evaluate(story):
                stories_trigger.append(story)
                break
    return stories_trigger



#======================
# User-Specified Triggers
#======================
# Problem 11
def read_trigger_config(filename):
    """
    filename: the name of a trigger configuration file

    Returns: a list of trigger objects specified by the trigger configuration
        file.
    """
    # We give you the code to read in the file and eliminate blank lines and
    # comments. You don't need to know how it works for now!
    trigger_file = open(filename, 'r')
    lines = []
    for line in trigger_file:
        line = line.rstrip()
        if not (len(line) == 0 or line.startswith('//')):
            lines.append(line)

    # TODO: Problem 11
    # line is the list of lines that you need to parse and for which you need
    # to build triggers

    print(lines) # for now, print it so you see what it contains!



SLEEPTIME = 120 #seconds -- how often we poll

def main_thread(master):
    # A sample trigger list - you might need to change the phrases to correspond
    # to what is currently in the news
    try:
        t1 = TitleTrigger("Trump")
        t2 = DescriptionTrigger("china")
        t3 = DescriptionTrigger("rusia")
        t4 = AndTrigger(t2, t3)
        triggerlist = [t1, t4]

        # Problem 11
        # TODO: After implementing read_trigger_config, uncomment this line 
        # triggerlist = read_trigger_config('triggers.txt')
        
        # HELPER CODE - you don't need to understand this!
        # Draws the popup window that displays the filtered stories
        # Retrieves and filters the stories from the RSS feeds
        frame = Frame(master)
        frame.pack(side=BOTTOM)
        scrollbar = Scrollbar(master)
        scrollbar.pack(side=RIGHT,fill=Y)

        t = "Google News"
        title = StringVar()
        title.set(t)
        ttl = Label(master, textvariable=title, font=("Helvetica", 18))
        ttl.pack(side=TOP)
        cont = Text(master, font=("Helvetica",14), yscrollcommand=scrollbar.set)
        cont.pack(side=BOTTOM)
        cont.tag_config("title", justify='center')
        button = Button(frame, text="Exit", command=root.destroy)
        button.pack(side=BOTTOM)
        guidShown = []
        def get_cont(newstory):
            if newstory.get_guid() not in guidShown:
                cont.insert(END, newstory.get_title()+"\n", "title")
                cont.insert(END, "\n---------------------------------------------------------------\n", "title")
                cont.insert(END, newstory.get_description())
                cont.insert(END, "\n*********************************************************************\n", "title")
                guidShown.append(newstory.get_guid())

        while True:

            print("Polling . . .", end=' ')
            # Get stories from Google's Top Stories RSS news feed
            # stories = process("http://news.google.com/news?output=rss")
            stories = process("https://news.google.com/rss?hl=en-US&gl=US&ceid=US%3Aen")
            # Get stories from Yahoo's Top Stories RSS news feed
            # stories.extend(process("http://news.yahoo.com/rss/topstories"))

            stories = filter_stories(stories, triggerlist)

            list(map(get_cont, stories))
            scrollbar.config(command=cont.yview)


            print("Sleeping...")
            time.sleep(SLEEPTIME)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    root = Tk()
    root.title("Some RSS parser")
    t = threading.Thread(target=main_thread, args=(root,))
    t.start()
    root.mainloop()

