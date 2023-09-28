import logging


logging.basicConfig(
    level=logging.WARN,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='app.log'
)

logger = logging.getLogger(__name__)