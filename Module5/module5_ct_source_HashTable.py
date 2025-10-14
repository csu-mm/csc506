# MS - Artificial Intelligence and Machine Learning
# Course: CSC506 - Design and Analysis of Algorithms
# Professor: Dr. Jonathan Vanover
# Module 5: Critical Thinking
# Created by Mukul Mondal
# Saturday, October 11, 2025
#
# Python Program:
#

'''
Problem statement:

Tackle the problem of optimizing a social media platform's content recommendation system 
using hash tables, considering the immense user data and real-time updates.

Algorithm: Hash Table
Analysis (one page, excluding cover and references): 
  Justify the implementation of a hash table for personalized content recommendations, 
  analyze the time complexity for data retrieval, and 
  discuss the real-life factors impacting hash table performance. 
  Examine external factors influencing the efficiency lower bound for content recommendations.

Please ensure that your submission includes the following components:
  Source code file(s) containing the program implementation.
  A 1-page paper (excluding the cover and references) explaining the program's purpose,... 
'''

from typing import Dict, Tuple, List
import numpy as np
from datetime import datetime
from os import system, name



# This is just a helper function to clear the screen
# This is not required, per problem statement.
def clearScreen():
    if name == 'nt':  # For windows system
        _ = system('cls')    
    else:             # for non-windows system
        _ = system('clear')
    print("")    
    return



# Class representing personalized content (text based content)
class ContentMining:
    def __init__(self):
        self.contentByID_dict: Dict[int, str] = {}
        self.contentIDsByTag_dict: Dict[str, List[int]] = {}
        self.contentAttributesByID_dict: Dict[int, List[int]] = {}  # ['content id', List('content length', 'like count')]
    
    def AddContent(self, id:int, tag:str, content:str):
        if id in self.contentByID_dict == False and len(content.strip()) > 0:
            self.contentByID_dict[hash(id)] = content.strip()
        
        if tag.strip().upper() in self.contentIDsByTag_dict == False:
            self.contentIDsByTag_dict[hash(tag.strip().upper())] = [id]
        else:
            temp1 = self.contentIDsByTag_dict[hash(tag.strip().upper())]
            temp1.append(id)
            self.contentIDsByTag_dict[hash(tag.strip().upper())] = temp1
        
        if id in self.contentAttributesByID_dict == False:
            self.contentAttributesByID_dict[hash(id)] = [len(content.strip()), 0]
        return
    
    def AddContentLike(self, id:int, like:int):
        if id in self.contentAttributesByID_dict == True:
            self.contentAttributesByID_dict[hash(id)][1] = self.contentAttributesByID_dict[hash(id)][1]+like
        return
    
    def GetAllTags(self) -> List[str]:
        return list(self.contentIDsByTag_dict.keys())
    
    def GetContentsByTag(self, tag:str) -> List[int]:
        result: int = []
        if tag.strip().upper() in self.contentIDsByTag_dict == True:
            return self.contentIDsByTag_dict[hash(tag.strip().upper())]
            #  result = "\n\n".join([result, self.contentByID_dict[cid]]) if result else self.contentByID_dict[cid]
        return result


class User:
    def __init__(self, name: str, id: int):
        self.Name: str = name.strip()
        self.ID: int = id


class ContentUser:
    def __init__(self):
        self.userInterests_dict: Dict[int, List[str]] = {}              # <user id, list<tags>>
        self.interactionLog_dict: Dict[Tuple[int, int], datetime] = {}  # <(user id,content id) 'when accessed'>
    
    def AddNewUser_User_Content_Interaction_Cache(self, uid: int, tag: str):
        if uid in self.userInterests_dict == False:
            self.userInterests_dict[hash(uid)] = [tag.strip().upper()]
        else:
            if tag.strip().upper() in self.userInterests_dict[hash(uid)] == False:
                self.userInterests_dict[hash(uid)].append(tag.strip().upper())
        return
    
    def Update_User_Content_Interaction_Cache(self, uid: int, cid: int):
        if id in self.userInterests_dict == True:
            self.interactionLog_dict[hash((uid, cid))] = datetime.now()
        return    

# initialize content (text based content) storage



# This class has the main implementation of the requirements.
# It has implementation of sorting algorithms

# Sorting options implemented for some important properties
# I can sorting options for more/all properties of these model classes
#
# I've added inline comments in multiple places, for user reference.
#
 

if __name__ == "__main__":
    clearScreen()
    print("\n=== CSC506 - Module 5: Critical Thinking ===\n")
    print("=== Algorithm: Hash Table ===")
    print("Use of Dictionary of Hash table for personalized content recommendations.")
    print("Assumption: Only text based content.")
    print("Data mining activity done using Dictionary (Hash table) for personalized content recommendations.")
    print("Every content has: ContentID, TAG, Content text, 'likes count'.")
    print("'Likes count' displayed as: Content Likes: *")
    print("User searches content by : TAG.")
    print("It's possible to add more functionality and make more user friendly.")
    print("It has few default TAGs, Content and Users.")
    print("It's possible to add more TAGs, Content and Users.")
    print("-------------------------------------------\n")


    # === Create required components for testing ===
    # initialize content (text based content) storage
    contentMining = ContentMining()
    contentUserCache = ContentUser()

    # === Add some dummy content ====
    #  User can also call the provided method to add content
    content: str    
    content = "Computer games are interactive digital experiences that combine graphics, storytelling, and gameplay. They entertain, educate, and connect players worldwide through genres like action, strategy, simulation, and role-playing adventures."
    contentMining.AddContent(101, "GAME", content)

    content = "A game is an interactive activity involving rules, strategy, and fun, often played for entertainment, competition, or skill development."
    contentMining.AddContent(102, "GAME", content)

    content = "AI and ML empower machines to learn from data, recognize patterns, and make decisions. They drive innovations in automation, personalization, and predictive analytics across industries like healthcare, finance, and transportation."
    contentMining.AddContent(103, "AIML", content)

    content = "Modern technology drives innovation across industries, enhancing communication, automation, and data analysis. From smartphones to AI and renewable energy, it transforms how we live, work, learn, and connect globally."
    contentMining.AddContent(104, "TECH", content)

    content = "USA politics involves dynamic debates, party divisions, policymaking, elections, and governance shaped by democratic principles and diverse public interests."
    contentMining.AddContent(105, "POLITICS", content)

    content = "Global politics involves the complex interplay of nations, leaders, and institutions shaping international relations, trade, security, and diplomacy. It reflects shifting alliances, power dynamics, and efforts to address global challenges collaboratively."
    contentMining.AddContent(106, "POLITICS", content)
    
    content = "Artificial Intelligence mimics human thinking, enabling machines to learn, adapt, and solve problems across industries like healthcare, finance, and education."
    contentMining.AddContent(107, "AIML", content)

    content = "Technology transforms lives through innovation, connecting people, automating tasks, enhancing efficiency, and driving progress. It powers communication, fuels creativity, enables exploration, and reshapes industries—from healthcare to entertainment to education and beyond."
    contentMining.AddContent(108, "TECH", content)

    content = "Global politics in October 2025 are marked by leadership changes, rising tensions, and democratic struggles. \nAuthoritarian regimes gain UN seats, Israel faces post-conflict reckoningForeign Policy, and Venezuela celebrates Nobel laureate Maria Machado’s democratic advocacy. Europe grapples with fiscal instability and resignationsEY, while Moldova resists Russian interference. Japan pledges $550B investment in the U.S.EY, and China prepares its tech-driven Five-Year Plan"
    contentMining.AddContent(109, "POLITICS", content)

    content = "The U.S. government entered a shutdown on October 1, 2025, due to partisan gridlock over federal spending, affecting nearly 1.6 million workers and halting key services nationwide. \nCongress failed to pass funding legislation for the 2026 fiscal year, triggering the shutdown.\nDisagreements center on spending levels, foreign aid cuts, and health insurance subsidies"
    contentMining.AddContent(110, "POLITICS", content)

    # === Create some random users ===
    allChars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # used for User.Name <== composed of randomly selected 3 characters
    listUsers: List[User] = []
    listUsers.append(User(allChars[np.random.randint(0,25)] + allChars[np.random.randint(0,25)] + allChars[np.random.randint(0,25)], 101))
    listUsers.append(User(allChars[np.random.randint(0,25)] + allChars[np.random.randint(0,25)] + allChars[np.random.randint(0,25)], 102))
    listUsers.append(User(allChars[np.random.randint(0,25)] + allChars[np.random.randint(0,25)] + allChars[np.random.randint(0,25)], 103))
    listUsers.append(User(allChars[np.random.randint(0,25)] + allChars[np.random.randint(0,25)] + allChars[np.random.randint(0,25)], 104))
    listUsers.append(User(allChars[np.random.randint(0,25)] + allChars[np.random.randint(0,25)] + allChars[np.random.randint(0,25)], 105))
    listUsers.append(User(allChars[np.random.randint(0,25)] + allChars[np.random.randint(0,25)] + allChars[np.random.randint(0,25)], 106))
    listUsers.append(User(allChars[np.random.randint(0,25)] + allChars[np.random.randint(0,25)] + allChars[np.random.randint(0,25)], 107))
    listUsers.append(User(allChars[np.random.randint(0,25)] + allChars[np.random.randint(0,25)] + allChars[np.random.randint(0,25)], 108))
    listUsers.append(User(allChars[np.random.randint(0,25)] + allChars[np.random.randint(0,25)] + allChars[np.random.randint(0,25)], 109))
    listUsers.append(User(allChars[np.random.randint(0,25)] + allChars[np.random.randint(0,25)] + allChars[np.random.randint(0,25)], 110))

    # === Testing  ===
    print(" === Default available TAGs: ", contentMining.GetAllTags(), " ===\n")
    contentIds: List[int] = []
    userInput: str = ''
    while userInput != "Q":
        # ask user, which type (content Tag) of content wants to read. Content 'Tag' = High-level content classification
        # search in the contentMining for that content 'Tag'
        randomUser = listUsers[np.random.randint(0,len(listUsers))] # select a random user from User collection
        
        while len(userInput) < 3 and len(contentIds) < 1:
            userInput = input("Enter what type of content, you'd like to read: ").strip().upper()
            if userInput == "Q":   # user wants to 'quit'
                exit(0)
            contentIds = contentMining.GetContentsByTag(userInput)
            if len(contentIds) < 1:
                print("Currently collection has Content type/tag: ", contentMining.GetAllTags())

        # Add new user in 'ContentUserCache' object
        if len(contentIds) > 0:
            contentUserCache.AddNewUser_User_Content_Interaction_Cache(randomUser.ID, userInput)  # ('user id', 'content tag')
        
        # === show content to the User ===
        # display these contents to the user seperated by '\n\n' and numbering, and Content 'Like' count as '*'
        likeCnt: int = -1
        docNum: int = 1
        cntnsText: str = ""
        for cid in contentIds:            
            cntnsText += ("\n\n" + str(docNum) + " ==> ") + contentMining.contentByID_dict[hash(cid)] + ("\nContent Likes: ")
            while likeCnt < contentMining.contentAttributesByID_dict[hash(cid)][1]:
                cntnsText += "*"
                likeCnt += 1
            likeCnt = -1
            docNum += 1        
        
        if len(contentIds) > 0:
            print(cntnsText)
        
        # === update User 'like' count for these contents in 'ContentUserCache' object ===
        #  Assumption: each user visit contributes to '1 like'
        #  Otherwise, I can provide option to call this function, externally
        for cid in contentIds:
            contentMining.AddContentLike(cid, 1)         # ('content id', List['content length', 'likes count'])
        
        # === next iteration ===
        print("\n\nPress Q to quit")
        print("   or  ")
        userInput = ""
        contentIds =[]
        
