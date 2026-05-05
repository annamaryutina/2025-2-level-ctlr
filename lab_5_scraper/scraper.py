"""
Crawler implementation.
"""

# pylint: disable=too-many-arguments, too-many-instance-attributes, unused-import, undefined-variable, unused-argument
import datetime
import json
import pathlib

import requests
from bs4 import BeautifulSoup, Tag

from core_utils.article.article import Article
from core_utils.config_dto import ConfigDTO
from core_utils.constants import CRAWLER_CONFIG_PATH


class IncorrectSeedURLError(Exception):
    'Seed URL does not match standard pattern "https?://(www.)"'
    pass


class NumberOfArticlesOutOfRangeError(Exception):
    "Total number of articles is out of range from 1 to 150"
    pass


class IncorrectNumberOfArticlesError(Exception):
    "Total number of articles to parse is not integer or less than 0"
    pass


class IncorrectHeadersError(Exception):
    "Headers are not in a form of dictionary"
    pass


class IncorrectEncodingError(Exception):
    "Encoding must be specified as a string"
    pass


class IncorrectTimeoutError(Exception):
    "Timeout value must be a positive integer less than 60"
    pass


class IncorrectVerifyError(Exception):
    "Verify certificate value is not boolean."
    pass


class IncorrectHeadlessModeError(Exception):
    "Headless mode value is not boolean."
    pass


class Config:
    """
    Class for unpacking and validating configurations.
    """

    def __init__(self, path_to_config: pathlib.Path) -> None:
        """
        Initialize an instance of the Config class.

        Args:
            path_to_config (pathlib.Path): Path to configuration.
        """
        self.path_to_config = path_to_config

    def _extract_config_content(self) -> ConfigDTO:
        """
        Get config values.

        Returns:
            ConfigDTO: Config values
        """
        with open(self.path_to_config, 'r', encoding='utf-8') as file:
            config_data = json.load(file)

        return ConfigDTO(
            seed_urls=config_data["seed_urls"],
            total_articles_to_find_and_parse=config_data["total_articles_to_find_and_parse"],
            headers=config_data["headers"],
            encoding=config_data["encoding"],
            timeout=config_data["timeout"],
            should_verify_certificate=config_data["should_verify_certificate"],
            headless_mode=config_data["headless_mode"]
        )

    def _validate_config_content(self) -> None:
        """
        Ensure configuration parameters are not corrupt.
        """
        cfg = self._extract_config_content()
        if not cfg.seed_urls or not all(u.startswith(('http://', 'https://')) for u in cfg.seed_urls):
            raise IncorrectSeedURLError()
        if not isinstance(cfg.total_articles_to_find_and_parse, int) or not (1 <= cfg.total_articles_to_find_and_parse <= 150):
            raise NumberOfArticlesOutOfRangeError()
        if not isinstance(cfg.headers, dict):
            raise IncorrectHeadersError()
        if not isinstance(cfg.encoding, str):
            raise IncorrectEncodingError()
        if not isinstance(cfg.timeout, int) or not (1 <= cfg.timeout <= 60):
            raise IncorrectTimeoutError()
        if not isinstance(cfg.should_verify_certificate, bool):
            raise IncorrectVerifyError()
        if not isinstance(cfg.headless_mode, bool):
            raise IncorrectHeadlessModeError()
        return cfg

    def get_seed_urls(self) -> list[str]:
        """
        Retrieve seed urls.

        Returns:
            list[str]: Seed urls
        """
        return self._config.seed_urls

    def get_num_articles(self) -> int:
        """
        Retrieve total number of articles to scrape.

        Returns:
            int: Total number of articles to scrape
        """
        return self._config.total_articles

    def get_headers(self) -> dict[str, str]:
        """
        Retrieve headers to use during requesting.

        Returns:
            dict[str, str]: Headers
        """
        return self._config.headers

    def get_encoding(self) -> str:
        """
        Retrieve encoding to use during parsing.

        Returns:
            str: Encoding
        """
        return self._config.encoding

    def get_timeout(self) -> int:
        """
        Retrieve number of seconds to wait for response.

        Returns:
            int: Number of seconds to wait for response
        """
        return self._config.timeout

    def get_verify_certificate(self) -> bool:
        """
        Retrieve whether to verify certificate.

        Returns:
            bool: Whether to verify certificate or not
        """
        return self._config.should_verify_certificate

    def get_headless_mode(self) -> bool:
        """
        Retrieve whether to use headless mode.

        Returns:
            bool: Whether to use headless mode or not
        """
        return self._config.headless_mode


def make_request(url: str, config: Config) -> requests.models.Response:
    """
    Deliver a response from a request with given configuration.

    Args:
        url (str): Site url
        config (Config): Configuration

    Returns:
        requests.models.Response: A response from a request
    """


class Crawler:
    """
    Crawler implementation.
    """

    #: Url pattern
    url_pattern: re.Pattern | str

    def __init__(self, config: Config) -> None:
        """
        Initialize an instance of the Crawler class.

        Args:
            config (Config): Configuration
        """

    def _extract_url(self, article_bs: Tag) -> str:
        """
        Find and retrieve url from HTML.

        Args:
            article_bs (bs4.Tag): Tag instance

        Returns:
            str: Url from HTML
        """

    def find_articles(self) -> None:
        """
        Find articles.
        """

    def get_search_urls(self) -> list:
        """
        Get seed_urls param.

        Returns:
            list: seed_urls param
        """


# 10
# 4, 6, 8, 10


class HTMLParser:
    """
    HTMLParser implementation.
    """

    def __init__(self, full_url: str, article_id: int, config: Config) -> None:
        """
        Initialize an instance of the HTMLParser class.

        Args:
            full_url (str): Site url
            article_id (int): Article id
            config (Config): Configuration
        """

    def _fill_article_with_text(self, article_soup: BeautifulSoup) -> None:
        """
        Find text of article.

        Args:
            article_soup (bs4.BeautifulSoup): BeautifulSoup instance
        """

    def _fill_article_with_meta_information(self, article_soup: BeautifulSoup) -> None:
        """
        Find meta information of article.

        Args:
            article_soup (bs4.BeautifulSoup): BeautifulSoup instance
        """

    def unify_date_format(self, date_str: str) -> datetime.datetime:
        """
        Unify date format.

        Args:
            date_str (str): Date in text format

        Returns:
            datetime.datetime: Datetime object
        """

    def parse(self) -> Article | bool:
        """
        Parse each article.

        Returns:
            Article | bool: Article instance, False in case of request error
        """


def prepare_environment(base_path: pathlib.Path | str) -> None:
    """
    Create ASSETS_PATH folder if no created and remove existing folder.

    Args:
        base_path (pathlib.Path | str): Path where articles stores
    """


def main() -> None:
    """
    Entrypoint for scraper module.
    """


if __name__ == "__main__":
    main()
