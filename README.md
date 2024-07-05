# Automated Form Filler with Selenium

This Python script uses Selenium to automate the process of logging in to a website and filling out a survey form. The script opens Chrome, logs in with the provided username and password, and then navigates through the survey, filling out each section.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- You have installed Python 3.x.
- You have installed Google Chrome.
- You have installed the necessary Python packages using the following command:

  ```bash
  pip install -r requirements.txt
  ```

## Usage
# 1. Clone this repository to your local machine:

 ```bash
git clone https://github.com/Maxxel346/Automate-Survey-UPN.git
cd Automate-Survey-UPN
 ```

# 2. Update the USERNAME and PASSWORD variables in the script with your credentials:

 ```python
USERNAME = "your_username"
PASSWORD = "your_password"
 ```

# 3. Run the script:

 ```bash
python SurveyUPN.py
 ```


## Script Explanation

- **Imports and Setup**: The script starts by importing necessary libraries and setting up the Chrome driver.
- **Login Process**: It navigates to the login page, waits for the elements to load, and enters the provided username and password.
- **Survey Filling**: After logging in, the script fills out each section of the survey by selecting predefined options.
- **Completion**: Once the survey is completed, the script closes the browser.

## Notes

- The script includes a manual wait time to solve CAPTCHA. Adjust the wait time (`time.sleep()`) if necessary.
- Make sure the `USERNAME` and `PASSWORD` variables are correctly filled to avoid script termination.

## Contributing

Contributions are always welcome! Please submit a pull request or open an issue to discuss changes.


  
