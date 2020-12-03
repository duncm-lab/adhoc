$csv = Import-Csv .\tickets_sanitized1.csv
$column_names = $csv | gm -MemberType NoteProperty | select Name

function create-script($col_names){
    $create = "create table table_from_csv "
    $x, $y = $col_names.Name

    do {$create = $create += "$x TEXT, ";
        $x, $y = $y;}
        while ($y -ne $null)
        return $create
}
