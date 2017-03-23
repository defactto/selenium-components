import time
from typing import List, Union
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from selenium_components import base_page
from selenium_utils import exception


class VideoWallPage(base_page.BasePage):
    """
    After a video is finished playing and if autoplay is turned off, a video wall with thumbnails is offered.
    """
    ENDSCREEN_VIDEOS = (By.CSS_SELECTOR, ".ytp-endscreen-content > a.ytp-suggestion-set")
    THUMBNAIL_TITLE = (By.CSS_SELECTOR, ".ytp-videowall-still-info-content")

    def __init__(self, driver):
        super().__init__(driver)
        self.videos = self._get_videos()

    def _get_videos(self) -> List[WebElement]:
        """
        Gets video thumbnail elements that show up when the video playback finishes and auto play toggle is off.

        Details:
        We wait until the thumnails are loaded.
        """
        for i in range(10):
            videos = self.driver.find_elements(*self.ENDSCREEN_VIDEOS)

            if len(videos) > 0:
                break
            else:
                time.sleep(1)
        else:
            raise exception.ElementNotFound("Thumbnail videos not found.")

        return videos

    def get_and_play_first_in_list(self, urls: list) -> Union[str, None]:
        """
        Plays first video that is found in the list
        :param urls: urls list of urls that we're looking for
        :return: found url or None
        """
        vid_url = None

        for element in self.videos:
            found_url = element.get_attribute("href")

            if found_url in urls:
                vid_url = found_url
                element.click()
                break

        return vid_url
