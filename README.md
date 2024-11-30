# Discord Assignment Announcement Bot

This project is a Discord bot that uses the Discord API and OpenAI's GPT model to automate assignment due date announcements in a class Discord server.

---

## 📦 Project Setup and Installation

Follow these steps to set up and run the project:

### 1️⃣ Clone the Repository
```bash
git clone [https://github.com/henraye/cs_2520_final_project_discord_assignment_announcement_bot/tree/main]
cd [cs_2520_final_project_discord_assignment_announcement_bot]
```
### 2️⃣ Set up your virtual Environment
On Windows
```
python -m venv venv
.\venv\Scripts\activate
```
 On macOS/Linux
```
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install Dependencies
```
pip install -r requirements.txt
```

### 4️⃣ Create the .env File (in your project root directory)
Copy and paste the following code into your .env file, replace each assignment operation with your own information
```
DISCORD_TOKEN=your_discord_bot_token
SPECIFIC_CHANNEL_ID=your_specific_channel_id
PUBLIC_CHANNEL_ID=your_public_channel_id
```

### 5️⃣ Run the Bot
Use the following command in your project root directory to run the program
```
python main.py
```
