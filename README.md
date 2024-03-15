# Login and Register Form with Online Database

This project contains a login and register form system designed to work with an online database. It's built to provide a seamless interface for user authentication and registration, utilizing a backend database to store and verify user credentials.

# Getting Started

To get this application up and running on your server, follow these steps:

# Prerequisites
Ensure you have a server with internet access and the ability to run Python applications. The database should be accessible online and properly configured to interact with this application.

# Installation
Clone the repository to your server:

git clone https://github.com/xSAY2780/Advanced-Login-Form.git

Install required dependencies by running:

pip install -r requirements.txt

# Configuration
API Setup: If you're planning to deploy the database in a manner that exposes it to external networks and host the application on a server, it's essential to upload api.py to your server.
Modifying api.py: At the end of the api.py file, you will find a comment line indicating where to insert the code necessary for proper server communication. Replace the last two lines of code with the following, ensuring you substitute <server-ip> with your server's IP address:

# Replace these lines with:
app.run(host='<server-ip>', port=5000)

This adjustment tells the application to listen on the specified server IP, making it accessible over your network.

# Usage

After completing the setup and configuration, you can start the application by running:

python main.py

This will start the server, and you can then navigate to the application using a web browser or any client that can interact with HTTP endpoints.

# Contributing

Feel free to fork this repository and submit pull requests if you have suggestions for improvements or have identified any issues.

# License

This project is licensed under the MIT License - see the LICENSE file for details.
