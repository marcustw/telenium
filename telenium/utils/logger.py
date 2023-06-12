import logging

logging.basicConfig(format='%(asctime)s | %(levelname)s: [%(filename)s:%(lineno)d] - %(message)s')
logging.root.setLevel(level=logging.INFO)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("vapeum")
logger.setLevel(logging.INFO)
logging.getLogger('seleniumwire').setLevel(logging.WARNING)