from typing import Any, List, Dict, Union, Optional
from abc import ABC, abstractmethod

class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return f"Output {result}"


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        try:
            var = data / 1
            return True
        except Exception:
            pass
        try:
            check_list = data + [] 
            
            for item in data:
                try:
                    var = item / 1
                except Exception:
                    return False
            return True
        except Exception:
            return False

    def process(self, data: Any) -> str:
        count = 0
        total_sum = 0
        is_list = False
        try:
            check_list = data + []
            is_list = True
        except Exception:
            is_list = False


        if is_list:
            for x in data:
                total_sum += x
                count += 1
        else:
            total_sum = data
            count = 1
        if count == 0:
            average = 0.0
        else:
            average = total_sum / count
            
        return f"Processed {count} numeric values, sum={total_sum}, avg={average}"

    def format_output(self, result: str) -> str:
        return super().format_output(result)


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        try:
            data += ""
            return True
        except Exception:
            return False

    def process(self, data: Any) -> str:
        char_count = 0
        word_count = 0
        in_word = False
        for char in data:
            char_count += 1
            if char == ' ':
                in_word = False
            elif in_word == False:
                word_count += 1
                in_word = True
            
        return f"Processed text: {char_count} characters, {word_count} words"


    def format_output(self, result: str) -> str:
        return super().format_output(result)


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        try:
            check = data + ""
        except Exception:
            return False

        has_colon = False
        for char in data:
            if char == ':':
                has_colon = True
        
        return has_colon

    def process(self, data: Any) -> str:
        colon_index = -1
        
        current_index = 0
        for char in data:
            if char == ':' and colon_index == -1:
                colon_index = current_index
            current_index += 1
            
        if colon_index != -1:
            level = data[:colon_index]
            
            msg_start = colon_index + 1
            
            if msg_start < current_index:
                if data[msg_start] == ' ':
                    msg_start += 1
            
            message = data[msg_start:]
        else:
            level = "UNKNOWN"
            message = data

        return f"[ALERT] {level} level detected: {message}"

    def format_output(self, result: str) -> str:
        return super().format_output(result)
