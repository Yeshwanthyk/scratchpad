#!/usr/bin/env python
##################################################################################
#### reddit Save to Pinboard
#### =======================
####
#### This script sends saved links from reddit to Pinboard. They get added to
#### your unread pile. It may be useful if reddit ever goes down.
#### 
#### Usage
#### -----
#### 
#### Go to your reddit preferences, and under 'content options', tick 'enable
#### private RSS feeds'. Then visit your private RSS feeds page and grab the
#### link for the RSS feed for 'your saved links'.
#### 
#### Use the RSS feed link when calling the script from the shell:
#### 
####     reddit_save_to_pinboard [-t] (saved links feed url) (pinboard username)
####                                  [pinboard password]
#### 
#### If no password is given, it'll ask you for it.
#### 
#### Further information
#### -------------------
#### 
#### Each link is given two tags: 'reddit', and that link's subreddit name.
#### 
#### By default, the Pinboard link is the submitted URL, with a link to the
#### reddit comments page as a comment.
#### 
#### If you like to use the reddit toolbar, use the '-t' option, which sets the
#### toolbar link as the main Pinboard link, and adds the submitted URL in the
#### comments.
#### 
#### Dependencies
#### ------------
#### 
#### You'll need three modules that don't come with Python by default:
#### 
#### - BeautifulSoup
#### - FeedParser
#### - Python-Pinboard
#### 
#### BeautifulSoup and FeedParser are available on pypi, using
#### pip. Python-Pinboard is at https://github.com/mgan59/python-pinboard
####
#### ---
#### 
#### Version: 20111118
#### More information: http://chrispoole.com/project/reddit-pinboard
################################################################################


### Copyright (c) 2011 Chris Poole <chris@chrispoole.com>
### 
### Permission is hereby granted, free of charge, to any person obtaining a copy
### of this software and associated documentation files (the "Software"), to
### deal in the Software without restriction, including without limitation the
### rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
### sell copies of the Software, and to permit persons to whom the Software is
### furnished to do so, subject to the following conditions:
### 
### The above copyright notice and this permission notice shall be included in
### all copies or substantial portions of the Software.
### 
### THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
### IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
### FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
### AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
### LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
### FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
### IN THE SOFTWARE.


from time import sleep
import re
import sys
import getpass

try:
    from BeautifulSoup import BeautifulSoup
except:
    raise ImportError('BeautifulSoup module required.')
try:
    import feedparser
except:
    raise ImportError('feedparser module required.')
try:
    import pinboard
except:
    raise ImportError('pinboard module required.')



def get_from_reddit(reddit_saved_rss_url):
    '''Pull REDDIT_SAVED_RSS_URL feed, collect and return list of tuples.

    Each tuple is of the form (title, title_ascii, url, comment_url, subreddit).'''

    output = []
    rex_subreddit = re.compile(r'^https?://www.reddit.com/r/[^/]+/$')

    try:
        reddit_feed = feedparser.parse(reddit_saved_rss_url)
    except:
        raise ValueError("Couldn't parse reddit RSS feed.")

    for item in reversed(reddit_feed.entries):
        summary_soup = BeautifulSoup(item.summary)

        ## Some unicode characters not handled by urllib.urlencode correctly,
        ## unless UTF-8
        title = item.title.encode('utf-8')
        title_ascii = item.title.encode('ascii', 'replace')

        try:
            subreddit = summary_soup.findAll('a', href=rex_subreddit)[0]['href'].split('/')[-2]
        except IndexError:
            subreddit = ''

        if use_toolbar:
            url = item.link
            comment_url = summary_soup.find(text='[link]').parent['href']
        else:
            try:
                url = summary_soup.find(text='[link]').parent['href']
            except:
                print summary_soup.find(text='[link]')

            try:
                comment_url = summary_soup.findAll('a')[-1]['href']
            except IndexError:
                comment_url = ''
        ## Don't show the URL twice for self posts
        if url == comment_url:
            comment_url = ''

        output.append((title, title_ascii, url, comment_url, subreddit))

    return output



def send_to_pinboard(pinboard_username, pinboard_password, items):
    '''Send ITEMS to Pinboard, requiring form given by `get_from_reddit`:

    (title, title_ascii, url, comment_url, subreddit).'''

    try:
        pinboard_account = pinboard.open(pinboard_username, pinboard_password)
    except:
        raise ValueError('Pinboard username or password incorrect.')
    for item in items:
        try:
            pinboard_account.add(url=item[2],
                                 description=item[0],
                                 extended=item[3].encode('utf-8'),
                                 tags=('reddit', item[4]),
                                 toread='yes')
            print('Added "{}"'.format(item[1]))
        except:
            raise ValueError("Couldn't send \"{}\" to Pinboard.".format(item[1]))

        sleep(1)  # Don't hit the servers too hard



if __name__ == '__main__':
    options = sys.argv[1:]

    if options[0] == "-t":
        use_toolbar = True
        options.pop(0)
    else:
        use_toolbar = False

    reddit_rss_url = options.pop(0)
    username = options.pop(0)

    if options:
        password = options[0]
    else:
        password = getpass.getpass('Pinboard password: ')

    reddit_items = get_from_reddit(reddit_rss_url)
    send_to_pinboard(username, password, reddit_items)
