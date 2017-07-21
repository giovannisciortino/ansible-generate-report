#!/usr/bin/python

from ansible.module_utils.basic import *
import sys
import os
import csv
import xlsxwriter
import glob


def main():
    fields = {
        "csv_dir": {"required": True, "type": "str"},
        "output_xlsx_file": {"required": True, "type": "str"},
        "format_header": {"required": True, "type": "bool"},
        # if defined use this csv list as first sheets of the workbook
        "summary_csv_list": {"required": False, "type": "list", "default": []},
    }

    module = AnsibleModule(argument_spec=fields)

    wb = xlsxwriter.Workbook(module.params['output_xlsx_file'])
    format_header = wb.add_format()
    format_header.set_bold()
    format_header.set_bg_color('red')
    format_header.set_font_color('white')

    csv_dir = module.params['csv_dir']
    csv_file_list = sorted(glob.glob(csv_dir + '/*.csv'))

    for summary_filename_csv in reversed(module.params['summary_csv_list']):
        summary_filename = csv_file_list.index(csv_dir + '/' + summary_filename_csv)
        csv_file_list.insert(0, csv_file_list.pop(summary_filename))

    for csv_file_path in csv_file_list:

        sheet_title = os.path.splitext(os.path.basename(csv_file_path))[0][0:31]
        ws = wb.add_worksheet(sheet_title)

        with open(csv_file_path, 'r') as csvfile:
            table = csv.reader(csvfile)
            num_row = 0
            num_cols = 0
            columns_width = []
            for row in table:
                if module.params['format_header'] and num_row == 0:
                    ws.write_row(num_row, 0, row, format_header)
                else:
                    ws.write_row(num_row, 0, row)

                num_row += 1
                num_cols = max(num_cols, len(row))
                columns_width = [max(len(j), columns_width[i] if len(columns_width) > i else 1) for i, j in enumerate(row)]
            # Simulate autofit column
            for i, j in enumerate(columns_width):
                column_name = "%s:%s" % (chr(ord('A') + i), chr(ord('A') + i))
                ws.set_column(column_name, j)

        if module.params['format_header']:
            ws.autofilter(0, 0, num_row-1, num_cols-1)

    wb.close()

    response = {"result": "file %s created" % (module.params['output_xlsx_file'])}
    module.exit_json(changed=False, meta=response)


if __name__ == '__main__':
    main()
