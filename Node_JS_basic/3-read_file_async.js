const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      // Drop empty lines, then drop the header row
      const lines = data.split('\n').filter((line) => line.trim() !== '');
      const students = lines.slice(1);

      console.log(`Number of students: ${students.length}`);

      const fields = {};
      students.forEach((line) => {
        const [firstname, , , field] = line.trim().split(',');
        if (!fields[field]) {
          fields[field] = [];
        }
        fields[field].push(firstname);
      });

      Object.keys(fields).forEach((field) => {
        const list = fields[field].join(', ');
        console.log(`Number of students in ${field}: ${fields[field].length}. List: ${list}`);
      });

      resolve();
    });
  });
}

module.exports = countStudents;
