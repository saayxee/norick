import requests
from termcolor import colored

# Example ASCII Art Logo
ascii_logo = colored(f'''
  
  
  ███╗   ██╗ ██████╗ ██████╗ ██╗ ██████╗██╗  ██╗
  ████╗  ██║██╔═══██╗██╔══██╗██║██╔════╝██║ ██╔╝
  ██╔██╗ ██║██║   ██║██████╔╝██║██║     █████╔╝ 
  ██║╚██╗██║██║   ██║██╔══██╗██║██║     ██╔═██╗ 
  ██║ ╚████║╚██████╔╝██║  ██║██║╚██████╗██║  ██╗
  ╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝╚═╝ ╚═════╝╚═╝  ╚═╝
          {colored("", "white")}     
          
  Never gonna give my streak up.          
  {colored("https://github.com/saayxee/norick", "light_yellow")} 
  
''', "yellow")

# Display the ASCII logo when the script runs
print(ascii_logo)

def verify_rickroll(url):
    try:
        # send an HTTP request to fetch the YouTube page content
        response = requests.get(url)
        
        # check to see if the request was successful (status code 200)
        if response.status_code == 200:
            # list of keywords that identify a rickroll
            rickroll_keywords = ["Rick Roll", "Rick Astley",  "Never Gonna Give You Up", "Whenever You Need Somebody", 'Rickrolled']

            # check to see if any of the keywords appear in the page text
            for rickroll_keyword in rickroll_keywords:
                if rickroll_keyword.lower() in response.text.lower():
                    return True  # the page contains a rickroll
            return False  # no rickroll detected
        else:
            return False  # the page was not found or an error occurred
    except requests.exceptions.RequestException as e:
        print(colored(f"  - Error: {e}", "light_red"))
        return "Error"  # an error occurred


while True: 
    url = input("  Enter a YouTube link (`exit` to stop): ")
    if (url == "exit"):
        print("\n")
        break
    elif ("youtube" not in url.lower()):
        print(colored("  - This link is not a YouTube link. Please enter a YouTube link.\n", "light_red"))
        continue
    elif ("https://" not in url.lower()):
        url = "https://" + url


    if verify_rickroll(url) == "Error":
        print("")
        continue
    elif verify_rickroll(url) :
        print(colored("  - This link is a rickroll! Proceed with caution.\n", "light_red"))
    else:
        print(colored("  - This link is safe. No rickroll detected.\n", "light_green"))
 
