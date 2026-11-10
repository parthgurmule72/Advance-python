import logging
import logging.config

def demo_levels():
    print("\n=== 1. LOGGING LEVELS ===")

    log = logging.getLogger("levels")
    log.handlers.clear()
    log.setLevel(logging.DEBUG)
    log.propagate = False

    h = logging.StreamHandler()
    h.setFormatter(logging.Formatter("%(levelname)s - %(message)s"))
    log.addHandler(h)

    log.debug("Debug information")
    log.info("Normal information")
    log.warning("Warning message")
    log.error("Error message")
    log.critical("Critical message")

    log.setLevel(logging.WARNING)
    log.warning("Visible warning message")

def demo_formatter():
    print("\n=== 2. FORMATTER ===")

    log = logging.getLogger("format")
    log.handlers.clear()
    log.setLevel(logging.INFO)
    log.propagate = False

    h = logging.StreamHandler()
    h.setFormatter(logging.Formatter(
        "%(asctime)s | %(name)s | %(levelname)s | %(message)s"
    ))
    log.addHandler(h)

    log.info("Formatted log message")

def demo_hierarchy():
    print("\n=== 3. LOGGER HIERARCHY ===")

    parent = logging.getLogger("shop")
    parent.handlers.clear()
    parent.setLevel(logging.INFO)
    parent.propagate = False

    h = logging.StreamHandler()
    h.setFormatter(logging.Formatter("[%(name)s] %(message)s"))
    parent.addHandler(h)

    logging.getLogger("shop.cart").info("Item added to cart")
    logging.getLogger("shop.pay").info("Payment accepted")

def demo_exception():
    print("\n=== 4. EXCEPTION LOGGING ===")

    log = logging.getLogger("errors")
    log.handlers.clear()
    log.setLevel(logging.ERROR)
    log.propagate = False

    h = logging.StreamHandler()
    log.addHandler(h)

    try:
        10 / 0
    except ZeroDivisionError:
        log.exception("Division failed")

class HideSecrets(logging.Filter):
    def filter(self, record):
        return "password" not in record.getMessage().lower()

def demo_filter():
    print("\n=== 5. LOGGING FILTER ===")

    log = logging.getLogger("secure")
    log.handlers.clear()
    log.setLevel(logging.INFO)
    log.propagate = False

    h = logging.StreamHandler()
    h.addFilter(HideSecrets())
    h.setFormatter(logging.Formatter("%(levelname)s - %(message)s"))
    log.addHandler(h)

    log.info("User logged in")
    log.info("Password is 1234")
    log.info("Dashboard opened")

def demo_lazy():
    print("\n=== 6. LAZY FORMATTING ===")

    log = logging.getLogger("extras")
    log.handlers.clear()
    log.setLevel(logging.INFO)
    log.propagate = False

    h = logging.StreamHandler()
    h.setFormatter(logging.Formatter(
        "%(levelname)s user=%(user)s %(message)s"
    ))
    log.addHandler(h)

    log.info(
        "Order %d placed, total Rs. %.2f",
        42, 1999.50,
        extra={"user": "rahul"}
    )

def demo_dictconfig():
    print("\n=== 7. DICTCONFIG ===")

    config = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "short": {
                "format": "%(levelname)s:%(name)s:%(message)s"
            }
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "formatter": "short",
                "level": "INFO"
            }
        },
        "loggers": {
            "configured": {
                "handlers": ["console"],
                "level": "INFO",
                "propagate": False
            }
        }
    }

    logging.config.dictConfig(config)
    logging.getLogger("configured").info("Configured using dictionary")

if __name__ == "__main__":
    print("PYTHON LOGGING MODULE DEMONSTRATION")

    demo_levels()
    demo_formatter()
    demo_hierarchy()
    demo_exception()
    demo_filter()
    demo_lazy()
    demo_dictconfig()

    print("\nAll logging demonstrations completed.")