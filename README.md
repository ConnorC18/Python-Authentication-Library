# Python Authentication Library


Welcome to the Python authentication library! This library allows you to install the file and have access to functions like, login, signup, reset password ect. This repo is being updated when required.

Contents
+ <a href="https://github.com/ConnorC18/Python-Authentication-Library#getting-started">Getting Started</a>
+ <a href="https://github.com/ConnorC18/Python-Authentication-Library#installing">Installing</a>
+ <a href="https://github.com/ConnorC18/Python-Authentication-Library#examples">Examples</a>
+ + <a href="https://github.com/ConnorC18/Python-Authentication-Library#load-library">Load Library</a>
+ + <a href="https://github.com/ConnorC18/Python-Authentication-Library#sign-up">Sign Up</a>
+ + <a href="https://github.com/ConnorC18/Python-Authentication-Library#login">Login</a>
+ + <a href="https://github.com/ConnorC18/Python-Authentication-Library#check-if-user-is-logged-in">Check if user is logged in</a>
+ + <a href="https://github.com/ConnorC18/Python-Authentication-Library#reset-password">Reset Password</a>
+ + <a href="https://github.com/ConnorC18/Python-Authentication-Library#session-info">Session Info</a>
+ + <a href="https://github.com/ConnorC18/Python-Authentication-Library#logout">Logout</a>
+  <a href="https://github.com/ConnorC18/Python-Authentication-Library#support">Support</a>
+ <a href="https://github.com/ConnorC18/Python-Authentication-Library#version">Version</a>
+ <a href="https://github.com/ConnorC18/Python-Authentication-Library#coming-soon">Coming Soon</a>


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See the examples / usage section on how to use the project on a live system.

#### Prerequisites

What things you need to install for this library to work
```
Python 3.4 Or Above
```

#### Installing
A step by step tutorial that will tell you how to get the library running<br>
First of all download the latest release! You can do this by clicking the button below:
<br>
[![Current Version](https://dabuttonfactory.com/button.png?f=Open+Sans&ts=16&tc=666&hp=24&vp=12&c=round&bgt=unicolored&bgc=eee&bs=1&bc=ccc&t=Download+Latest+Version)](https://github.com/ConnorC18/Python-Authentication-Library/releases/latest)
<br>
<ol>
  <li>Open the .ZIP and drag the <b>loginSystem.py</b> to your project directory</li>
  <li>Inside your project at the top add
  
  ```
  from loginSystem import *
  ```
  
  </li>
</ol>

#### Examples
<a href="https://github.com/ConnorC18/Python-Authentication-Library/wiki">Wiki!</a>
###### Load Library
```
from loginSystem import * # Loads the login library
```
###### Sign Up
```
signup() # Will return True or the error message thrown by the function
```
###### Login
```
login() # Will return True or "incorrectinfo" or "noaccount" depending on the error.
```
###### Check If User Is Logged In
```
checkLoggedIn() # Will return True of False
```
###### Reset Password
```
passwordReset() # Will return True or "noemail" or "wrongsecurityquestionanswer"
```
###### Session Info
```
print(sessionInfo["username"]) # Will return the current logged in users, username
```
###### Logout
```
print(logout())  # Will return True or "notloggedin"
```




#### Support
Contact me on discord: Paint#0001<br>
Email Me: connor.coleman2002@gmail.com

#### Version

<b>Current Version: 1.1.0</b>


#### Coming Soon

+ Email With Password reset will have a subject line























<link rel="stylesheet" href="https://unpkg.com/purecss@1.0.0/build/pure-min.css" integrity="sha384-nn4HPE8lTHyVtfCBi5yW9d20FjT8BJwUXyWZT9InLYax14RDjBj46LmSztkmNP9w" crossorigin="anonymous">
