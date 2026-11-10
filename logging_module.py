import logging

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(levelname)s - %(message)s"
)

# 1. Logging Levels
print("\n--- Logging Levels ---")
logging.debug("Debug message")
logging.info("Information message")
logging.warning("Warning message")
logging.error("Error message")
logging.critical("Critical message")

# 2. Formatter
print("\n--- Formatter ---")
logger = logging.getLogger("MyLogger")
logger.info("This is a formatted message")

# 3. Logger Hierarchy
print("\n--- Logger Hierarchy ---")
parent = logging.getLogger("shop")
child = logging.getLogger("shop.cart")
parent.info("Shop started")
child.info("Item added to cart")

# 4. Exception Logging
print("\n--- Exception Logging ---")
try:
    result = 10 / 0
except ZeroDivisionError:
    logging.exception("Division error occurred")

# 5. Logging Filter
print("\n--- Logging Filter ---")
class MyFilter(logging.Filter):
    def filter(self, record):
        return "password" not in record.getMessage().lower()

logger.addFilter(MyFilter())
logger.info("User logged in")
logger.info("Password is 1234")

# 6. Lazy Formatting
print("\n--- Lazy Formatting ---")
logging.info("Student %s scored %d marks", "Rahul", 90)

print("\nProgram completed successfully!")