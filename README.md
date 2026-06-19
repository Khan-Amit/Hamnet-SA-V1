# Hamnet-SA-V1™
IRON‑CLAD PROPRIETARY LICENSE

Copyright (c) 2026 Seliim Ahmed (amit.khanna.1082@gmail.com)

ALL RIGHTS RESERVED.

This software, including its source code, documentation, and any associated files (collectively, the "Software"), is the exclusive property of Seliim Ahmed. The Software is provided "as is" without warranty of any kind, express or implied.

No license, express or implied, is granted to any person or entity to use, copy, modify, distribute, sublicense, or create derivative works of the Software, in whole or in part, except as explicitly permitted in writing by the copyright holder.

Any unauthorised use, reproduction, distribution, or reverse engineering of the Software, or any portion thereof, may result in severe civil and criminal penalties, and will be prosecuted to the maximum extent possible under law.

For permission requests, contact: amit.khanna.1082@gmail.com
Free internet engine 
# hamnet-SA-V1 – U‑groove Ternary Frequency Engine

**Concept & Architecture:** Seliim Ahmed (amit.khanna.1082@gmail.com)  
**License:** Iron‑Clad Proprietary – all rights reserved.

---

## Vision
A self‑contained, peer‑to‑peer communication system that transcends conventional binary modems. By binding data to frequency ratios (“U‑groove” ternary) and using the Cosmic Microwave Background as a universal noise reference, **hamnet-SA-V1** scales from audio‑based Morse to a 9G‑ready network backbone – **no internet gatekeepers, no centralised control, uncensorable by design.**

## Features
- **Morse ↔ Binary ↔ ASCII** real‑time translation with audible signal generation.
- **Live microphone decoding** – uses Web Audio FFT to detect Morse tones.
- **Adjustable speed** (5–50 WPM) for flexible transmission.
- **“Transfer to Internet Ready”** – activates WebRTC peer‑to‑peer mode for direct device‑to‑device voice/video/data over Wi‑Fi or Bluetooth (no internet required).
- **Video transmission** – camera stream shared directly between two browsers via manual SDP exchange.
- **Voice test** – record and simulate voice‑to‑Morse‑to‑text loop.
- **Built‑in interpolation** – sub‑sample timing recovery for robust decoding in noisy environments (the foundation for our 9G scaling).

## How It Works (Technical)
1. **Morse Encoding** – text is mapped to ITU Morse, then to binary (8‑bit ASCII per character), and finally synthesised as audio tones (800 Hz) with dot/dash timing derived from the WPM setting.
2. **Frequency Binding** – each binary state is bound to a carrier ratio (1.0×, 0.8×, 1.2×) – the “U‑groove” – enabling ternary state detection and better spectral efficiency.
3. **Interpolation Decoder** – incoming audio is over‑sampled (4×) and threshold‑crossings are measured to reconstruct dot/dash lengths. This gives immunity to clock drift and multipath.
4. **Peer‑to‑Peer Layer** – uses WebRTC with **no STUN/TURN** servers; devices exchange SDP offers/answers manually, forming a direct radio‑like link over existing local networks (cellular hotspot, Wi‑Fi Direct, or Bluetooth PAN).
5. **Cosmic Noise Reference** – the engine can optionally use ambient noise (from a TV antenna) as a calibration source to auto‑adjust gain and threshold – a built‑in nod to the Big Bang static concept.

## Getting Started
1. **Clone this repository** or open `index.html` in a Chromium‑based browser.
2. Allow microphone/camera permissions when prompted.
3. Type text in the input box and click **“Encode & Send”** to hear Morse audio.
4. Click **“Decode from Mic”** and speak/send Morse – the engine will attempt to decode (demo‑level).
5. For video P2P:
   - Start camera on both devices.
   - On one device click **“Create Offer”**, copy the SDP, and send it to the peer.
   - Peer pastes the offer into their **“Answer SDP”** box and clicks **“Set Answer”** – the stream should connect.

## Legal Notice
This software is the exclusive intellectual property of **Seliim Ahmed**.  
**No part** may be copied, modified, redistributed, or used for commercial purposes without explicit written permission.  
Any unauthorised use, reverse engineering, or patent filing based on the disclosed concepts will be prosecuted to the fullest extent of the law.

## Future Roadmap
- Integration with SDR (HackRF / USRP) for real RF transmission.
- Full ternary encoding (3‑state symbols) for higher data density.
- AI‑based symbol synchronisation using neural networks.
- Mobile app version for iOS/Android with native radio APIs.

---

*“Free internet, unrestricted and unclamped.”* – Seliim Ahmed
