import re
from titlecase import titlecase
import webbrowser
import pyclip
while True:
    out = input("Please enter a Sentence:\n")

    # remove multiple spaces
    out = out.strip()
    out = " ".join(out.split())
    
    # add a space after comma
    out = re.sub(r'(?<=[,])(?=[^\s])', r' ', out)

    # Capitalize first character in every word
    out_tle = out.title()

    # Covert the given text to Title Caps, but avoid to cap small words like a/an/the/of
    # drop the end period at the end of text
    out_tle = titlecase(out_tle).rstrip('.').rstrip().rstrip(',')
    print(out_tle)
    # remove the space before a comma
    out_tle = re.sub(r'\s*,', ',', out_tle)

    # print new sentence
    print('New sentence is:\n',out_tle)
    
    # sent the result to your clipboard
    pyclip.copy(out_tle)

    # automatically open google search in broswer and search the address to find out if the address is spelled correctly
    ## Replace symbol "&" with "%26", so Google could handle it
    out_tle = out_tle.replace("&","%26")
    url = "https://www.google.com.tr/search?q={}".format(out_tle)
    webbrowser.open_new_tab(url)

    if out == 'q': # break the loop
        break
print('Loop exited')

