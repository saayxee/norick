# Norick
![Mockup image of a CLI (assumingly macOS/zsh) demonstrating the use of the tool](https://github.com/saayxee/norick/blob/main/assets/CLI.jpg?raw=true)
> Norick is a lightweight, simple, and user-friendly CLI tool implemented in Python to check whether a given YouTube link is a Rickroll. It scrapes the raw HTML content of the page and checks for keywords such as "Rick Roll", "Rickrolled", "Never Gonna Give You Up", etc.

## Libraries Used
- Requests: to scrape the HTML content from the link's page.
- Termcolor: to provide a more user-friendly interface by adding color.

## Setup
> [!NOTE]  
> Ensure you have Python 3, pip, and git installed on your machine.

**Clone the repository**

```bash
git clone https://github.com/saayxee/norick
```

**Change directory**

```bash
cd norick
```

**Install termcolor**  

```bash
pip install termcolor
```

## Usage
**Run the script**
```bash
python main.py
```

Now you may enter the URL into the input field and verify if the link is a Rickroll or not.

## Features
> [!TIP]  
> You can enter a URL without the prefix "https://" and the tool will add it automatically.
- Enter any YouTube link.
- User-friendly, color-coded interface and error messages. 
- Rickroll identification through specific keywords found on the page of the HTML content.


## Customization
You can add more keywords to make the tool more efficient for your specific use case.

## Contribution/Bugs
> If you experience any bugs regarding the tool, open an issue and document the problem in detail so that I can replicate it and fix it accordingly.

If you want to contribute a feature or fix a bug yourself, kindly act in accordance with the following instructions/guide:
- Fork the repository.
- Create a new branch for your changes.
- Implement your changes.
- Create a PR.
- Wait for the PR to get approved.

## Developer
Made by Aayan Zaidi ✌️
