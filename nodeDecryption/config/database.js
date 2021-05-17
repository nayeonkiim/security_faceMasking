const mysql = require("mysql");
let db_info = {
    host: 'localhost', //실제로 연결할 데이터베이스의 위치
    port: '3306',
    user: 'root',
    password: 'password',
    database: 'imgmac' //데이터베이스 이름
};

module.exports = {
    init: function () {
        return mysql.createConnection(db_info);
    },
    connect: function (conn) {
        conn.connect(function (err) {
            if (err) console.error('mysql connection error : ' + err);
            else console.log('mysql is connected successfully!');
        });
    }
}