from project.worker.tasks import mul
import time
import logging

logger = logging.getLogger(__name__)

while True:
    mul.apply_async((2, 2))
    logger.warn("Dispatched stuff")
    time.sleep(5)