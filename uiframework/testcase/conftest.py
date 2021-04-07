import os
import signal
import subprocess
import time
import allure
import pytest

from uiframework.utils.logger import init_logger, logger


@pytest.fixture(scope="module", autouse=True)
def init():
    # configure logger
    init_logger()

    # Start recording
    command = "scrcpy -Nr ../logs/tmp.mp4"
    p = subprocess.Popen(command, shell=True)
    yield
    os.kill(p.pid, signal.CTRL_C_EVENT)
    with open("../logs/tmp.mp4", "rb") as f:
        allure.attach(f.read(), name="record.mp4", attachment_type=allure.attachment_type.MP4)
