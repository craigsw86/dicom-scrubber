# test_imports.py
# This script tests that all required packages are installed correctly.

print("Testing package imports...")

# Test everything being imported by the application

try:
    import annotated_doc
    print("annotated_doc imported successfully")
except ImportError as e:
    print("annotated_doc failed:", e)

try:
    import annotated_types
    print("annotated_types imported successfully")
except ImportError as e:
    print("annotated_types failed:", e)

try:
    import anyio
    print("anyio imported successfully")
except ImportError as e:
    print("anyio failed:", e)

try:
    import colorama
    print("colorama imported successfully")
except ImportError as e:
    print("colorama failed:", e)

try:
    import fastapi
    print("fastapi imported successfully")
except ImportError as e:
    print("fastapi failed:", e)

try:
    import idna
    print("idna imported successfully")
except ImportError as e:
    print("idna failed:", e)

try:
    import cv2
    print("cv2 imported successfully")
except ImportError as e:
    print("cv2 failed:", e)

try:
    import numpy
    print("numpy imported successfully")
except ImportError as e:
    print("numpy failed:", e)

try:
    import packaging
    print("packaging imported successfully")
except ImportError as e:
    print("packaging failed:", e)

try:
    import PIL
    print("PIL imported successfully")
except ImportError as e:
    print("PIL failed:", e)
                  
try:
    import pydantic
    print("pydantic imported successfully")
except ImportError as e:
    print("pydantic failed:", e)

try:
    import pydantic_core
    print("pydantic_core imported successfully")
except ImportError as e:
    print("pydantic_core failed:", e)

try:
    import pydicom
    print("pydicom imported successfully")
except ImportError as e:
    print("pydicom failed:", e)

try:
    from PySide6.QtWidgets import QApplication
    print("PySide6 imported successfully")
except ImportError as e:
    print("PySide6 failed:", e)

try:
    import PySide6_Addons
    print("PySide6_Addons imported successfully")
except ImportError as e:
    print("PySide6_Addons failed:", e)

try:
    import PySide6_Essentials
    print("PySide6_Essentials imported successfully")
except ImportError as e:
    print("PySide6_Essentials failed:", e)

try:
    import pytesseract
    print("pytesseract imported successfully")
except ImportError as e:
    print("pytesseract failed:", e)

try:
    import shiboken6
    print("shiboken6 imported successfully")
except ImportError as e:
    print("shiboken6 failed:", e)

try:
    import starlette
    print("starlette imported successfully")
except ImportError as e:
    print("starlette failed:", e)

try:
    import tqdm
    print("tqdm imported successfully")
except ImportError as e:
    print("tqdm failed:", e)

try:
    import typing_inspection
    print("typing_inspection imported successfully")
except ImportError as e:
    print("typing_inspection failed:", e)

try:
    import typing_extensions
    print("typing_extensions imported successfully")
except ImportError as e:
    print("typing_extensions failed:", e)

try:
    import unicorn
    print("unicorn imported successfully")
except ImportError as e:
    print("unicorn failed:", e)
