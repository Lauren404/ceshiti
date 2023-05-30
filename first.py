from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd

edge_driver_path = r'C:\Users\17273\PycharmProjects\pythonProject1\msedgedriver.exe'
driver = webdriver.Edge(executable_path=edge_driver_path)

# 打开目标网页
url = 'https://iftp.chinamoney.com.cn/english/bdInfo/'
driver.get(url)

# 模拟选择下拉菜单中的条件
bond_type = 'Treasury Bond'
issue_year = '2023'

bond_type_element = driver.find_element(By.ID, 'Bond_Type_select')
bond_type_element.send_keys(bond_type)

issue_year_element = driver.find_element(By.ID, 'Issue_Year_select')
issue_year_element.send_keys(issue_year)

search_buttons = driver.find_elements(By.XPATH, '//a[@class="san-btn san-btn-primary"]')
search_buttons[0].click()


# 等待数据加载完成（根据实际情况调整等待时间）
driver.implicitly_wait(60)

# 使用BeautifulSoup解析网页内容
soup = BeautifulSoup(driver.page_source, 'html.parser')

# 找到包含数据的表格元素
table = soup.find('table')

# 解析表格数据并保存为DataFrame
data = []
header = ['ISIN', 'Bond Code', 'Issuer', 'Bond Type', 'Issue Date', 'Latest Rating']
data.append(header)

for row in table.find_all('tr')[1:]:
    columns = row.find_all('td')
    data.append([column.text.strip() for column in columns[:6]])

# 关闭浏览器
driver.quit()

# 将数据保存为CSV文件
df = pd.DataFrame(data[1:], columns=data[0])
df.to_csv('bonds_data.csv', index=False)
