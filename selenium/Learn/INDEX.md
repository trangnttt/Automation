https://www.youtube.com/playlist?list=PLL34mf651faPOf5PE5YjYgTRITzVzzvMz

*** Selenium là 1 bộ công cụ kiểm thử tự động open source ***
- Kết hợp Webdriver Manager của Python để Chạy selenium trên chrome:
B1: from selenium import webdriver
B2: 
B3: Xem Run_TC_Basic.py

*** 1. Find Element ***
- from selenium.webdriver.common.by import By
- Find ID Element
- Find Name Element
- Find Xpath xem https://viettuts.vn/selenium/xpath-trong-selenium-webdriver#goto-h3-2
- Find CSS Selector
- Find Link Text or Partial Link Text
- Find Tag Name or Class Name
=> Find_Element.py
* => .send_keys("__") nhập value vào input

- Find List: => Find_Element_List.py

*** 2. Các lệnh trình duyệt (Browser Commands) *** 
=> Browser_Commands.py

*** 3. Get text Element && Get Attribute Value ***
=> Find_Element_Text.py

*** 4. Check if Element is Enabled ***
- Dùng is_enabled()
=> Element_State.py

*** 5. Handle Hidden Elements (xử lý các elm ẩn) ***
- Dùng is_displayed()
=> Hidden_Elements.py

*** 6. Handle Checkbox ***
=> Handle_Checkbox.py (để xem lại không dùng is_selected() được phải dùng is_displayed())
Nghiên cứu thử Is_selected.py

*** 7. Radio Buttons ***
=> Handle_Checkbox.py (để xem lại không dùng is_selected() được phải dùng is_displayed())

*** 8. Handle Dropdown *** 
- from selenium.webdriver.support.select import Select
=> Handle_Dropdown.py

*** 9. Handle Multiselect List/Dropdown *** 
=> Multiselect_List_Dropdown.py

*** 10. Handle Auto Suggestion ***
- from selenium.webdriver.common.keys import Keys
=> Auto_Suggestion.py

*** 11. Handle Calendar *** 
=> Auto_Suggestion.py

*** 12. Capture Screenshot ***
- from PIL import Image
=> Capture_Screenshot.py

*** 13. Execute JavaScript ***
=> Execute_JavaScript.py

*** 14. Handle Multiple Windows ***
=> Handle_Multiple_Windows.py

*** 15. Handle Frames ***
=> Handle_Frames.py

*** 16. Handle Alerts ***
- from selenium.webdriver.common.alert import Alert 
=> Handle_Alerts.py

*** 17. Handle Mouse Hover ***
- from selenium.webdriver.common.action_chains import ActionChains
=> Handle_Mouse_Hover.py

*** 18. Perform Right Click & Double Click ***
- from selenium.webdriver.common.action_chains import ActionChains
=> Right_Click_Double_Click.py

*** 19. Handle Sliders ***
- from selenium.webdriver.common.action_chains import ActionChains
=> Handle_Sliders.py

*** 20. Drag and Drop ***
- from selenium.webdriver.common.action_chains import ActionChains
=> Drag_Drop.py

*** 21. Implicit Wait, Fluent Wait, Explicit Wait  ***
=> Implicit_Wait.py (xem thêm trên mạng nếu cần)

# wait commands
- time.sleep(time)  
    * Ưu điểm: 
        + Dễ sử dụng
        + Chỉ cần gọi hàm time.sleep() với tham số là thời gian muốn tạm dừng, chương trình sẽ tự động tạm dừng trong khoảng thời gian đó.
    * Nhược điểm: 
        + Hiệu suất của chương trình rất kém
        + Khi sử dụng hàm time.sleep(), chương trình sẽ không thực hiện bất kỳ tác vụ nào trong khoảng thời gian được đề cập. Điều này có thể làm giảm hiệu suất của chương trình.
        + Khi sử dụng hàm time.sleep(), chương trình sẽ không kiểm tra xem phần tử có sẵn hay không. Nếu phần tử không có sẵn trong khoảng thời gian được đề cập, chương trình sẽ gặp lỗi ngoại lệ.

- Implicit Wait
    * Ưu điểm:
        + Sử dụng đơn giản: Chỉ cần sử dụng một câu lệnh driver.implicitly_wait(time) để thiết lập thời gian chờ ngầm định cho trình duyệt.
        + Hiệu suất không bị giảm: Ngược lại với time.sleep(), implicit wait sẽ không khiến chương trình tạm dừng hoàn toàn trong khoảng thời gian chờ đợi. Thay vào đó, trình duyệt sẽ tiếp tục thực thi các lệnh khác trong khi chờ phần tử mong muốn xuất hiện. Điều này giúp cải thiện hiệu suất của chương trình, đặc biệt là khi có nhiều phần tử cần chờ đợi.
    * Nhược điểm: 
        + Có thể gây ra ngoại lệ: Nếu phần tử không có sẵn trong khoảng thời gian được đề cập, trình duyệt sẽ tiếp tục thực thi các lệnh tiếp theo mà không kiểm tra trạng thái của phần tử. Điều này có thể dẫn đến lỗi ngoại lệ nếu phần tử không tồn tại hoặc chưa được tải đầy đủ.

- Explicit Wait
    Explicit Wait works based on condition ...
    * Ưu điểm: 
        + Hiệu quả hơn: Explicit wait cho phép bạn kiểm tra trạng thái của phần tử hoặc của trang web theo các điều kiện cụ thể. Điều này giúp bạn tránh được tình trạng lỗi ngoại lệ do phần tử không có sẵn hoặc không đạt được trạng thái mong muốn.
    * Nhược điểm: 
        + Phải sử dụng ở nhiều nơi: Explicit wait cần phải được sử dụng ở nhiều nơi trong mã của bạn, mỗi nơi tương ứng với một điều kiện chờ đợi. Điều này có thể khiến mã của bạn trở nên cồng kềnh và khó hiểu.
        + Khó sử dụng: Explicit wait có thể khó sử dụng nếu bạn không quen với các điều kiện chờ đợi của Selenium.