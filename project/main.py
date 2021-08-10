from project.worker.tasks import mul, add
import time
import logging

logger = logging.getLogger(__name__)

while True:
    mul.apply_async((3, 2))
    add.apply_async((3,5))
    logger.warning("Dispatched stuff")
    time.sleep(5)