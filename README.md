# Telegram Random Video Bot
This bot serves a random video from a defined pool via a Telegram Inline Message

Originally written for __@tom_scott_bot__ - Gives you a random Tom Scott excuse every time you call it!

## Configuration
This bot uses environment variables to configure it.
* `TOKEN` - Telegram bot token - get this from @BotFather
* `BASE_URL` - The base URL for the video pool (see web server, below)
* `CLIPS` - (int) The number of clips in the pool
* `TITLE` - (optional) The message presented as the response to the inline query

Alternatively, these can be listed in a file called `.env`

## Web Server Layout
This program expects an https-capable web server with a set of mp4 video clips, numbered sequencially. A single thumbnail image, called thumb.jpg, may also be placed next to the files.

### Example
```
BASE_URL
| - thumb.jpg
| - 1.mp4
| - 2.mp4
| - 3.mp4
| - ...
```

## Docker

This program also comes with an associated Docker container for ease of deployment:

```sh
docker run -d --name TGVideoBot -e TOKEN=<token> -e BASE_URL=https://example.com -e CLIPS=20 adamant/tgvideobot
```
