function systemScripts(e) {
    const long_text = e;
    const hide_text = long_text.nextElementSibling;

    if (long_text.className === "long_text") {
        long_text.style.display = "none";
        long_text.style.fontSize = "0";

        hide_text.style.display = "flex";
        hide_text.style.fontSize = "20px";
    } else if (long_text.className === "long_text__hide") {
        long_text.style.display = "none";
        long_text.style.fontSize = "0";
    }
}


function deleteRow(e) {
    const row = e.closest('tr');
    if (row) {
        row.remove();
        console.log(e)
/*
        const mysql = require('mysql');
        let con = mysql.createConnection({
            host: '{{ database.host }}',
            user: '{{ database.user }}',
            password: '{{ database.password }}',
            database: '{{ database.database }}'
        });

        con.connect((err) => {
            if (err) {
                console.log("Ошибка подключения.", err);
                return;
            }
            con.query('DELETE FROM {{ database.database }} WHERE ${e}')
        })
*/
    }
}