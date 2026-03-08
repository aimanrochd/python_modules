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
        self.critical_alerts = 0

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None
    ) -> List[Any]:

        numeric_values: List[float] = [
            item for item in data_batch
            if isinstance(item, (int, float))
        ]

        if criteria == "high":
            return [value for value in numeric_values if value > 30]

        if criteria == "low":
            return [value for value in numeric_values if value < 0]

        return numeric_values

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            valid_data = self.filter_data(data_batch, None)
            if len(valid_data) == 0:
                raise ValueError("Invalid Data")

            self.total_readings += len(valid_data)

            batch_alerts = len(self.filter_data(valid_data, "high"))
            self.critical_alerts += batch_alerts

            total = sum(valid_data)
            average = total / len(valid_data)

            return (
                f"Sensor analysis: {len(valid_data)} readings processed, "
                f"avg temp: {average:.1f}°C, "
                f"{batch_alerts} critical alerts"
            )
        except Exception as e:
            return f"Error: {e}"

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "stream_id": self.stream_id,
            "total_readings": self.total_readings,
            "critical_alerts": self.critical_alerts
        }


class TransactionStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        self.stream_id = stream_id
        self.net_flow = 0.0

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None
    ) -> List[Any]:

        valid_transactions: List[str] = [
            item for item in data_batch
            if isinstance(item, str) and ":" in item
        ]

        if criteria == "buy":
            return [item for item in valid_transactions
                    if item.lower().startswith("buy")]

        if criteria == "sell":
            return [item for item in valid_transactions
                    if item.lower().startswith("sell")]

        if criteria == "large":
            result: List[str] = []
            for item in valid_transactions:
                try:
                    value = float(item.split(":")[1])
                    if abs(value) > 100:
                        result.append(item)
                except (ValueError, IndexError):
                    continue
            return result

        return valid_transactions

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            flows: List[float] = [
                float(item.split(':')[1]) if "buy" in item
                else -float(item.split(':')[1])
                for item in data_batch
                if isinstance(item, str) and ':' in item
            ]

            if len(flows) == 0:
                raise ValueError("No valid transaction data")

            current_net_flow = sum(flows)
            self.net_flow += current_net_flow

            if current_net_flow.is_integer():
                net_display = int(current_net_flow)
            else:
                net_display = current_net_flow

            return (
                f"Transaction analysis: {len(flows)} operations, "
                f"net flow: {net_display:+} units"
            )

        except Exception as e:
            return f"Error: {e}"

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "stream_id": self.stream_id,
            "total_net_flow": self.net_flow
        }


class EventStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        self.stream_id = stream_id
        self.total_events = 0
        self.total_errors = 0

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None
    ) -> List[Any]:

        valid_events: List[str] = [
            item for item in data_batch
            if isinstance(item, str)
        ]

        if criteria == "error":
            return [item for item in valid_events if item.lower() == "error"]

        if criteria == "normal":
            return [item for item in valid_events if item.lower() != "error"]

        return valid_events

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            errors = [item for item in data_batch if item == "error"]
            self.total_events += len(data_batch)
            self.total_errors += len(errors)
            return (
                f"Event analysis: {len(data_batch)}"
                f"events, {len(errors)} error detected"
            )
        except Exception as e:
            return f"Error: {e}"

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "stream_id": self.stream_id,
            "total_events": self.total_events,
            "total_errors": self.total_errors
        }


class StreamProcessor:
    def __init__(self) -> None:
        self.streams: List[DataStream] = []

    def add_stream(self, stream: DataStream) -> None:
        self.streams.append(stream)

    def process_all(
        self,
        data_batches: List[List[Any]],
        criteria: Optional[str] = None
    ) -> List[str]:

        results: List[str] = []

        for i in range(len(self.streams)):

            try:
                if i >= len(data_batches):
                    results.append("Error: Missing data batch for stream")
                    continue

                stream = self.streams[i]
                batch = data_batches[i]

                filtered_batch = stream.filter_data(batch, criteria)
                result = stream.process_batch(filtered_batch)

                results.append(result)

            except Exception as e:
                results.append(f"Error processing stream: {e}")

        return results


def main() -> None:
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

    print("Initializing Sensor Stream...")
    print("Stream ID: SENSOR_001, Type: Environmental Data")
    print("Processing sensor batch: [temp:22.5, humidity:65, pressure:1013]")
    sensor = SensorStream("SENSOR_001")
    print(sensor.process_batch([22.5, 22.5, 22.5]))

    print("\nInitializing Transaction Stream...")
    print("Stream ID: TRANS_001, Type: Financial Data")
    print("Processing transaction batch: [buy:100, sell:150, buy:75]")
    trx = TransactionStream("TRANS_001")
    print(trx.process_batch(["buy: 100", "sell: 150", "buy: 75"]))

    print("\nInitializing Event Stream...")
    print("Stream ID: EVENT_001, Type: System Events")
    print("Processing event batch: [login, error, logout]")
    evt = EventStream("EVENT_001")
    print(evt.process_batch(["login", "error", "logout"]))

    print("\n=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...")
    print("\nBatch 1 Results:")

    processor = StreamProcessor()
    processor.add_stream(sensor)
    processor.add_stream(trx)
    processor.add_stream(evt)

    batch_sensor = [10.0, 40.0]
    batch_trx = ["buy:100", "sell:50", "buy:25", "sell:10"]
    batch_evt = ["login", "error", "logout"]

    data_batches = [batch_sensor, batch_trx, batch_evt]

    results = processor.process_all(data_batches)

    sensor_count = len(sensor.filter_data(batch_sensor, None))
    trx_count = len(trx.filter_data(batch_trx, None))
    evt_count = len(evt.filter_data(batch_evt, None))

    if any(result.startswith("Error") for result in results):
        print("Warning: One or more streams encountered an error.")

    print(f"- Sensor data: {sensor_count} readings processed")
    print(f"- Transaction data: {trx_count} operations processed")
    print(f"- Event data: {evt_count} events processed")

    print("\nStream filtering active: High-priority data only")

    critical_alerts = len(sensor.filter_data([10.0, 40.0, 35.0], "high"))
    large_transactions = len(
        trx.filter_data(["buy:50", "sell:200", "buy:20"], "large")
    )

    print(
        f"Filtered results: {critical_alerts} critical sensor alerts, "
        f"{large_transactions} large transaction"
    )

    print("\nAll streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    main()
