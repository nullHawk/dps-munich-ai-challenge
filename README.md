# DPS AI Challenge


## Introduction

This repository contains the code s for the DPS AI Challenge.

**Goal**: Given the Dataset about traffic accidents, You need to predict total number of traffic accidents on the given month of a year.

## Aproach:
- At first I tried to use LSTM model for Time Sequence Prediction of accidents, but the model failed to predict the number of accidents properly,
- Used SARIMA model, since the the Time Sequence is Sesional

## Installation

To get started with the project, clone the repository and install the necessary dependencies:

```bash
git clone https://github.com/nullHawk/dps-munich-ai-challenge
cd dps_ai_challenge
pip install -r requirements.txt
```

## Usage

To run the project, use the following command:

```bash
python app.py
```

The application will start running at `http://localhost:8080`

**Using API**

to get a prediction from the API, send a POST request to http://localhost:8080/prediction with the following JSON payload:
```
{
  "year": 2024,
  "month": 1
}
```