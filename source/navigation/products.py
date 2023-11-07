from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get( "https://es.aliexpress.com/w/wholesale-Cuidado-personal.html?spm=a2g0o.categorymp.category.25.2df7yH5LyH5LLB&categoryUrlParams=%7B%22q%22%3A%22Cuidado%20personal%22%2C%22s%22%3A%22qp_nw%22%2C%22osf%22%3A%22categoryNagivateOld%22%2C%22sg_search_params%22%3A%22on___%2528%2520prism_tag_id%253A%25271000486104%2527%2520%2529%22%2C%22guide_trace%22%3A%22c5dd6635-cece-43a9-a5fa-5fa79ebbda7a%22%2C%22scene_id%22%3A%2230630%22%2C%22searchBizScene%22%3A%22openSearch%22%2C%22recog_lang%22%3A%22es%22%2C%22bizScene%22%3A%22categoryNagivateOld%22%2C%22guideModule%22%3A%22unknown%22%2C%22postCatIds%22%3A%2215%2C13%22%2C%22scene%22%3A%22category_navigate%22%7D&isFromCategory=y")
print(driver.title)