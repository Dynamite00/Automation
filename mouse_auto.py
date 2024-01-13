import pyautogui
import time

# 화면 크기 출력
print(pyautogui.size())

# 마우스 위치 출력
time.sleep(2)  # 2초 후의 마우스 위치를 출력
print(pyautogui.position())

# 마우스 이동
pyautogui.moveTo(993, 254, 2)

# 마우스 클릭
pyautogui.click()  # 클릭
pyautogui.click(button='right')  # 오른쪽 마우스 클릭
pyautogui.doubleClick()   # 더블 클릭
pyautogui.click(clicks=3, interval=1)  # 1초마다 3회 클릭


# 마우스 드래그
# 769, 65 -> 905, 66 위치 이동
pyautogui.moveTo(769, 65, 2)
pyautogui.dragTo(905, 66, 2)
