# RSS_Parse
This project parses an rss stream for a specific content and generates a new rss 

---

# Soundcloud RSS parsing with Python


Modern Sabahlar(english:Modern Mornings) has long been one of my favorite radio shows. It has been on air for 20 years with some short/long breaks and many Ankarans(is this a thing?) has been waking up to their weekdays with the voice of Ege Fahir Oktay trio. 

Being a fan for years, I have been listening to them through their podcasts since I have moved to US. After a series of unfortunate events shows hosts stopeed broadcasting for more than 6 months until 2 weeks ago. 

Show has returned to a new radio station, Show Radyo of Turkey. Luckily, renewed Show Radyo records and uploads the podcasts online. However, they use a single soundcloud account for all of their shows. In order to access Modern Sabahlar podcast in a traditional way, I decided to start this short project.

# Finding SoundCloud RSS Feed 
My first target was to find the rss feed for the soundcloud podcasts. I found "http://getrssfeed.com" as my tool to get the rss link for the channel.

You should be able to find this information digging into sourcecode of the soundcloud page but this webpage saved me time.

# Parsing RSS Feed
Looking at the raw rss feed, I decided to use BeautifulSoup for python to parse the feed to regenerate a new one. 
First I implemented a basic find to locate the feed for Modern Sabahlar. Then I got rid of rest of the content using decompose:

# Changing Images and Names
My next step was changing the generic channel information such as title, author, show-name and image to information specific to my show. I used "replace_with" command to accomplish this. Details can be found in the github code.
Generating new RSS and Uploading it to Dropbox

I decided to use my raspberry pi device to keep checking the existing stream and upload new rss to dropbox.
In order to do so I used Dropbox Uploader from Andrea Fabrizi. This is a tool that lets you interact with your dropbox account using a developer token.
