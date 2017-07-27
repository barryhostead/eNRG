def ParseHashTags(TweetArray):
        element = "HashTags"
        rows = len(TweetArray)
        DataElementList = []
        while rows >= 0:
            row = rows-1
            DataElement = TweetArray[row][element]
            DataElementID = TweetArray[row]["ID"]
            #print (type(DataElement))
            if type(DataElement) is list:
                if element == "HashTags":
                    for item in DataElement:
                        DataElementList.append([DataElementID,item["text"]])
                
            else:
                DataElementList.append(DataElement)
            
            rows = rows-1
         
        return DataElementList



def ParseMentions(TweetArray):
        element = "Mentions"
      
        rows = len(TweetArray)
        DataElementList = []
        while rows >= 0:
            row = rows-1
            DataElement = TweetArray[row][element]
            DataElementID = TweetArray[row]["ID"]
            #print (type(DataElement))
            if type(DataElement) is list:
                if element == "Mentions":
                    for item in DataElement:
                        DataElementList.append([DataElementID,item["screen_name"]])
            else:
                DataElementList.append(DataElement)
            
            rows = rows-1
         
        return DataElementList



def SearchMentions(Mentions, SearchTerms):
    UniqueUsers = []
    for user in Mentions:
        if user[1] not in UniqueUsers:
            UniqueUsers.append(user[1])

    for user in UniqueUsers:
        print (user)
        TweetArray.append(GetTopNTweetsForUser(user, TopN, consumerKey, consumerSecret, acceesToken, accessSecret))
