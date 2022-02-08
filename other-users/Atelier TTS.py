#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().system('pip install pyttsx3')


# # Loading

# In[1]:


import pyttsx3


# # First test

# In[2]:


engine = pyttsx3.init()
engine.say("My name is John and I'm here to make my computer talk")
engine.runAndWait()


# # Single line usage with speak function with default options
# 

# In[4]:


pyttsx3.speak("I will speak this text")


# # Changing parameters: Voice, Rate and Volume

# In[5]:


engine = pyttsx3.init() # object creation

""" RATE"""
rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate
engine.setProperty('rate', 125)     # setting up new voice rate

engine.say("My name is John and I'm here to make my computer talk")
engine.runAndWait()


# In[6]:


"""VOLUME"""
volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
print (volume)                          #printing current volume level
engine.setProperty('volume',2.0)    # setting up volume level  between 0 and 1

engine.say("My name is John and I'm here to make my computer talk")
engine.runAndWait()


# In[7]:


"""VOICE"""
voices = engine.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

engine.say("Hello World!")
engine.say('My name is John and I\'m here to make my computer talk ' + str(rate))
engine.runAndWait()
engine.stop()



# In[8]:


"""Saving Voice to a file"""
# On linux make sure that 'espeak' and 'ffmpeg' are installed
engine.save_to_file('My name is John and I\'m here to make my computer talk', 'test.mp3')
engine.runAndWait()


# In[ ]:




