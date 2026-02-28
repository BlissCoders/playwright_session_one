import os

import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture
def playwright_page(request):
    test_name = request.node.name
    root_dir = request.config.rootpath

    video_path = os.path.join(root_dir, "tests-results","videos",str(test_name))
    screenshot_path = os.path.join(root_dir, "tests-results", "screenshots", str(test_name))

    #Create directory only if not present
    if not os.path.exists(video_path):
        os.makedirs(video_path, exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(record_video_dir=video_path)
        page = context.new_page()

        try:
            yield page
        finally:
            page.screenshot(path=f"{screenshot_path}/{test_name}.png")

            # VERY IMPORTANT: close context to finalize video
            context.close()

            # Now it's safe to close browser
            browser.close()