# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 00:57:37 2023

@author: creis
"""
import unittest
from ps5 import *
from datetime import timedelta

class ProblemSet5NewsStory(unittest.TestCase):
    def setUp(self):
        pass

    def testNewsStoryConstructor(self):
        story = NewsStory('', '', '', '', datetime.now())

    def testNewsStoryGetGuid(self):
        story = NewsStory('test guid', 'test title', 
                          'test description', 'test link', datetime.now())
        self.assertEqual(story.get_guid(), 'test guid')

    def testNewsStoryGetTitle(self):
        story = NewsStory('test guid', 'test title', 
                          'test description', 'test link', datetime.now())
        self.assertEqual(story.get_title(), 'test title')

    def testNewsStoryGetdescription(self):
        story = NewsStory('test guid', 'test title', 
                          'test description', 'test link', datetime.now())
        self.assertEqual(story.get_description(), 'test description')

    def testNewsStoryGetLink(self):
        story = NewsStory('test guid', 'test title', 
                          'test description', 'test link', datetime.now())
        self.assertEqual(story.get_link(), 'test link')

    def testNewsStoryGetTime(self):
        story = NewsStory('test guid', 'test title', 
                          'test description', 'test link', datetime.now())
        self.assertEqual(type(story.get_pubdate()), datetime)

class ProblemSet5(unittest.TestCase):
    def setUp(self):
        class TrueTrigger:
            def evaluate(self, story): return True

        class FalseTrigger:
            def evaluate(self, story): return False

        self.tt = TrueTrigger()
        self.tt2 = TrueTrigger()
        self.ft = FalseTrigger()
        self.ft2 = FalseTrigger()

    def test1TitleTrigger(self):
        cuddly    = NewsStory('', 'The purple cow is soft and cuddly.', '', '', datetime.now())
        exclaim   = NewsStory('', 'Purple!!! Cow!!!', '', '', datetime.now())
        symbols   = NewsStory('', 'purple@#$%cow', '', '', datetime.now())
        spaces    = NewsStory('', 'Did you see a purple     cow?', '', '', datetime.now())
        caps      = NewsStory('', 'The farmer owns a really PURPLE cow.', '', '', datetime.now())
        exact     = NewsStory('', 'purple cow', '', '', datetime.now())

        plural    = NewsStory('', 'Purple cows are cool!', '', '', datetime.now())
        separate  = NewsStory('', 'The purple blob over there is a cow.', '', '', datetime.now())
        brown     = NewsStory('', 'How now brown cow.', '' ,'', datetime.now())
        badorder  = NewsStory('', 'Cow!!! Purple!!!', '', '', datetime.now())
        nospaces  = NewsStory('', 'purplecowpurplecowpurplecow', '', '', datetime.now())
        nothing   = NewsStory('', 'I like poison dart frogs.', '', '', datetime.now())

        s1 = TitleTrigger('PURPLE COW')
        s2  = TitleTrigger('purple cow')
        for trig in [s1, s2]:
            self.assertTrue(trig.evaluate(cuddly), "TitleTrigger failed to fire when the phrase appeared in the title.")
            self.assertTrue(trig.evaluate(exclaim), "TitleTrigger failed to fire when the words were separated by exclamation marks.")
            self.assertTrue(trig.evaluate(symbols), "TitleTrigger failed to fire when the words were separated by assorted punctuation.")
            self.assertTrue(trig.evaluate(spaces), "TitleTrigger failed to fire when the words were separated by multiple spaces.")
            self.assertTrue(trig.evaluate(caps), "TitleTrigger failed to fire when the phrase appeared with both uppercase and lowercase letters.")
            self.assertTrue(trig.evaluate(exact), "TitleTrigger failed to fire when the words in the phrase were the only words in the title.")
            
            self.assertFalse(trig.evaluate(plural), "TitleTrigger fired when the words in the phrase were contained within other words.")
            self.assertFalse(trig.evaluate(separate), "TitleTrigger fired when the words in the phrase were separated by other words.")
            self.assertFalse(trig.evaluate(brown), "TitleTrigger fired when only part of the phrase was found.")
            self.assertFalse(trig.evaluate(badorder), "TitleTrigger fired when the words in the phrase appeared out of order.")
            self.assertFalse(trig.evaluate(nospaces), "TitleTrigger fired when words were not separated by spaces or punctuation.")
            self.assertFalse(trig.evaluate(nothing), "TitleTrigger fired when none of the words in the phrase appeared.")

    def test3altBeforeAndAfterTrigger(self):

        dt = timedelta(seconds=5)
        now = datetime(2016, 10, 12, 23, 59, 59)
        now = now.replace(tzinfo=pytz.timezone("EST"))
        
        ancient_time = datetime(1987, 10, 15)
        ancient_time = ancient_time.replace(tzinfo=pytz.timezone("EST"))
        ancient = NewsStory('', '', '', '', ancient_time)
        
        just_now = NewsStory('', '', '', '', now - dt)
        in_a_bit = NewsStory('', '', '', '', now + dt)
        
        future_time = datetime(2087, 10, 15)
        future_time = future_time.replace(tzinfo=pytz.timezone("EST"))
        future = NewsStory('', '', '', '', future_time)


        s1 = BeforeTrigger('12 Oct 2016 23:59:59')
        s2 = AfterTrigger('12 Oct 2016 23:59:59')

        self.assertTrue(s1.evaluate(ancient), "BeforeTrigger failed to fire on news from long ago")
        self.assertTrue(s1.evaluate(just_now), "BeforeTrigger failed to fire on news happened right before specified time")

        self.assertFalse(s1.evaluate(in_a_bit), "BeforeTrigger fired to fire on news happened right after specified time")
        self.assertFalse(s1.evaluate(future), "BeforeTrigger fired to fire on news from the future")

        self.assertFalse(s2.evaluate(ancient), "AfterTrigger fired to fire on news from long ago")
        self.assertFalse(s2.evaluate(just_now), "BeforeTrigger fired to fire on news happened right before specified time")

        self.assertTrue(s2.evaluate(in_a_bit), "AfterTrigger failed to fire on news just after specified time")
        self.assertTrue(s2.evaluate(future), "AfterTrigger failed to fire on news from long ago")

    def test3BeforeAndAfterTrigger(self):

        dt = timedelta(seconds=5)
        now = datetime(2016, 10, 12, 23, 59, 59)
        ancient = NewsStory('', '', '', '', datetime(1987, 10, 15))
        just_now = NewsStory('', '', '', '', now - dt)
        in_a_bit = NewsStory('', '', '', '', now + dt)
        future = NewsStory('', '', '', '', datetime(2087, 10, 15))

        s1 = BeforeTrigger('12 Oct 2016 23:59:59')
        s2 = AfterTrigger('12 Oct 2016 23:59:59')

        self.assertTrue(s1.evaluate(ancient), "BeforeTrigger failed to fire on news from long ago")
        self.assertTrue(s1.evaluate(just_now), "BeforeTrigger failed to fire on news happened right before specified time")

        self.assertFalse(s1.evaluate(in_a_bit), "BeforeTrigger fired to fire on news happened right after specified time")
        self.assertFalse(s1.evaluate(future), "BeforeTrigger fired to fire on news from the future")

        self.assertFalse(s2.evaluate(ancient), "AfterTrigger fired to fire on news from long ago")
        self.assertFalse(s2.evaluate(just_now), "BeforeTrigger fired to fire on news happened right before specified time")

        self.assertTrue(s2.evaluate(in_a_bit), "AfterTrigger failed to fire on news just after specified time")
        self.assertTrue(s2.evaluate(future), "AfterTrigger failed to fire on news from long ago")
        
if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(ProblemSet5NewsStory))
    suite.addTest(unittest.makeSuite(ProblemSet5))
    unittest.TextTestRunner(verbosity=2).run(suite)    
