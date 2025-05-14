# Digital Self CLI

## Overview

The **Digital Self CLI** is a Python-based command-line tool designed to conduct reflective interviews. It generates deep, introspective questions, records and transcribes user responses, and saves the data for future use. The project aims to help users build a digital representation of themselves by capturing their thoughts, values, and motivations.

---

## Features

1. **Interview Question Generation**:

   - Uses a language model to generate unique, reflective questions.
   - Avoids repeating previously asked questions.

2. **Speech-to-Text Recording**:

   - Records user responses via a microphone.
   - Transcribes audio responses into text using the Whisper model.

3. **Text-to-Speech**:

   - Reads questions aloud using a TTS (Text-to-Speech) engine.

4. **Data Storage**:

   - Saves questions and answers in a JSONL file for future reference.
   - Maintains a history of previously asked questions to avoid duplicates.

5. **Microphone Selection**:
   - Allows users to select and save a preferred microphone input device.

---

## Installation

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd digital-self
   ```
2. **Set Up Python Environment**:
   - Install Python 3.11.8 (as specified in .python-version).
   - Create a virtual environment:
   ```bash
   uv install
   ```
3. **envs**:
   - Create a `.env` file in the root directory and add your OpenAI API key:
   ```bash
   TOGETHER_API_KEY=your_openai_api_key
   MIC_DEVICE_INDEX=<your-microphone-index can be set using the --select-mic flag or manually if you know the index>
   ```

---

## Usage

1. **Select Microphone**:
   ```bash
   python main.py --select-mic
   ```
2. **Run the CLI**:
   ```bash
   python main.py
   ```
