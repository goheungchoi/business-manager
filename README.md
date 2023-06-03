# business-manager
 
**Author**: Goheung Choi

**Version**: *`0.6.0`*

**Last Update**: *06/02/23*

This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

## Overview

**TODO**

### Key Features

**TODO**

## How to Use

1. Clone this repo `git clone https://github.com/goheungchoi/business-manager.git` in your preferred directory.
2. Make an `.env` file in `business-manager` directory and add following lines.
  ```
  EMAIL_HOST=smtp.gmail.com
  EMAIL_HOST_USER=<your-gmail@gmail.com>
  EMAIL_HOST_PASSWORD=<your-gmail-password>
  ```
3. Open up two terminals or prompts: one for launching the server and the other for the browser UI.
4. For the Server, run
  ```
  bash$ python manage.py runserver
  ```
5. For the UI, run 
  ```
  bash$ cd client
  bash$ npm start
  ```
6. Once you sign up and log in, it will send a log in verification email to your account. Click the link in the email to verify you log in attempt.

## Future Development Roadmap

The following enhancements are planned for future updates

- UI Update: `Account` views and forms.
- Security Update: Data fetch permission using JWT token.
- Security Update: Hide hard-coded credential data from backend and frontend.
- Security Update: Prevent use of `localStorage`.
