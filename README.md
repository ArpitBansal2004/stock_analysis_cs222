# Machine Learning - 'TradingLead' Data-Driven Trading System Proposal


## Introduction

The financial markets generate vast amounts of data daily. This data has potential patterns that can be discerned and leveraged for trading. We design and implement a trading algorithm that uses machine learning techniques to predict short-term price movements and execute profitable trades with a success rate higher than traditional methods.

<img width="841" alt="image" src="https://github.com/CS222-UIUC-FA23/group-project-team33/assets/78969188/7d57567c-783f-470c-8a7c-a126432f9927">




## Technical Architecture

### Application Architecture Diagram

![image](https://github.com/CS222-UIUC-FA23/group-project-team33/assets/78969188/41cc6552-1655-4a6b-aef7-7918fb57e45e)


### Component Details

1. **Machine Learning Model (`modeltrain.py`)**
   - **Role:** Processes financial data for feature extraction and runs machine learning model for stock price prediction.
   - **Interactions:** Receives data from the yfinance API, sends predictions to the Flask backend.
   - **Languages/Libraries:** Python; libraries include pandas, scikit-learn, yfinance.
   - **Developers:** Kavin Jindel and Rishab Doshi focused on the data analysis and model creation.

2. **Flask Backend (`app.py`)**
   - **Role:** Serves as the server-side application handling API requests and integrating the machine learning model.
   - **Interactions:** Communicates with the model and the frontend, processes data, and gives predictions.
   - **Languages/Libraries:** Python; Flask for the web framework.
   - **Developers:** Yoshee Jain and Arpit Bansal, who also worked on web development and data collection.

3. **Frontend (HTML, CSS, JavaScript files: `index.html`, `script.js`, `styles.css`)**
   - **Role:** Provides the user interface for displaying real-time data and predictions.
   - **Interactions:** Interacts with the Flask backend to receive data and display it to the user.
   - **Languages/Libraries:** HTML, CSS, JavaScript.
   - **Developers:** Arpit Bansal and Yoshee Jain were primarily responsible for the frontend development.

4. **Data Source (yfinance)**
   - **Role:** Supplies real-time and historical stock market data.
   - **Interactions:** Directly connected to the machine learning model for data retrieval.
   - **Languages/Libraries:** Python; yfinance library.
   - **Developers:** Managed by the Data Collection Team (Yoshee Jain and Arpit Bansal).

### System Workflow

1. **Data Acquisition:** The machine learning model retrieves data from yfinance.
2. **Data Processing:** Data is cleaned, analyzed, and features are extracted for modeling.
3. **Model Training and Prediction:** The selected machine learning model predicts stock prices.
4. **Data Visualization:** Predictions are visualized and sent to the frontend for display.
5. **User Interaction:** Users interact with the frontend to view predictions and market trends.


## Development

The following are the issues we encountered while developing this project.

### i) Choosing the Optimal Machine Learning Model

(a) What led to the problem:
Given the vast array of machine learning models available, we faced the challenge of selecting the most suitable model for our trading system.

(b) The solution:
We reviewed some machine learning models commonly used in financial predictions. We shortlisted models based on their descriptions, advantages, and historical applications in similar contexts. We utilized a small training and testing dataset (figures smaller than our final test sets) to evaluate model performance. Some models tested included Linear Regression, Support Vector Machines, Random Forest, and Decision Trees. We utilized Mean Squared Error (MSE) to assess model performance. We iteratively tested these models against various subsets of the training and testing data. We then observed how models performed with different features and timeframes and then chose the one with the best performance. 

(c) Why we did what we did: 
This approach ensured that the model we eventually integrated into our trading system had undergone thorough testing and validation, aligning with our commitment to deliver a robust and accurate solution.

### ii) Simplistic Initial Approach in Website Development and Integration of Real-Time Data and Backend Development

(a) What led to the problem:
The team, comprising Arpit, Yoshee, Rishab, and Kavin, had basic knowledge of HTML and CSS but lacked expertise in full stack development. This led to an oversimplified approach in the initial stages of the website creation, focusing only on basic functionalities like plotting points and adding features for displaying coordinate details on hover. As the project progressed, the team encountered limitations with their basic approach, especially when integrating more complex functionalities. The requirement to fetch real-time data from yfinance presented a significant challenge. The team's initial front-end focused approach was insufficient for handling dynamic data retrieval and processing. They realized the need for a more robust solution to incorporate the outputs from the model training code. 

(b) The solution:
To address this, the team developed a server using Flask, creating a backend system that could handle requests from the front end. This server was designed to fetch and process real-time data, returning the appropriate graph for a given company. Successful requests were indicated by a 200 status code, and the corresponding graph was displayed on the website. This phase of the project was crucial in teaching the team about server-side programming, data handling, and the integration of front-end and back-end systems in full stack development.Thus, we had a shift in strategy, opting to use static images generated by the modeltrain.py file for graph representation. 

(c) Why we did what we did: 
We realized the importance of planning and scalability in web development and thus used flask which is a more robust web development library.
  

## Reproducible Installation Instructions

This section outlines the steps necessary to set up the project environment and run the application. 
**Note:** The dependencies listed below are based on our specific system requirements. Due to variations in system configurations, you may need to install additional dependencies. Please adjust the installation process accordingly to suit your system.

### Step 1: Install Required Libraries

Execute the following commands in your terminal to install the necessary libraries for the project:

- **Flask (Web Framework):**
  ```bash
  pip3 install Flask
  ```

- **yfinance (Financial Market Data):**
  ```bash
  pip3 install yfinance
  ```

- **Scikit-learn (Machine Learning Library):**
  ```bash
  pip3 install scikit-learn
  ```

- **Matplotlib (Plotting Library):**
  ```bash
  pip3 install matplotlib
  ```

- **Pandas (Data Analysis Library):**
  ```bash
  pip3 install pandas
  ```

### Step 2: Running the Application

After you have installed all the required libraries, follow these steps to run the application:

1. Open your terminal and navigate to the directory containing the `app.py` file.
2. Start the Flask server by executing:
   ```bash
   python app.py
   ```
3. Open your web browser and access the application at:
   ```plaintext
   http://127.0.0.1:5000/
   ```



## Group Members and their Roles

Group 33
Members: Arpit Bansal (arpitb2), Kavin Jindel (kjindel2), Rishab Doshi (rishabd2), Yoshee Jain (yoshee2) 

### Data Collection Team and Web Development (Yoshee Jain and Arpit Bansal)

Data Collection:
Explore various sources for obtaining stock market data. Choose the most suitable source based on data volume, preprocessing needs, and reliability. Opted for yfinance for its extensive, almost preprocessed dataset. Find real-time and historical market data using libraries like yfinance to pull data from Yahoo Finance. Establish connections to data providers' APIs for continuous data streams.

Web Development Team:
Create a user-friendly interface for the trading system. Integrate the model into the front end of the Flask website. Visualize stock predictions in real-time using real-time graph integration to the back end to ensure the website reflects the latest predictions and market trends.

### Data Analysis and Model Creation and Training Team (Kavin Jindel and Rishab Doshi): 

Data Analysis:
Assess the quality and credibility of the data from each source. Perform data cleaning and preprocessing to prepare the dataset for modeling. Apply feature engineering techniques to extract relevant trading indicators. Normalize data for consistent model training. Conduct a detailed analysis of the data's characteristics, including the amount and granularity of data available for each stock. 

Model Creation and Training Team:
Explore various predictive models, assessing them for complexity and performance. Select the Linear Regression model for its simplicity and lower Mean Squared Error (MSE), indicating better predictive accuracy.

## Future Work

### Database Integration for Efficient Historical Data Management

Optimize the trading system's efficiency and reduce costs by integrating historical data into either MongoDB or PostgreSQL. This strategic move aims to enhance data retrieval processes, minimizing runtime and external API calls.
We can use PostgresSQL or MongoDB for this integration. 

Objective: It keeps the database current with periodic updates based on the most recent past data by developing a systematic update process that is triggered at predefined intervals.

Benefits: It minimizes external API calls by relying on a local database. This optimizes query performance for historical data retrieval. It also leads to reduce data retrieval time by accessing historical data locally. Thus, it decreases operational costs associated with external API calls.
