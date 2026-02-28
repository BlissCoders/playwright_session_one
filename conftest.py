import os
from datetime import datetime

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


def pytest_configure(config):
    # This overrides the .ini setting with a timestamped filename
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # Create directories
    root_dir = config.rootpath
    report_path = os.path.join(root_dir, "reports")
    if not os.path.exists(report_path):
        os.makedirs(report_path, exist_ok=True)

    config.option.htmlpath = f"{report_path}/report_{now}.html"
    config.option.self_contained_html = True