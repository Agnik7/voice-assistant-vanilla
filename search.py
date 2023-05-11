import webbrowser
from googlesearch import search
import speech
# Input the text to search
def find(text):
    # Perform the Google search
    url = ''
    for j in search(text):
        url = j
        break

    # Open the first search result in the browser
    speech.speech("opening in browser....")
    webbrowser.open(url)


