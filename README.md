\# Network Discovery \& Auditing Tool



This is a multi-threaded TCP Port Scanner developed for the Python Programming module assignment at NIBM.



\## Team Members

\-J.P.P.S. Bandara cohndne251f-015 

\-H.P.I.D. Pathirana cohndne251f-016 

\-D.R.D.K. Wickramathunga cohndne251f-031 

\-I. S. Premathilake cohndne251f-006 



\## Features

\- \*\*Fast Scanning:\*\* Uses Python Multi-threading (`ThreadPoolExecutor`) for high-speed port scanning.

\- \*\*Subnet Support:\*\* Supports scanning entire networks using CIDR notation (e.g., 192.168.1.0/24).

\- \*\*Professional CLI:\*\* Clean command-line interface with customizable port ranges and thread counts.

\- \*\*Protocol Support:\*\* Scan both TCP and UDP ports with accurate service detection.

\- \*\*Timeout Control:\*\*  Adjustable connection timeout values for different network conditions.



\## Prerequisites

\- Python 3.10 or higher installed.



\## How to Run

1\. Open your terminal or command prompt.

2\. Navigate to the project directory.

3\. Run the following command:

&#x20;  ```bash

bashpython scanner.py -t 127.0.0.1/32 -p 1-1024 -w 100

