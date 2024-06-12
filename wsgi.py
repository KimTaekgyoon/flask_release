import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

from app import app

if __name__ == '__main__':
    logger.info("Starting application...")
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

