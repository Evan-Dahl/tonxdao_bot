# 🔥🔥 Tonxdao Tapper Bot 🔥🔥
1. CONCURRENT SESSION HANDLING FOR DAO FARMING
2. AUTO COMPLETES TASKS, CLAIMS DAILY REWARDS

# 🔥🔥 MUST USE PYTHON 3.10 🔥🔥

(MINOR UPDATE) Added a random delay between each cycle instead of the script exiting upon completion

## Features  
The script allows you to farm the **Tonxdao tapper game** by running multiple sessions within a DAO concurrently. You can organize your Telegram sessions into different DAO folders (`dao_1`, `dao_2`, etc.), and the script will run all 5 sessions in each DAO simultaneously. When all sessions in a DAO are tapping together, you achieve **up to 3x the points**, maximizing your rewards while farming. Upon completing the code will move onto the next dao and repeat. In addition to farming, the bot also auto-completes tasks, claims daily rewards, and supports signing up new sessions using referral codes.

## Features  
| Feature                                                     | Supported  |
|-------------------------------------------------------------|:----------:|
| Concurrent session handling with async                      |     ✅     |
| Proxy binding to session                                     |     ✅     |
| Auto ref                                                     |     ✅     |
| Auto check-in                                                |     ✅     |
| Auto farm points                                               |     ✅     |
| Auto complete tasks                                          |     ✅     |
| Referral code sign-up support                                |     ✅     |
| Multi-session DAO farming                                    |     ✅     |

## [Settings](https://github.com/loguru-log/tonxdao_bot/blob/main/.env-example)
| Settings                     | Description                                                                                         |
|------------------------------|-----------------------------------------------------------------------------------------------------|
| **API_ID / API_HASH**         | Telegram API credentials used for the sessions (default platform - android)                         |       
| **REF_LINK**                  | Put your referral link here (default: your ref link)                                                 |
| **AUTO_TASK**                 | Automatically complete tasks (default: True)                                                        |
| **AUTO_PLAY_GAME**            | Automatically farm the game (default: True)                                                         |
| **DELAY_EACH_ACCOUNT**        | Delay between account actions (default: [15,25])                                                    |
| **USE_PROXY_FROM_FILE**       | Whether to use a proxy from the bot/config/proxies.txt file (True / False)                          |
| **DAO_SESSIONS**              | Path to the `dao_sessions` folder containing the subdirectories `dao_1`, `dao_2`, etc.              |

## Quick Start 📚

To install libraries and run the bot, open `run.bat` on Windows or follow the manual instructions below.

## Prerequisites
Before you begin, make sure you have the following installed:
- [Python](https://www.python.org/downloads/) **version 3.10**

## Obtaining API Keys
1. Go to my.telegram.org and log in using your phone number.
2. Select "API development tools" and fill out the form to register a new application.
3. Record the API_ID and API_HASH provided after registering your application in the `.env` file.

## Installation

### Linux manual installation
```shell
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
cp .env-example .env
nano .env  # Here you must specify your API_ID and API_HASH, the rest is taken by default
python3 main.py
```
# You can also use arguments for quick start, for example:
```shell
~/tonxdao_bot >>> python3 main.py --action (1/2)
# Or
~/tonxdao_bot >>> python3 main.py -a (1/2)

# 1 - Run clicker
# 2 - Creates a session
```

### Windows manual installation
```shell
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
copy .env-example .env
# Here you must specify your API_ID and API_HASH, the rest is taken by default
python main.py
```
# You can also use arguments for quick start, for example:
```shell
~/tonxdao_bot >>> python main.py --action (1/2)
# Or
~/tonxdao_bot >>> python main.py -a (1/2)

# 1 - Run clicker
# 2 - Creates a session
```
