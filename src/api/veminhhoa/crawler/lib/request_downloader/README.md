# Giới thiệu 
Thư viện request_downloader dùng để đơn giản hoá việc sử dụng browser kết hợp với tor service để download html request

# Tính năng chính
1. Thống nhất giao diện sử dụng của browser downloader lẫn request downloader  
2. Tích hợp sẵn tor proxy 
3. Đơn giản hoá việc cài đặt firefox + selenium driver / puppeter  
4. Tích hợp cơ chế load profile để crawl những trang cần login / cần chạy addon 
5. Tự động quản lý các driver, xử lý vấn đề driver bị block / crash / memory leak 

# Cài đặt 
### Bước 1: Clone và cài đặt thư viện 
Chạy file install.sh để cài đặt driver và các thư viện cần thiết cho Python

### Bước 2: Cài đặt Tor và cấu hình End Node ở Việt Nam 
~~~ 
sudo apt install tor  
~~~ 

Sau đó thêm dòng sau vào trong file /etc/tor/torrc để chuyển exit node tại Việt Nam  

~~~
ExitNodes {vn}
StrictNodes 1
~~~ 

# Test 
~~~
python3 -m pytest tests/
~~~

# Những vấn đề đã phát hiện 
1. BrowserDownloader không thể sử dụng cùng lúc tor proxy và adblock extension
Nếu sử dụng kết hợp này thì không load được dữ liệu cuả trang 
