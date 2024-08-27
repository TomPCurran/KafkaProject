import json

from kafka import KafkaProducer
from kafka.errors import KafkaError
from twelvedata import TDClient
from dotenv import load_dotenv
from utils import market_is_open

import os

load_dotenv()

# API_KEY = os.getenv("TWELVE_DATA_API_KEY")
