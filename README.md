# Export query results to Redmine textile comments format

_Mysql Workbench plugin_

## Installing

* Save result-to-redmine_grt.py somewhere
* Go to "Scripting" / "Install Plugin/Module..."
* Find result-to-redmine_grt.py
* Restart Mysql Workbench

## Usage

* Run your query
* Open "Plugins" / "Utilities" / "Export to Redmine comments"
* Paste your results from clipboard!

## Example output

    |_. TABLE_TYPE|_. ENGINE|_. VERSION|_. ROW_FORMAT|
    |BASE TABLE|MyISAM|10|Fixed|
    |BASE TABLE|MyISAM|10|Dynamic|
    |BASE TABLE|CSV|10|Dynamic|

    <pre><code class="sql">
    SELECT DISTINCT TABLE_TYPE, ENGINE, VERSION, ROW_FORMAT
    FROM INFORMATION_SCHEMA.TABLES
    WHERE TABLE_SCHEMA = 'mysql'
    LIMIT 0, 1000
    </code></pre>

