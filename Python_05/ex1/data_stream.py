from typing import Any, List, Dict, Union, Optional
from abc import ABC, abstractmethod


class DataStream(ABC):

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(
    self, data_batch: List[Any], criteria: Optional[str] = None
    ) -> List[Any]:
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
          return {}

class SensorStream(DataStream):
    def __init__(self, stream_id: str) -> None:
          self.stream_id = stream_id
          self.total_readings = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            valid_data: List[float] = [
                item for item in data_batch
                if isinstance(item, (int, float))
            ]
            if len(valid_data) == 0:
                 raise ValueError("Invalid Data")
            self.total_readings += len(valid_data)
            total = sum(valid_data)
            average = total / len(valid_data)
            return f"Sensor analysis: {len(valid_data)} readings processed, avg temp: {average}°C"
        except Exception as e:
             return f"Error: {e}"
    
    def get_stats(self) -> Dict[str, Union[str, int, float]]:
         return {"stream_id": self.stream_id, "total_readings": self.total_readings}
         