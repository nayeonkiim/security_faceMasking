const express = require('express');
const path = require('path');
const app = express();
const nunjucks = require('nunjucks');
const indexRouter = require('./routes/index');

app.use(express.static(path.join(__dirname, 'public')));

app.set('port', process.env.PORT || 3001);  //3001 포트로 설정 
app.set('view engine', 'html');
nunjucks.configure('views', {
    express: app,
    watch: true,
});

app.use('/', indexRouter);

app.listen(app.get('port'), function () {
    console.log("Express server has started on port" + app.get('port'));
})