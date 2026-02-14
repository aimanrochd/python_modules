from stream_processor import NumericProcessor, TextProcessor, LogProcessor

def main():
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")
    
    numeric_proc = NumericProcessor()
    text_proc = TextProcessor()
    log_proc = LogProcessor()

    numeric_data = [1, 2, 3, 4, 5]
    text_data = "Hello Nexus World"
    log_data = "ERROR: Connection timeout"

    print("\nInitializing Numeric Processor...")
    print(f"Processing data: {numeric_data}")
    if numeric_proc.validate(numeric_data):
        print("Validation: Numeric data verified")
        result = numeric_proc.process(numeric_data)
        print(f"Output: {result}")
    else:
        print("Validation: Failed")

    print("\nInitializing Text Processor...")
    print(f"Processing data: \"{text_data}\"")
    if text_proc.validate(text_data):
        print("Validation: Text data verified")
        result = text_proc.process(text_data)
        print(f"Output: {result}")
    else:
        print("Validation: Failed")

    print("\nInitializing Log Processor...")
    print(f"Processing data: \"{log_data}\"")
    if log_proc.validate(log_data):
        print("Validation: Log entry verified")
        result = log_proc.process(log_data)
        print(f"Output: {result}")
    else:
        print("Validation: Failed")

    print("\n=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface....")
    
    processors = [
        (numeric_proc, [1.5, 2.5, 2.0]),
        (text_proc, "Polymorphism is cool"),
        (log_proc, "INFO: System ready")
    ]

    i = 1
    for processor, data in processors:
        if processor.validate(data):
            result = processor.process(data)
            formatted = processor.format_output(result) 
            print(f"Result {i}: {result}")
        else:
            print(f"Result {i}: Validation Failed")
        i += 1

    print("\nFoundation systems online. Nexus ready for advanced streams.")

if __name__ == "__main__":
    main()