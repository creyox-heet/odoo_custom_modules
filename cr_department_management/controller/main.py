from odoo import http
from odoo.http import request, content_disposition
import io
import xlsxwriter

class ExcelReportController(http.Controller):
    @http.route("/report/excel_download/<int:department_id>", type="http", auth="user")
    def excel_download(self, department_id):
        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output,{'in_memory': True})
        sheet = workbook.add_worksheet("Department Details")
        department_record = request.env["department.department"].browse(department_id)
        header_style = workbook.add_format({'bold':True,'bg_color':'#4472C4','border':1})

        sheet.write(0,0,"Sequence Code",header_style)
        sheet.set_column(0,0,15)
        sheet.write(1,0,department_record.sequence_code)
        sheet.write(0,1,"Name",header_style)
        sheet.write(1,1,department_record.name)
        sheet.write(0, 2,"Code", header_style)
        sheet.write(1,2,department_record.code)
        sheet.write(0,3,"Number of Students",header_style)
        sheet.write(1,3,department_record.no_of_students)
        sheet.write(0,4,"HOD Id",header_style)
        sheet.write(1,4,department_record.hod_id.name)
        sheet.write(0,5,"Status",header_style)
        if department_record.active:
            sheet.write(1, 5,"True")
        else:
            sheet.write(1, 5,"False")
        sheet.write(0,6,"Staff",header_style)
        sheet.set_column(6,7,25)
        sheet.write(0,7,"Students",header_style)

        row1 =1
        for data in department_record.staff_ids:
            sheet.write(row1, 6,data.name)
            row1 +=1
        row2 = 1
        for data in department_record.student_ids:
            sheet.write(row2, 7,data.name)
            row2 +=1

        workbook.close()
        output.seek(0)

        file_name = f"report_of_{department_record.name}.xlsx"
        return request.make_response(output.getvalue(),
                                     headers=[
                                         ('Content-Type',
                                          'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'),
                                         ('Content-Disposition', content_disposition(file_name))
                                     ]
                                     )
