# logger.py
import logging

def log_operation(expression, result):
    logging.basicConfig(filename='operations.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    log_entry = f"Expression: {expression}, Result: {result}"
    logging.info(log_entry)
    print("Operation logged successfully.")