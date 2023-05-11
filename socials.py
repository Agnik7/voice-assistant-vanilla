import webbrowser

def open(social):
    match social:
        case "whatsapp": 
            url = 'https://web.whatsapp.com/'
        case "instagram":
            url = 'https://www.instagram.com/?hl=en'
        case "github":
            url = 'https://github.com/'
        case "linkedin":
            url = 'https://www.linkedin.com/feed/'
        case "medium": 
            url = 'https://medium.com/'
    webbrowser.open(url)