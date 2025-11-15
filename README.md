# Instagram Downloader (Login Mode)

A simple Python script to download Instagram posts and Reels using your account login. Supports session saving and 2FA.

## Requirements

- Python 3.7+
- `instaloader` Python package

## Installation

Install the required package:

```bash
pip install instaloader
```

## Usage

Run the downloader script:

```bash
python insta_downloader_api.py
```
Follow the prompts to login with your Instagram username and password. If 2FA is enabled, you will be asked to enter the verification code.

Once logged in, you can enter Instagram post or Reel URLs to download them. Type exit to quit the program.

## Features

Login with Instagram credentials

Supports Two-Factor Authentication (2FA)

Saves session to avoid logging in every time

Downloads posts and Reels to a folder named after the username
