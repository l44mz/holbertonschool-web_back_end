const express = require('express');
const fs = require('fs');

const DB_PATH = process.argv[2];
const PORT = 1245;

function getStudentsReport(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const lines = data.split('\n').filter((line) => line.trim() !== '');
      const students = lines.slice(1);

      const fields = {};
      students.forEach((line) => {
        const [firstname, , , field] = line.trim().split(',');
        if (!fields[field]) {
          fields[field] = [];
        }
        fields[field].push(firstname);
      });

      const report = [`Number of students: ${students.length}`];
      Object.keys(fields).forEach((field) => {
        const list = fields[field].join(', ');
        report.push(`Number of students in ${field}: ${fields[field].length}. List: ${list}`);
      });

      resolve(report.join('\n'));
    });
  });
}

const app = express();

app.get('/', (req, res) => {
  res.type('text/plain');
  res.send('Hello Holberton School!');
});

app.get('/students', (req, res) => {
  res.type('text/plain');
  getStudentsReport(DB_PATH)
    .then((report) => {
      res.send(`This is the list of our students\n${report}`);
    })
    .catch((error) => {
      res.send(`This is the list of our students\n${error.message}`);
    });
});

app.listen(PORT);

module.exports = app;
