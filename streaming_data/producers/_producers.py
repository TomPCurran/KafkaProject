from kafka import KafkaProducer
from utils import create_producer_decorator


class Producer(KafkaProducer):
    def __init__(self, params, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._params = params
        self._topic_name = self._params.get("topic_name")
        self._producer_address = self._params.get("producer_address")

    @create_producer_decorator
    def _create_producer(self):
        return KafkaProducer(bootstrap_servers=[self._producer_address])
