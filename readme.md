# CELIO ATTACK v1.0 - Advanced Attack Tool

**CELIO ATTACK** is a modular and powerful DDOS attack script designed to target both the network infrastructure (Layer 4) and the application layer (Layer 7). This tool combines different attack vectors into a single interface, allowing you to perform flexible and effective tests.

## Legal Disclaimer

**THIS TOOL IS FOR LEGAL AND EDUCATIONAL PURPOSES ONLY.**

Using this script against systems, networks, or websites without permission is illegal and can have serious consequences. The developer is not responsible for any illegal use of this tool. Only use it on systems you own or have explicit permission to test.

## Core Features

-   **Multi-Layer Attacks:** Capable of launching attacks on both network (L4) and application (L7) layers.
-   **Modular Menu:** Easily select the attack layer and method through a user-friendly menu.
-   **Layer 7 (Application) Attacks:**
    -   **Advanced HTTP Flood:** Smart HTTP requests that mimic real user behavior (random User-Agent, Referer, etc.) and bypass caching mechanisms (cache-busting).
    -   **Proxy Support:** Ability to route attack traffic through a list of proxies to anonymize and distribute the attack source.
-   **Layer 4 (Network) Attacks:**
    -   **TCP SYN Flood:** A classic and effective attack aimed at exhausting the server's connection resources.
    -   **UDP Flood:** A high-volume data packet attack designed to saturate the target's network bandwidth.
-   **High Performance:** Capable of sending thousands of concurrent requests or packets thanks to its multi-threading architecture.
