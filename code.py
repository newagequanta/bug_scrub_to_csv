'''
Git Created, further versioning handled in Git
Version 4:
    1. Two new columns
        a. CDETS URL of the bug
        b. CloudApps URL of the bug
Version 4:
    1. Broken up into 3 functions:
        a. open_text_file - Create a file object
        b. read_text_file - An object generator (read docstring)
        c. create_csv - Create the final CSV
Version 3:
    1. File name is asked for in input
Version 2:
    1. for function going thru list is made more efficient
    2. CSV module used to output to CSV file
'''
import task_borgv3_bug_api as borg_bug

def bug_details(bug_id):
    '''
    INPUT - Bug-ID in string format
    OUTPUT - String containing Integerated-Releases
    '''

    bug_obj = borg_bug.task(None, bug_id, 'details')
    return ', '.join(bug_obj.variables[bug_id]['Integrated-releases'])

def create_csv_from_doc(input_filename, output_filename):
    '''
    INPUT - A text file of the bugscrub, Name of the CSV file
    OUTPUT - A CSV file created in the current directory
    '''
    import csv
    import docx

    #Create a read object by:
        #First calling the open_text_file on input_filename
        #Then callin gthe read_text_file with the above object

    #read_object = read_text_file(open_text_file(input_filename))
    doc = docx.Document(input_filename)

    #Variable to store the previous line, used for logic check later
    #prev_line = ''

    #Variables to store the URL prefixes for CDETS and CloudApps
    #=HYPERLINK is added to ensure a hyperlink appears in CSV and not just test
    url_prefix = ['=HYPERLINK("https://cdetsng.cisco.com/webui/#view=',
                  '=HYPERLINK("https://quickview.cloudapps.cisco.com/quickview/bug/']

    #create the list of lists with Header Only, relevant records added later
    all_records = [['Identifier', 'AS Severity', 'Headline', 'CDETS Link',
                    'CloudApps Link', 'Fixed Releases']]

    for table in doc.tables:
        if 'CSC' in table.cell(0, 1).text:
            #The table object now contains a table with bug details
            current_record = []

            #The CDETS and CloudApps URLs are created with the prefix+Bug-ID
            cdets_url = '{}{}")'.format(url_prefix[0],
                                        table.cell(0, 1).text.replace('\n', ''))
            capps_url = '{}{}")'.format(url_prefix[1],
                                        table.cell(0, 1).text.replace('\n', ''))
            current_record.append(table.cell(0, 1).text.replace('\n', ''))
            current_record.append(table.cell(0, 3).text[13:])
            current_record.append(table.cell(1, 2).text)
            current_record.extend([cdets_url, capps_url])

            #Gather integerated-releases from BORGv3_bug_api
            current_record.append(bug_details(current_record[0]))
            all_records.append(current_record)

    output_file = csv.writer(open(output_filename, 'w'), delimiter=',',
                             quoting=csv.QUOTE_ALL)
    for record in all_records:
        output_file.writerow(record)
