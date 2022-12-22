
# Log internet speed and log IP change (dynamic WAN IP) using speedtest.net

## About project

This run python script to check internet speed and IP.
I write this script to monitoring internet speed of my PI node computer.
Because internet in Vietnam is not stable. With this data, I can claim my network provider or change network provider.
If you want to join PI Network, let's go to [minepi.com](https://minepi.com) for more information.
> Use ref code **pcPC9x** to get higher miner rate.

## Howto use

### Method 1:

1. Install python
2. Install speedtest library
```
pip install speedtest
```
3. Download this netspeed.py and run
```
python path/to/netspeed.py
```

### Method 2: More easy (for Windows only)

- Download release package
- Extract zip file
- Goto extract folder
- Make run_speedtest.bat shortcut
- Run this shortcut

![run](/netspeed_run.gif "Run in Windows")

Default interval time is 180 minutes. Change this in run_speedtest.bat file:
```
%0\..\python37\python.exe %0\..\netspeed.py 180
```

### Auto start with Windows

- Copy *run_speedtest.bat - Shortcut.Lnk* file
- Press: Windows + R, type: shell:startup then Enter
- Paste to this. Done

*Tiếng việt*

# Giám sát tốc độ và IP WAN mạng internet

## Hoàn cảnh ra đời

Ở nhà đang có mấy con máy chạy Pi node cần mạng ổn định. Mà mạng internet ở Việt Nam thì các bác biết rồi đấy.
Thấy anh em kêu nào là: buổi tối bóp băng thông, IP tự thay đổi liên tục...
Để tiện theo dõi, so sánh tốc độ, tôi có viết vài dòng lệnh python để kiểm tra.

Lưu ý: Tốc độ mạng khi test bị ảnh hưởng bởi:
- Server test (thuật toán chọn server của speedtest.net)
- Lượng băng thông cho các máy khác cùng mạng LAN

## Hướng dẫn sử dụng

- Tải gói tại trang release (gói đã bao gồm core python và script)
- Giải nén file zip vừa tải
- Mở thư mục vừa giải nén
- Tạo shortcut file run_speedtest.bat
- Chạy shortcut vừa tạo (click đúp chuột)

![run](/netspeed_run.gif "Run in Windows")

Chu kỳ kiểm tra đặt mặc định là 180 phút. Có thể thay đổi thời gian này trong file run_speedtest.bat
Chuột phải vào file *run_speedtest.bat*, chọn Edit
Thay số 180 bằng thời gian tùy chọn. Sau đó lưu file

Nội dung file:
```
%0\..\python37\python.exe %0\..\netspeed.py 180
```
### Tự chạy cùng Windows

- Copy *run_speedtest.bat - Shortcut.Lnk* file (Ctrl + C)
- Nhấn tổ hợp phím: Windows + R, sau đó gõ: ```shell:startup``` rồi nhấn Enter
- Dán vào đó (Ctrl + V)