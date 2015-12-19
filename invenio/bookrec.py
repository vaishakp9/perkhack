import json
from math import sqrt

def sim_pearson(prefs,p1,p2):
  si={}
  for item in prefs[p1]:
      if item in prefs[p2]:
        si[item]=1

  n=len(si)
  if n==0: return 0
  sum1=sum([prefs[p1][it] for it in si])
  sum2=sum([prefs[p2][it] for it in si])
 
  sum1Sq=sum([pow(prefs[p1][it],2) for it in si])
  sum2Sq=sum([pow(prefs[p2][it],2) for it in si])
  
  pSum=sum([prefs[p1][it]*prefs[p2][it] for it in si])
  num=pSum-(sum1*sum2/n)
  den=sqrt((sum1Sq-pow(sum1,2)/n)*(sum2Sq-pow(sum2,2)/n))
  if den==0: return 0
  r=num/den
  return r

def getRecommendations(prefs,person,similarity=sim_pearson):
  totals={}
  simSums={}
  for other in prefs:
    if other==person: continue
    sim=similarity(prefs,person,other)
    if sim<=0: continue
    for item in prefs[other]:
      if item not in prefs[person] or prefs[person][item]==0:
        totals.setdefault(item,0)
        totals[item]+=prefs[other][item]*sim
        simSums.setdefault(item,0)
        simSums[item]+=sim
  
  rankings=[(total/simSums[item],item) for item,total in totals.items()]
  #rankings=[(item) for item,total in totals.items()]
  rankings.sort()
  rankings.reverse()
  return rankings

def recomend(person):
  json_file = open("MainDatabase.json",encoding="latin-1")
  json_str = json_file.read()
  #ustr_to_load = unicode(json_str, 'latin-1')
  json_data = json.loads(json_str)
  #print(person)
  #print(ustr_to_load)
  result=getRecommendations(json_data,person)
  return(result)     
