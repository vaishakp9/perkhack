DOCS

Server for PerkHack Customer Advertorial-Review Incentivisation System

For PerkHack
Host : 192.168.1.22:5421

1. /resto
Method : GET Request
Header : "uid : johndoe"

This method returns a csv string with all details of the restaurant based on uid, passed as a header


2. /weight
Method : GET Request
Header : "object_id: johndoe"

This method returns credits based on how popular the post is, ie, number of likes


3. /getSentiment

Method : GET Request
Header : "text : text_to_be_analysed"

This method returns a value between -1 and 1 that accurately depicts the mood of the text, so that the quality of the post can be evaluated, and appropriate Perk credits can be assigned to the reviewer