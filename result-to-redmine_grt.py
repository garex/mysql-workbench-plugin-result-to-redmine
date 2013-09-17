from wb import *
import grt
import mforms
import re

ModuleInfo = DefineModule(name= "Exporter", author= "Alexander Ustimenko", version="1.0")

@ModuleInfo.plugin(
    "wb.sqlide.exportToRedmine",
    caption= "Export to Redmine comments",
    input= [wbinputs.currentSQLEditor()],
    pluginMenu= "SQL/Utilities")
@ModuleInfo.export(grt.INT, grt.classes.db_query_Editor)
def exportToRedmine(editor):
    """ Exports current query and it's results to clipboard in Redmine comments format
    """
    
    if editor.activeQueryEditor.activeResultset == None:
        status = "No SQL result for export to redmine!"
        print status
        mforms.App.get().set_status_text(status)
        return 1

    rs = editor.activeQueryEditor.activeResultset

    table = [[]]
    for column in rs.columns:
        table[0].append(_textileHeader(column.name))
    table[0] = _textileRow(table[0])

    hasRows = rs.goToFirstRow()
    while hasRows:
        row = []
        for column in rs.columns:
            row.append(rs.stringFieldValueByName(column.name))
        table.append(_textileRow(row))
        hasRows = rs.nextRow()

    output = '\n' . join(table + [
        '',
        '<pre><code class="sql">',
        rs.sql.strip(),
        '</code></pre>'
    ])
    
    print output
    mforms.Utilities.set_clipboard_text(output)
    sql = re.sub("\s+", " ", rs.sql.strip())
    mforms.App.get().set_status_text("SQL result exported to redmine: " + sql)
    
    return 0

def _textileHeader(cell):
    return '_. ' + cell

def _textileRow(row):
    return '|' . join([''] + row + [''])

# debug
# exportToRedmine(grt.root.wb.sqlEditors[0].queryEditors[0])

