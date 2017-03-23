import random
import time
from typing import Tuple

from selenium.webdriver.common.by import By
from selenium.common import exceptions

from selenium_components import base_page
from selenium_components.youtube import video_wall_page
from selenium_utils import element


class VideoPage(base_page.BasePage):
    """
    Page object for the page where video plays
    """

    BUTTON_SHOW_MORE = (By.CSS_SELECTOR, "#action-panel-details > button.yt-uix-button.yt-uix-button-size-default.yt-uix-button-expander.yt-uix-expander-head.yt-uix-expander-collapsed-body.yt-uix-gen204")
    BUTTON_SHOW_LESS = (By.CSS_SELECTOR, "#action-panel-details > button.yt-uix-button.yt-uix-button-size-default.yt-uix-button-expander.yt-uix-expander-head.yt-uix-expander-body > span")
    BUTTON_SHARE = (By.CSS_SELECTOR, "#watch8-secondary-actions > button > span")
    BUTTON_PLAY = (By.CSS_SELECTOR, "#movie_player > div.ytp-chrome-bottom > div.ytp-chrome-controls > div.ytp-left-controls > button")
    BUTTON_PLAY_NEXT = (By.CSS_SELECTOR, "#movie_player > div.ytp-chrome-bottom > div.ytp-chrome-controls > div.ytp-left-controls > a.ytp-next-button.ytp-button")
    PLAYER_CONTROL_FIELD = (By.CSS_SELECTOR, "#movie_player > div.ytp-chrome-bottom > div.ytp-chrome-controls")
    BUTTON_MORE = (By.CSS_SELECTOR, "#action-panel-overflow-button")
    BUTTON_LIKE = (By.CSS_SELECTOR, "#watch8-sentiment-actions > span > span:nth-child(1) > button")
    BUTTON_DISLIKE = (By.CSS_SELECTOR, "#watch8-sentiment-actions > span > span:nth-child(3) > button")
    PLAYER_AREA = (By.CSS_SELECTOR, "#player-api")
    TOGGLE_AUTOPLAY = (By.ID, "autoplay-checkbox")
    SUGGESTED_VIDEOS = (By.CSS_SELECTOR, "#movie_player > div.html5-endscreen.ytp-player-content.videowall-endscreen.ytp-show-tiles.ytp-endscreen-paginate > div")
    PLAY_TIME = (By.CSS_SELECTOR, "#movie_player > div.ytp-chrome-bottom > div.ytp-chrome-controls > div.ytp-left-controls > div > span.ytp-time-current")
    BUTTON_REMIND_ME_LATER = (By.CSS_SELECTOR, "#ticker-content > div > div.yt-consent-buttons > button.yt-uix-button.yt-uix-button-size-default.yt-uix-button-default.consent-close > span")
    BUTTON_CLOSE_CHOOSE_LANGUAGE_WINDOW = (By.CSS_SELECTOR, "#yt-lang-alert-container > div.yt-alert-buttons > button")
    BUTTON_ALARM_WATCH_WITH_CHROME = (By.CSS_SELECTOR, "#ticker > div.yt-alert-buttons > button")

    def _show_more_or_less(self, locator):
        el = self.driver.find_element(*locator)
        element.scroll_into_view(self.driver, el)
        el.click()

    def show_more(self):
        self._show_more_or_less(self.BUTTON_SHOW_MORE)

    def show_less(self):
        self._show_more_or_less(self.BUTTON_SHOW_LESS)

    def share(self):
        self.driver.find_element(*self.BUTTON_SHARE).click()

    def more(self):
        self.driver.find_element(*self.BUTTON_MORE).click()

    def _like_or_dislike(self, locator: Tuple[By, str]):
        self.driver.find_element(*locator).click()
        el = self.driver.find_element(*self.PLAYER_AREA)
        element.scroll_into_view(self.driver, el)

    def like(self):
        self._like_or_dislike(self.BUTTON_LIKE)

    def dislike(self):
        self._like_or_dislike(self.BUTTON_DISLIKE)

    def toggle_autoplay(self):
        """
        or mobile clients there's no autoplay toggle. Note that we have to wait that all elements load since otherwise
        the toggle goes to the init position back.
        """
        try:
            time.sleep(2)       # if we click too fast the toggle goes into initial position
            self.driver.find_element(*self.TOGGLE_AUTOPLAY).click()
        except exceptions.NoSuchElementException:
            # for some user agents the element isn't present
            pass

    def simulate_user_click_activity(self):
        self.like()
        time.sleep(random.randrange(1, 5))

        self.more()
        time.sleep(random.randrange(1, 5))

        self.share()
        time.sleep(random.randrange(1, 5))

        self.share()
        time.sleep(random.randrange(1, 5))

    def is_video_done_playing(self) -> bool:
        return "Replay" == self.driver.find_element(*self.BUTTON_PLAY).get_attribute("title")

    def wait_until_video_done_playing(self):
        """Wait until the video finishes (provided we turned off autoplay)"""

        while not self.is_video_done_playing():
            time.sleep(5)

            if "0:00" == self.driver.find_element(*self.PLAY_TIME).text:
                break

        return video_wall_page.VideoWallPage(self.driver)

    def ignore_privacy_reminder(self):
        try:
            self.driver.find_element(*self.BUTTON_REMIND_ME_LATER).click()
            time.sleep(0.2)
        except exceptions.NoSuchElementException:
            pass

    def ignore_language_selection(self):
        try:
            time.sleep(0.2)     # needs some time to be detectable as a click
            self.driver.find_element(*self.BUTTON_CLOSE_CHOOSE_LANGUAGE_WINDOW).click()
        except exceptions.NoSuchElementException:
            # for some user agents the element isn't present
            pass

    def ignore_browser_selection(self):
        try:
            time.sleep(0.2)     # needs some time to be detectable as a click
            self.driver.find_element(*self.BUTTON_ALARM_WATCH_WITH_CHROME).click()
        except exceptions.NoSuchElementException:
            # for some user agents the element isn't present
            pass
