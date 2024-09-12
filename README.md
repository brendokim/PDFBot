# Discord Image to PDF Converter Bot

A Discord bot that automates the conversion of user-submitted image files into PDF format. The bot is built with Python, using `discord.py` for bot functionality, `Pillow (PIL)` for image handling, and `ReportLab` for generating PDFs.

## Features

- Converts image files (e.g., PNG, JPEG) submitted in Discord channels into a single, multipage PDF.
- Handles multiple image attachments in a single command.
- Provides error messages for unsupported or invalid file formats.
  
## Usage

1. **Run the bot:**

    ```bash
    python bot.py
    ```

2. **Invite the bot to your Discord server:**

   Use the OAuth2 URL Generator in the Discord Developer Portal to invite the bot to your server.

3. **Use the bot command:**

   - Use the `!convert` command and attach the image files you want to convert to a PDF. The bot will reply with a downloadable PDF file.
