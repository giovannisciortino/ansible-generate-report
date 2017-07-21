# README

An Ansible module to generate report in Excel xlsx format.

## Overview

This module allows to create xlsx report from a set of csv files.
It can be useful to save and show data collected by Ansible managed hosts.

## Requirements

- xlswriter Python module ( http://xlsxwriter.readthedocs.io )

## Installation

[TODO] check xlswriter module installation

Clone the ansible-generate-report repository:

    git clone https://github.com/giovannisciortino/ansible-generate-report.git /path/to/ansible-generate-report

Then, you need to tell Ansible where to find the new module.
You can do this by
appending the repository path to the `library` value in your
`~/.ansible.cfg` file. You can find the `library` value under the
`defaults` group. If you do not have a `defaults` group in your
`~/.ansible.cfg` file (or if you do not have a `~/.ansible.cfg` file
at all)
add one. You can find more information about configuring Ansible
[here](http://docs.ansible.com/ansible/intro_configuration.html).

    [defaults]
    library = CURRENT_PATH:/path/to/ansible-generate-report

Alternatively, you can specify the `-M` option when invoking a
playbook. Example:

    $ ansible-playbook -M /path/to/ansible-generate-report my_playbook.yml

Or when running an [ad-hoc
command](http://docs.ansible.com/ansible/intro_adhoc.html). Example:

    $ ansible -m xlswriter \
             -M /path/to/ansible-generate-report/generate-report \
             -a 'csv_dir=/path/csv_dir \
                 output_xls_file=/path/report.xlsx \
                 format_header=True' \
             localhost

## Parameters

     csv_dir:
         description: The directory containing the csv file with csv extension.
                      The xlsx file will contain a sheet for each csv
         type:        string
         required:    true
     output_xlsx_file:
         description: The path of the output xlsx file
         type:        string         
         required:    true
     format_header:
         description: If true the header(the first line of each csv) will be
                      formatted
         type:        boolean         
         required:    true
     summary_csv_list:
         description: List of csv files inserted in the first sheet(s) of the
                      workbook
         required:    false


## Usage

The xlsxwriter module is typically used from an Ansible playbook.

[TODO] Insert an playbook example
    ---

    - hosts: localhost
      tasks:
      - name: ""

Example:

    $ ansible-playbook example.yml

    [TODO] Insert an playbook example output
