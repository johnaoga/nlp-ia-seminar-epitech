#!/usr/bin/env python
# coding: utf-8

# # Spacy for Name Entity Recognition
# 
# ## John Aoga

# # Introduction
# 
# In this project we'll learn how to use Spacy to do **NER**.
# 
# NER standing for Named Entity Recognition is a proccess of identifying entity such as date, mail, person name, in a text.
# 
# 
# [Spacy](https://spacy.io/usage) is the python module/library we'll use to do it here.

# # Installing Spacy

# In[ ]:


get_ipython().system('pip install spacy')


# In[ ]:


get_ipython().system('python -m spacy download en_core_web_lg')


# # Loading Spacy

# In[54]:


import spacy


# # Loading the Web English Small model and Text

# In[55]:


nlp = spacy.load("en_core_web_sm")


# In[56]:


text = """
Artificial intelligence (AI) is intelligence demonstrated by machines, as opposed to natural intelligence displayed by animals including humans. Leading AI textbooks define the field as the study of "intelligent agents": any system that perceives its environment and takes actions that maximize its chance of achieving its goals.[a] Some popular accounts use the term "artificial intelligence" to describe machines that mimic "cognitive" functions that humans associate with the human mind, such as "learning" and "problem solving", however, this definition is rejected by major AI researchers.[b]

AI applications include advanced web search engines (e.g., Google), recommendation systems (used by YouTube, Amazon and Netflix), understanding human speech (such as Siri and Alexa), self-driving cars (e.g., Tesla), automated decision-making and competing at the highest level in strategic game systems (such as chess and Go).[2][citation needed] As machines become increasingly capable, tasks considered to require "intelligence" are often removed from the definition of AI, a phenomenon known as the AI effect.[3] For instance, optical character recognition is frequently excluded from things considered to be AI,[4] having become a routine technology.[5]

Artificial intelligence was founded as an academic discipline in 1956, and in the years since has experienced several waves of optimism,[6][7] followed by disappointment and the loss of funding (known as an "AI winter"),[8][9] followed by new approaches, success and renewed funding.[7][10] AI research has tried and discarded many different approaches since its founding, including simulating the brain, modeling human problem solving, formal logic, large databases of knowledge and imitating animal behavior. In the first decades of the 21st century, highly mathematical statistical machine learning has dominated the field, and this technique has proved highly successful, helping to solve many challenging problems throughout industry and academia.[11][10]
"""


# In[57]:


doc = nlp(text)


# In[58]:


print(len(doc))
print(len(text))


# # `Doc` structure
# 
# ![Alt](http://spacy.pythonhumanities.com/_images/spacy_containers.png)

# In[60]:


#for token in text:
for token in doc:
    print(token)


# In[65]:


#sentence1 = doc.sents
sentence1 = list(doc.sents)[0] 
print(sentence1)


# In[69]:


token8 = sentence1[7]
print(token8)
print(token8.lang)
print(token8.lang_)
print(token8.text)
print(token8.head)
print(token8.right_edge)
print(token8.left_edge)
print(token8.ent_type)
print(token8.morph)
print(token8.pos_)
print(token8.dep_)


# In[70]:


for token in sentence1:
    print (token.text, token.pos_, token.dep_)


# In[71]:


for sent in doc.sents:
    print(sent)


# In[72]:


from spacy import displacy
displacy.render(sentence1, style="dep")


# In[73]:


for ent in doc.ents:
    print(ent, ent.label_)


# In[74]:


displacy.render(doc, style="ent")


# # Reference
# 
# - [Tutorial to learn Spacy](http://spacy.pythonhumanities.com/intro.html)
# 
# ## Other Great Tools
# 
# - [NLTK](http://spacy.pythonhumanities.com/intro.html)

# In[ ]:




