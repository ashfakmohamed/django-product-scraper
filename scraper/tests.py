from unittest.mock import patch

from django.test import TestCase


class RunScraperViewTests(TestCase):
    @patch("scraper.views.scrape_shoes")
    def test_run_scraper_returns_success_without_live_network_call(self, mocked_scraper):
        response = self.client.get("/scraper/scraper_app/")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Scraping completed")
        mocked_scraper.assert_called_once_with()
