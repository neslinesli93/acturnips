## /r/acturnips bot

**Requires python >= 3.5**

## Setup

Clone the repo and run:

```sh
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

---

Create a `config.json` in the root of the project. Copy `config.example.json` and enter your desired values.

**It's mandatory that you create a new reddit app**. [Check the instructions](https://www.reddit.com/prefs/apps) on how to make a new app, and once you are done, copy `client_id` and `client_secret` inside your `config.json`

---

Start the bot

```sh
python bot.py
```
