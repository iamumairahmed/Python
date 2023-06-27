A Simple translator web application using Python, Flask, and Azure Cognitive Services that incorporates AI.

### Introduction
Developing a web application with AI capabilities doesn't have to involve extensive coding or starting from scratch. Let's consider the scenario of creating a website that offers text translation for users.

To simplify the integration of our services without unnecessary complexity, we can choose a framework like Flask. Flask is a lightweight "micro-framework" that provides essential services like routing and templating while allowing flexibility in utilizing backend services. It streamlines the process of setting up and deploying our application quickly. Instead of requiring a database or advanced features, our focus is on selecting a framework that facilitates UI development and enables back-end service calls.

Rather than building our own machine learning model, we can leverage a suite of AI services called Azure Cognitive Services for the back end. These services can be accessed either through an SDK or by making HTTP calls. In our case, we can utilize the Translator service from Azure Cognitive Services to fulfill our main objective of text translation. This approach saves time and effort by utilizing existing AI services rather than reinventing the wheel.

### Development Enviornment Setup
1. Install Visual Studio Code (if not already installed)
2. Install Python (if not already installed)
3. Create a directory for your code
4. Create a virtual environment
5. Install Flask and other libraries
   
### Create App
1. Create new Python application
2. Add the route for our application in app.py file
3. Create the HTML template for our site named index.html
4. Set variable value by executing command `set FLASK_APP=app.py`        
5. Test the application by running `flask run` command
   
### Create Translator Service in Azure
1. Create Azure Account at https://azure.microsoft.com/free
2. Browse to Portal and Select "Create Resource"
3. Select "Translator" and Create
4. Give subscription, resource group name, region, and pricing tier as Free F0
5. Create and Go to Resource once creation completes
6. Select Keys and Endpoints and copy you key, endpoint and location.
7. Create .env file in your Python project root directory.
8. Give following values you just copied
    * KEY=your_key
    * ENDPOINT=your_endpoint
    * LOCATION=your_location

### Call Translator Service from Web App
Run the app and enter text and press Translate button to see the magic
