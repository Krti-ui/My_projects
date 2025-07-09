from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

driver = webdriver.Chrome()

url = 'https://www.formula1.com/en/results.html/2024/drivers.html'
driver.get(url)

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "table.f1-table"))
)

rows = driver.find_elements(By.CSS_SELECTOR, "table.f1-table tbody tr")

data = []

for row in rows:
    cols = row.find_elements(By.TAG_NAME, "td")
    if len(cols) >= 5:
        position = cols[0].text.strip()
        driver_name = cols[1].text.strip()
        nationality = cols[2].text.strip()
        team = cols[3].text.strip()
        points = cols[4].text.strip()
        data.append([position, driver_name, nationality, team, points])

df = pd.DataFrame(data, columns=["Position", "Driver", "Nationality", "Team", "Points"])

# Save to CSV
df.to_csv("f1_driver_standings.csv", index=False)
print("Saved to f1_driver_standings.csv")

driver.quit()
