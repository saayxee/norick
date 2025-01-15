import requests
from termcolor import colored

# Example ASCII Art Logo
ascii_logo = f'''
  
  
  ███╗   ██╗ ██████╗ ██████╗ ██╗ ██████╗██╗  ██╗
  ████╗  ██║██╔═══██╗██╔══██╗██║██╔════╝██║ ██╔╝
  ██╔██╗ ██║██║   ██║██████╔╝██║██║     █████╔╝ 
  ██║╚██╗██║██║   ██║██╔══██╗██║██║     ██╔═██╗ 
  ██║ ╚████║╚██████╔╝██║  ██║██║╚██████╗██║  ██╗
  ╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝╚═╝ ╚═════╝╚═╝  ╚═╝
          {colored("", "white")}     
  Never gonna give my streak up.          
  {colored("https://github.com/saayxee/norick", "grey")} 

'''


def verify_rickroll(url):
    try:
        # Send an HTTP request to fetch the page content
        response = requests.get(url)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            
            # Define a list of keywords that identify a rickroll
            rickroll_keywords = ["Rick Roll", "Rick Astley",  "Never Gonna Give You Up", "Whenever You Need Somebody", 'Rickrolled']

            # Check if any of the keywords appear in the page text
            for keyword in rickroll_keywords:
                if keyword.lower() in response.text.lower():
                    return True  # The page contains a rickroll
            return False  # No rickroll detected
        else:
            return False  # The page was not found or an error occurred
    except requests.exceptions.RequestException as e:
        print(colored(f"  - Error: {e}", "red"))
        return "Maybe"  # Return false if there was an issue fetching the page

# Display the ASCII logo when the script runs
print(ascii_logo)

# Example usage
while True: 
    url = input("  Enter the YouTube link that you want to check (Input `exit` to leave): ")
    if (url == "exit"):
        print("\n")
        break
    elif ("youtube" not in url.lower()):
        print(colored("  - This link is not a YouTube link. Please enter a YouTube link.\n", "red"))
        continue
    if verify_rickroll(url) == "Maybe":
        print("")
        continue
    elif verify_rickroll(url) :
        print(colored("  - This link is a rickroll! Proceed with caution.\n", "light_red"))
    else:
        print(colored("  - This link is safe. No rickroll detected.\n", "light_green"))
 
