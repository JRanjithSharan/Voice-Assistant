# J.A.R.V.I.S - Voice-Activated Personal Assistant

Jarvis is a Python-based voice-activated personal assistant that performs various tasks and provides information based on voice commands. This assistant utilizes several libraries and APIs to carry out functionalities like answering questions, searching the web, playing music on YouTube, providing weather updates, and more.

## Features

- **Voice Interaction:** Communicate with Jarvis using voice commands.
- **Wikipedia Search:** Retrieve information from Wikipedia by asking specific questions.
- **YouTube Integration:** Play videos on YouTube by instructing Jarvis.
- **Google Search:** Perform Google searches using voice commands.
- **Spotify Integration:** Open the Spotify web player to play music.
- **Time and Date:** Get real-time information on the current time and date.
- **News Updates:** Fetch top headlines from news sources.
- **Weather Forecast:** Get the current weather conditions and temperature.
- **Mathematical Calculations:** Perform mathematical calculations.
- **Shutdown and Restart:** Initiate system shutdown or restart with voice commands.
- **Location Services:** Use Google Maps to locate a place.
- **System Control:** Log off, hibernate, or pause Jarvis based on commands.

## Requirements

- Python
- Various Python libraries (e.g., `wolframalpha`, `pyttsx3`, `speech_recognition`, `pyjokes`, `pywhatkit`, `requests`, `BeautifulSoup`, etc.)
- API keys (e.g., Wolfram Alpha, NewsAPI, OpenWeatherMap) for specific functionalities.

## Usage

1. Install the required Python libraries using the following command:
   ```
   pip install wolframalpha pyttsx3 SpeechRecognition wikipedia pywhatkit playsound feedparser requests beautifulsoup4
   ```

2. Obtain API keys for services like Wolfram Alpha and NewsAPI if you intend to use those features.

3. Run the script `jarvis.py` using Python:
   ```
   python jarvis.py
   ```

4. Follow the voice prompts to interact with Jarvis and execute various commands.

## Additional Notes

- Customize the assistant's voice, name, and other settings in the script.
- Ensure a stable internet connection for services that rely on online data.
- Some functionalities may require additional setup and configurations.

Feel free to explore and modify the code to suit your preferences and needs. Jarvis is designed to be a versatile and interactive personal assistant.
