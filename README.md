# Protected Management Frames (PMF) and Their Role in Securing Wi‑Fi Networks

## Project Overview
This project studies how **Protected Management Frames (PMF / IEEE 802.11w)** improve Wi‑Fi security against management-frame abuse, especially **deauthentication attacks**. The work combines a short research write-up with a Python proof-of-concept used **only inside an isolated, authorized lab environment** to observe how networks behave **with and without PMF enabled**.

The project focuses on:
- understanding why traditional management frames were historically vulnerable,
- explaining how deauthentication attacks disrupt Wi‑Fi availability,
- showing how PMF helps protect clients and access points,
- comparing expected behavior in **WPA2 without PMF**, **WPA2 with PMF**, and **WPA3** environments.

## Objective
The main objective is to evaluate whether PMF reduces the effectiveness of spoofed deauthentication frames and to explain the security impact of enabling PMF in modern wireless networks.

## Repository Contents
- `Protected_Management_Frames_PMF_and_Their_Role_i-2.pdf` — project report / term paper describing the topic, scope, background, findings, and references.
- `deauth.py` — Python script included for **controlled educational testing in an isolated lab**.
- `README.md` — overview of the project, structure, and safe usage notes.

## What the Report Covers
The report explains that management frames are essential for Wi‑Fi network control and lifecycle operations, but historically many of them were not protected. This made attacks such as spoofed deauthentication and disassociation possible. The paper also discusses how PMF adds integrity, authenticity, and replay protection for selected management frames, and compares adoption and protection differences between WPA2 and WPA3. 

It also concludes that WPA2 without PMF remains vulnerable to deauthentication attacks, while WPA2 with PMF and WPA3 provide stronger resistance when both the access point and client support PMF correctly. 

## About `deauth.py`
The Python file is a **demonstration script for academic lab observation**. At a high level, it:
- builds IEEE 802.11 deauthentication management frames,
- supports testing against one or more lab targets,
- prints packet metadata and progress information,
- iterates over target channels during the controlled test.

This script exists to help explain **why PMF matters**, not to enable real-world disruption.

## Important Safety and Ethics Notice
This repository is for:
- coursework,
- defensive security education,
- isolated laboratory validation,
- authorized research only.

Do **not** use this project against networks, devices, or users without explicit written permission. Interfering with wireless communications on networks you do not own or administer may violate law, policy, university rules, and ethical standards.

## Lab-Only Evaluation Approach
A safe way to evaluate this project is to compare three controlled scenarios inside a private lab:

1. **WPA2 without PMF**  
   Observe that spoofed deauthentication management traffic can interrupt connectivity more easily.

2. **WPA2 with PMF enabled**  
   Observe that protected clients should ignore forged deauthentication frames when PMF is properly negotiated.

3. **WPA3**  
   Observe that PMF support is stronger by design, which improves baseline resistance to deauthentication abuse.

## Expected Findings
Based on the report, the expected security behavior is:

| Network Configuration | Expected Result |
|---|---|
| WPA2 without PMF | Vulnerable to spoofed deauthentication |
| WPA2 with PMF | Better protection against deauthentication |
| WPA3 | Stronger default protection when PMF is supported |

These outcomes align with the project write-up’s analysis and recommendation to enable PMF where client compatibility allows it. 

## Requirements
For analysis and lab discussion, the project assumes familiarity with:
- IEEE 802.11 basics,
- management, control, and data frames,
- WPA2 / WPA3 concepts,
- PMF / 802.11w,
- wireless monitoring and packet analysis fundamentals.

The Python script itself is written in Python 3 and depends on packet-crafting capabilities commonly provided by wireless security lab environments.

## Limitations
This project has several important limitations:
- PMF does **not** protect every possible wireless attack surface.
- Legacy and IoT devices may not support PMF correctly.
- Real-world protection depends on both the **client** and the **access point** supporting and negotiating PMF.
- Implementation flaws, compatibility issues, and configuration mistakes can weaken protections. 

## Recommendation
The main recommendation of the project is to:
- enable PMF where supported,
- prefer **WPA3** when possible,
- test device compatibility carefully,
- avoid leaving enterprise or sensitive WLAN environments on legacy configurations when stronger management-frame protection is available. 

## Academic Summary
In short, this project demonstrates that **unprotected management frames create a real availability risk in Wi‑Fi networks**, while **PMF significantly reduces that risk** by protecting important management traffic such as deauthentication and disassociation frames. The report argues that PMF should be considered an important defensive control for modern wireless environments. 

## Disclaimer
This repository is shared for **educational documentation and defensive understanding only**. Any practical testing must stay inside a controlled, authorized lab environment and must follow legal and institutional requirements.
