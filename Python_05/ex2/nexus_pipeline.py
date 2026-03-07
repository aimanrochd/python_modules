from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional, Protocol
import collections


class ProcessingStage(Protocol):
    def process(self, data: Any) -> Any:
        ...


class InputStage:
    def process(self, data: Any) -> Dict[str, Any]:
        try:
            return {
                "raw": data,
                "type": type(data).__name__,
                "stage": "input"
            }
        except Exception as e:
            return {"error": str(e), "stage": "input"}


class TransformStage:
    def process(self, data: Any) -> Dict[str, Any]:
        try:
            if isinstance(data, dict):
                transformed = dict(data)
                transformed["enriched"] = True 
                transformed["stage"] = "transform"
                return transformed
            return {"raw": data, "enriched": False, "stage": "transform"}
        except Exception as e:                                                                                                                                                                                                                                                                                                                                                                                                                                 
            return {"error": str(e), "stage": "transform"}


class OutputStage:
    def process(self, data: Any) -> str:
        try:
            if isinstance(data, dict):
                return f"Processed: {data.get('raw', data)}"
            return f"Output: {str(data)}"
        except Exception as e:
            return f"Output error: {str(e)}"


class ProcessingPipeline(ABC):
    def __init__(self, pipeline_id: str) -> None:
        self.pipeline_id: str = pipeline_id
        self.stages: List[ProcessingStage] = [
            InputStage(), TransformStage(), OutputStage()
        ]

    def add_stage(self, stage: ProcessingStage) -> None:
        self.stages.append(stage)

    @abstractmethod
    def process(self, data: Any) -> Union[str, Any]:
        ...

    def get_stats(self) -> Dict[str, Union[str, int]]:
        return {
            "pipeline_id": self.pipeline_id,
            "stages": len(self.stages)
        }


class JSONAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        super().__init__(pipeline_id)

    def process(self, data: Any) -> Union[str, Any]:
        try:
            import json
            parsed = json.loads(data) if isinstance(data, str) else data
            return f"JSON processed: {parsed}"
        except Exception as e:
            return f"JSON error: {str(e)}"


class CSVAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        super().__init__(pipeline_id)

    def process(self, data: Any) -> Union[str, Any]:
        try:
            if isinstance(data, str):
                lines = data.strip().split("\n")
                headers = lines[0].split(",")
                rows = lines[1:]
                return f"CSV processed: {len(headers)} cols, {len(rows)} rows"
            return f"CSV processed: {str(data)}"
        except Exception as e:
            return f"CSV error: {str(e)}"


class StreamAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        super().__init__(pipeline_id)

    def process(self, data: Any) -> Union[str, Any]:
        try:
            if isinstance(data, list):
                nums = [x for x in data if isinstance(x, (int, float))]
                avg = sum(nums) / len(nums) if nums else 0.0
                return f"Stream processed: {len(nums)} readings, avg: {avg:.1f}"
            return f"Stream processed: {str(data)}"
        except Exception as e:
            return f"Stream error: {str(e)}"


class NexusManager:
    def __init__(self) -> None:
        self.pipelines: List[ProcessingPipeline] = []

    def add_pipeline(self, pipeline: ProcessingPipeline) -> None:
        self.pipelines.append(pipeline)

    def process_data(self, data: Any) -> List[str]:
        results: List[str] = []
        for pipeline in self.pipelines:
            try:
                results.append(pipeline.process(data))
            except Exception as e:
                results.append(f"Error: {str(e)}")
        return results