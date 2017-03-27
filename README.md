# Selenium-components: a collection of page objects for common components

## Compatibility
Because of heavy type hinting usage, Python3.5 and above is supported. 

## Examples
```python
from selenium import webdriver

from selenium_components.youtube import video_page


driver = webdriver.Chrome()
driver.get("https://www.youtube.com/watch?v=k_ZPaQUS8W4")

vp = video_page.VideoPage(driver)

# disable autoplay and wait until the video stops playing
vp.toggle_autoplay()
vp.wait_until_video_done_playing()
```
## TODO
+ add docs
+ add tests
+ CI integration
+ add support for [react components](https://github.com/brillout/awesome-react-components)
+ potential support for Python versions under 3.5
