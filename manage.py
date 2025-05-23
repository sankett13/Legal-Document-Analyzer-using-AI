#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Legal_Doc_Analyzer_usingAI.settings")

    try:
        import django
        django.setup()
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    # Disable autoreload if running as an executable
    if getattr(sys, 'frozen', False) and "runserver" in sys.argv:
        sys.argv.append("--noreload")

    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
