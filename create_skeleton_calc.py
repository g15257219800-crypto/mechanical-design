#!/usr/bin/env python3
"""Generate 彩锌多孔板骨架数量计算表."""
from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter

PLATE_WIDTH = 1250
PLATE_LENGTH = 2500

wb = Workbook()
ws = wb.active
ws.title = "骨架数量计算"

thin = Side(style="thin", color="666666")
border = Border(left=thin, right=thin, top=thin, bottom=thin)
header_fill = PatternFill("solid", fgColor="4472C4")
header_font = Font(bold=True, color="FFFFFF", size=11)
title_font = Font(bold=True, size=14)
note_font = Font(size=10, color="444444")
center = Alignment(horizontal="center", vertical="center")
left = Alignment(horizontal="left", vertical="center", wrap_text=True)

ws.merge_cells("A1:F1")
ws["A1"] = "彩锌多孔板 — 单张可制骨架数量"
ws["A1"].font = title_font
ws["A1"].alignment = center

ws.merge_cells("A2:F2")
ws["A2"] = f"板材规格：{PLATE_WIDTH} × {PLATE_LENGTH}（宽 × 长）"
ws["A2"].font = note_font
ws["A2"].alignment = center

ws.merge_cells("A3:F3")
ws["A3"] = "公式：INT(1250÷展长) × INT(2500÷高度) = 骨架数量（只取整，不四舍五入）"
ws["A3"].font = note_font
ws["A3"].alignment = center

headers = ["序号", "展长", "高度", "横向个数\nINT(1250/展长)", "纵向个数\nINT(2500/高度)", "骨架数量"]
for col, h in enumerate(headers, start=1):
    cell = ws.cell(row=5, column=col, value=h.replace("\n", "\n"))
    cell.fill = header_fill
    cell.font = header_font
    cell.border = border
    cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)

# Sample rows + empty rows for user input
sample_data = [
    (200, 500),
    (250, 400),
    (300, 625),
]

start_row = 6
num_rows = 20

for i in range(num_rows):
    row = start_row + i
    ws.cell(row=row, column=1, value=i + 1).alignment = center
    ws.cell(row=row, column=1).border = border

    if i < len(sample_data):
        exp_len, height = sample_data[i]
        ws.cell(row=row, column=2, value=exp_len)
        ws.cell(row=row, column=3, value=height)
    else:
        ws.cell(row=row, column=2, value="")
        ws.cell(row=row, column=3, value="")

    for c in (2, 3):
        ws.cell(row=row, column=c).alignment = center
        ws.cell(row=row, column=c).border = border
        ws.cell(row=row, column=c).number_format = "0"

    # INT division — Excel INT truncates toward zero; positive values = floor
    ws.cell(row=row, column=4, value=f"=IF(B{row}=\"\",\"\",INT({PLATE_WIDTH}/B{row}))")
    ws.cell(row=row, column=5, value=f"=IF(C{row}=\"\",\"\",INT({PLATE_LENGTH}/C{row}))")
    ws.cell(row=row, column=6, value=f"=IF(OR(B{row}=\"\",C{row}=\"\"),\"\",D{row}*E{row})")

    for c in (4, 5, 6):
        ws.cell(row=row, column=c).alignment = center
        ws.cell(row=row, column=c).border = border
        ws.cell(row=row, column=c).number_format = "0"

ws.row_dimensions[5].height = 36
widths = [6, 12, 12, 16, 16, 12]
for i, w in enumerate(widths, start=1):
    ws.column_dimensions[get_column_letter(i)].width = w

out = "/workspace/彩锌多孔板骨架数量计算.xlsx"
wb.save(out)
print(f"Saved: {out}")
