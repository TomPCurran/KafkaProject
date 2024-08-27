from typing import Optional
import pandas_market_calendars as mcal
import datetime
import pytz  # For handling time zones


def is_market_open() -> Optional[bool]:
    try:
        nyse = mcal.get_calendar("NYSE")
        eastern_tz = pytz.timezone("US/Eastern")
        now = datetime.datetime.now(eastern_tz)

        # Get today's date and time in Eastern Time (NYSE time zone)
        today = now.date()
        current_time = datetime.datetime.combine(
            today, now.time()
        )  # Convert to datetime

        # Check if today is a trading day
        is_trading_day = today in nyse.valid_days(today, today).date

        if is_trading_day:
            # Get market open and close times for today
            market_open = nyse.open_time
            market_close = nyse.close_time

            # Check if current time is within market hours
            is_market_hours = market_open <= current_time.time() <= market_close

            if is_market_hours:
                return True

        return False
    except Exception as e:
        return None


market_is_open = is_market_open()


def create_producer_decorator(func):
    def wrapper(self, *args, **kwargs):
        if not hasattr(self, "_producer"):
            self._producer = func(self, *args, **kwargs)
        return self._producer

    return wrapper
