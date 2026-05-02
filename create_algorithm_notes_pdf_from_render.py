from pathlib import Path

from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader


ROOT = Path(r"C:\Users\Rahul Yadav\OneDrive\Desktop\123")
RENDER_DIR = ROOT / "algorithm_notes_render_v2"
OUT = ROOT / "Algorithm_Design_Analysis_35_Page_Notes_Rahul_Yadav.pdf"


def page_number(path: Path) -> int:
    return int(path.stem.split("-")[1])


pages = sorted(RENDER_DIR.glob("page-*.png"), key=page_number)
if len(pages) != 35:
    raise SystemExit(f"Expected 35 rendered pages, got {len(pages)}")

first = Image.open(pages[0])
width_px, height_px = first.size
pdf = canvas.Canvas(str(OUT), pagesize=(width_px, height_px))

for page in pages:
    with Image.open(page) as img:
        pdf.setPageSize(img.size)
        pdf.drawImage(ImageReader(img.convert("RGB")), 0, 0, width=img.width, height=img.height)
        pdf.showPage()

pdf.save()
print(OUT)
