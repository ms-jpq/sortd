from .main import main

try:
    exit(main())
except KeyboardInterrupt:
    exit(130)
except BrokenPipeError:
    exit(13)

