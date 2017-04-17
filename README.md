# StarCraft-Replay-Analysis
This project is used to process StarCraft replay files and generate the building order automatically.

## How to get started
- Run networkCrawler.py to get game replay files from http://www.teamliquid.net/replay/
- Decode downloaded replay files using open source tool: https://github.com/syhw/bwrepdump
- Run dataSetFilter.py to filter decoded files
- Run parser.py to remove redundant information, which just keeps winners' building order in the first 7 minutes
- Run clustering.py to do data mining over data and generate building order information
