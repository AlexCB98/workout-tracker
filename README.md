# Workout Tracker API

A simple Python project that uses the Nutritionix API to analyze natural language exercise input and save workout data locally in a JSON file.

This project was built using Python, API requests, environment variables, JSON file handling, and error handling with try/except.

---

## Features

- Accepts natural language exercise input from the user
- Sends the exercise query to the Nutritionix API
- Uses personal data such as weight, height, age, and gender for more accurate results
- Extracts exercise name, duration, and calories from the API response
- Saves workout data locally in `workouts.json`
- Automatically creates the JSON file if it does not exist
- Handles empty or corrupted JSON files with `try/except`
- Keeps API credentials hidden using environment variables

---

## What I practiced

- Working with external APIs using `requests`
- Sending POST requests with headers and JSON data
- Reading secret credentials from a `.env` file
- Using `python-dotenv`
- Using `os.environ` for environment variables
- Parsing JSON responses from an API
- Creating dictionaries and lists for structured data
- Saving data into a local JSON file
- Handling `FileNotFoundError`
- Handling `json.JSONDecodeError`
- Using `datetime` to generate current date and time
- Replacing a third-party Google Sheets workflow with local JSON storage

---

## Project structure

```
main.py
workouts.json
.env
.gitignore
```

---

## How to run

Install the required packages:

```bash
pip install requests python-dotenv
```

Create a `.env` file and add your API credentials:

```env
APP_ID=your_app_id
API_KEY=your_api_key
```

Run the project with:

```bash
python main.py
```

Then type an exercise in natural language, for example:

```text
ran for 30 minutes
```

The workout data will be saved in:

```text
workouts.json
```

---

## Technologies used

- Python
- Nutritionix API
- Requests
- python-dotenv
- JSON
- datetime
- os
- try/except error handling

---

## Note

This project was created as part of my Python learning journey through Angela Yu’s Udemy course.

The original version of the course uses Google Sheets through Sheety, but this version saves the workout data locally in JSON because it is simpler, more stable, and better suited for local Python practice.

---

## Author

Alex — Aspiring Python developer building projects step by step through daily practice, with the long-term goal of becoming a professional software developer.