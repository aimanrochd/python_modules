from abc import ABC, abstractmethod
from typing import Any, Dict, List, Union, Optional


class DataProcessor(ABC):

    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class NumericProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        if not isinstance(data, list):
            return isinstance(data, (int, float))
        for item in data:
            if not isinstance(item, (int, float)):
                return False
        return True

    def process(self, data: Any) -> str:
        try:
            if not self.validate(data):
                raise ValueError("Invalid Data!")

            if isinstance(data, (int, float)):
                data = [data]
            stats: Dict[str, Union[int, float]] = {}
            average: Optional[float] = None

            if len(data) == 0:
                stats["total"] = 0
                average = 0.0
            else:
                stats["total"] = sum(data)
                average = sum(data) / len(data)

            stats["average"] = average

            result_str = (
                f"Processed {len(data)} numeric values, "
                f"sum={stats['total']}, avg={stats['average']:.1f}"
            )
            return super().format_output(result_str)

        except Exception as e:
            return f"Error: {e}"


class TextProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        return isinstance(data, str)

    def process(self, data: Any) -> str:
        try:
            if not self.validate(data):
                raise ValueError("Invalid Data")
            total_chars = len(data)
            total_words = len(data.split())
            result_str = (
                f"Processed text: {total_chars} characters, "
                f"{total_words} words"
            )
            return super().format_output(result_str)
        except Exception as e:
            return f"Error: {e}"


class LogProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        if not isinstance(data, str):
            return False
        if ':' not in data:
            return False
        return True

    def process(self, data: Any) -> str:
        try:
            if not self.validate(data):
                raise ValueError("Invalid Data")

            parts: List[str] = data.split(':', 1)
            level = parts[0].strip()
            message = parts[1].strip()

            alert_type = "ALERT" if level == "ERROR" else "INFO"

            result_str = f"[{alert_type}] {level} level detected: {message}"
            return super().format_output(result_str)

        except Exception as e:
            return f"Error: {e}"


def main() -> None:
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")

    print("Initializing Numeric Processor...")
    num_proc = NumericProcessor()
    numeric_data = [1, 2, 3, 4, 5]
    print(f"Processing data: {numeric_data}")
    if num_proc.validate(numeric_data):
        print("Validation: Numeric data verified")
    print(num_proc.process(numeric_data))
    print()

    print("Initializing Text Processor...")
    text_proc = TextProcessor()
    test_data = "Hello Nexus World"
    print(f'Processing data: "{test_data}"')
    if text_proc.validate(test_data):
        print("Validation: Text data verified")
    print(text_proc.process(test_data))
    print()

    print("Initializing Log Processor...")
    log_proc = LogProcessor()
    data3 = "ERROR: Connection timeout"
    print(f'Processing data: "{data3}"')
    if log_proc.validate(data3):
        print("Validation: Log entry verified")
    print(log_proc.process(data3))
    print()

    print("=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface....")

    res1 = NumericProcessor().process([1, 2, 3])
    res2 = TextProcessor().process("Nexus System")
    res3 = LogProcessor().process("INFO: System ready")

    print(res1.replace("Output: ", "Result 1: "))
    print(res2.replace("Output: ", "Result 2: "))
    print(res3.replace("Output: ", "Result 3: "))

    print("\nFoundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    main()
