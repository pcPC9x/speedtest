
# Log internet speed and log IP change (dynamic WAN IP) using speedtest.net
# Copyright 2022 pcPC9x
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import speedtest
import os, sys
import datetime as dt
import time

from inspect import getsourcefile
current_path = os.path.abspath(getsourcefile(lambda: 0))
current_dir = os.path.dirname(current_path)
result_dir = os.path.join(current_dir, "RESULT")

LOOP_MINUTE = 3*60

def file_get_lastIP():
    "Get last IP saved from file"
    dir_ = os.path.join(result_dir,'lastIP.txt')
    try:
        with open(dir_, 'r') as f:
            ip = f.read()
    except FileNotFoundError:
        ip = '0.0.0.0'
        with open(dir_, 'w') as f:
            f.write(ip)
    return ip
def file_set_lastIP(ip: 'string', filename='lastIP.txt'):
    "Save IP to file"
    dir_ = os.path.join(result_dir, filename)
    with open(dir_, 'w') as f:
        f.write(ip)
def file_log_IP(ip: 'string', filename='logIP.txt'):
    "Save IP with date time to file"
    dir_ = os.path.join(result_dir, filename)
    text = f'{dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")} :{ip} \n'
    with open(dir_, 'a') as f:
        f.write(text)
def file_log_speed(text: 'string'):
    "Save date time, IP, Download speed, Upload speed to file"
    dt_now = dt.datetime.now()
    dir_ = os.path.join(result_dir,f'logSpeed_{dt_now.year:04}{dt_now.month:02}.txt')
    # Add header of file
    if not os.path.exists(dir_):
        # text = f'DATETIME\tIP\tDOWNLOAD\tUPLOAD\n{text}\n'
        text = f'{"DATETIME":20}\t{"IP":16}\t{"DOWN (Mbps)":11}\t{"UP (Mbps)":11}\n{text}\n'
    else:
        text = f'{text}\n'
    with open(dir_, 'a') as f:
        f.write(text)

if __name__ == "__main__":
    if not os.path.exists(result_dir): os.makedirs(result_dir)
    try:
        # Set LOOP_MINUTE from command prompt argument parameter (optional)
        LOOP_MINUTE = int(sys.argv[1])
    except:
        pass
    file_lastIP = file_get_lastIP()
    print(f'Check each {LOOP_MINUTE} minutes')
    print(f'{"DATETIME":20}\t{"IP":16}\t{"DOWN (Mbps)":11}\t{"UP (Mbps)":11}')
    # Delay for stable Internet connect at startup
    time.sleep(5)
    while (True):    
        try:
            st = speedtest.Speedtest()
            ip = st.config['client']['ip']
            down_speed = st.download() /1000.0 /1000.0
            up_speed = st.upload() /1000.0 /1000.0
        except Exception as e:
            # Internet disconnect
            ip = '0.0.0.0'
            down_speed = 0
            up_speed = 0
            file_log_IP(str(e), 'logError.txt')

        dt_now_str = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # text = '%s\t %s\t %.2fMbit/s\t %.2fMbit/s' %(dt_now_str, ip, down_speed, up_speed)
        text = f'{dt_now_str:20}\t{ip:16}\t{down_speed:8.2f}\t{up_speed:8.2f}'
        print(text)
        # Log speed
        file_log_speed(text)

        # Log IP change
        if file_lastIP != ip:
            file_lastIP = ip
            file_set_lastIP(ip)
            file_log_IP(ip)

        time.sleep(LOOP_MINUTE*60)
