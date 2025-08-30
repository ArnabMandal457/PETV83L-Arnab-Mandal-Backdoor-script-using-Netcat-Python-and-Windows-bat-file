# PookiePrank: A Cute but Terrifying Cybersecurity Awareness Tool 💀🎀


**PLEASE READ THE FULL DOCUMENTATION TO FULLY UNDERSTAND THE PROJECT AND HOW TO MAKE IT ACTUALLY WORK.**

> 🚨 TL;DR: This tool is a local network educational reverse shell simulator designed to teach security awareness and social engineering vulnerabilities. No real exploitation. No persistence. No remote IP targeting.
> 
> ⚠️ **Disclaimer: This tool is for educational and ethical purposes only. Use responsibly. If you end up grounded, disowned, or expelled, that’s on you.**

---

## Table of Contents
- [What Is This?](#what-is-this)
- [Features](#features)
- [Why?](#why)
- [Usage](#usage)
- [Important Notes](#important-notes)
- [Responsible Pranking Guidelines](#responsible-pranking-guidelines)
- [Legal Disclaimer](#legal-disclaimer)
- [Future Plans](#future-plans)

---

##  What Is This?

**PookiePrank** is a lightweight "educational" tool designed to demonstrate the importance of digital awareness through *strategic chaos*.  
It's a prank tool wrapped in charm **cute on the outside, spooky on the inside**.

- Uses `netcat` for remote shell access (with full user control)
- Disguised behind a friendly-looking Python CLI
- An educational simulation that demonstrates how **vulnerable behavior** (like running random executables) can lead to unauthorized access, shown through a safe local network demo.
- Perfect for ethical demos, cybersecurity training, and… *light mischief*.

---

##  Features

- **Silent Netcat Backdoor:** Triggers a reverse shell silently via batch file.
- **User Distraction UI:** Friendly messages and fake interactions to lower suspicion.
- **Remote Payload Execution:** Once connected, send commands in real-time.
- **Prank Arsenal:** Shutdowns, message popups, browser hijacks, and more.
- **Educational Angle:** Reinforces the dangers of blind trust in random executables.

---

##  Why?
Because **people learn faster when they’re scared and slightly crying**.  
This tool aims to:

- Raise awareness of how easily social engineering works.
- Demonstrate how social engineering + trust = disaster
- Teach how reverse shells work in real-world setups
- Serve as a meme-worthy portfolio project
- Make your cybersecurity professors laugh nervously
- Make friends laugh, cry, maybe scream into a pillow and Rickroll them while you’re at it.

  
---

##  Usage

1. Host the executable and `netcat` folder.
2. Share the executable within a controlled test environment (e.g., local network or VM) with **explicit consent** of all parties involved. Never use anonymous link shorteners or tracking tools in real-world scenarios or you can perform an `nmap` scan over the network.
3. Wait for the target to run the file.
4. Connect to the shell:

   Okay, we’re getting a bit technical here. Buckle up and read each line like your life depends on it because, if you mess this up and your friend gets sus, you might end up on the next ride in the prison bus.
   
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
   - here by `4444` we mean the port used for creating the backdoor, and in our case, it’s `4444`.. If required, port number can be changed in the `backdoor.bat` file accordingly.
     
   ---

   **NOTE:**
   
   - You will need to know the target IP address beforehand. You can either use IP Loggers or do an `nmap` scan over the local network using the network id, which can be obtained by the subnet mask and the IP address of your device.
   
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

   Once the target (with prior consent) executes the demo script, you receive a reverse shell connection—simulating unauthorized access risks.




6. Enjoy responsibly (or face karmic doom).
   
  ---

## Important Notes

- 🧼 **No binaries included.** Clone, run, regret (but legally).
- 🛡️ **Antivirus may yeet this into oblivion.** It’s not personal, just code business.
- 🧪 **Virtual machines recommended** unless you enjoy living on the edge.

---

## Responsible Pranking Guidelines

- ☑️ No persistence (we prank, not haunt)
- ☑️ No data theft or spying (we ain’t the NSA)
- ☑️ No real damage, only digital therapy sessions
- ☑️ Reveal the prank soon (or your karma will download a reverse shell on you)
- ☑️ Never use on someone without **consent** (seriously, don’t be that guy)

---

## Legal Disclaimer

- This project is for **educational purposes only**.  
- The creator is not responsible for any misuse, damage, or memes-gone-too-far caused by this script.
- This tool does not include persistence, data collection, remote access over public IPs, or any features beyond safe demo within private networks.

---

## Future Plans

1. Add GUI launcher with meme themes

2. Auto-cancel prank if user types a secret code

3. PookieSec Dashboard™ for multi-prank coordination

4. Add dancing ASCII Rick in the terminal

---

## One Last Thing…

> **IMPORTANT:** For this prank/educational tool to work, **you and your target must be on the same network** (e.g., college Wi-Fi, LAN party, cursed hostel internet).  

> Netcat operates over **local IP addresses** unless you're routing through public ports with port forwarding which we’re *not doing here* (because jail is not part of the prank).

> If you run this on your professor, boss, or crush — we salute your bravery and recommend a lawyer.


> ⚠️ Antivirus Note:
This project may be flagged by antivirus software due to its reverse shell functionality.
However, during testing, no detection occurred on our system.
Detection results can vary based on the antivirus engine, configuration, and updates.

---

## 👀 Hidden Bonus (for the real ones who scroll to the bottom)

If you made it this far congrats, legend.  
You’re now officially certified in:

- ✔️ Cyberprank Literacy  
- ✔️ Netcat Nonsense Navigation  
- ✔️ Surviving PookieSec Ops Training: Level 1  

If you’ve ever Rickrolled someone (and confessed afterward),  
you’ve earned your stripes, your badge, and possibly a cease-and-desist from IT.

Stay chaotic, stay ethical. 💻💅

- *PookieSec Ops Out.*
