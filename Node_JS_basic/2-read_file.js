const fs = require('fs');

function countStudents(path) {
  let data;
  try {
    data = fs.readFileSync(path, 'utf8');
  } catch (error) {
    throw new Error('Cannot load the database');
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
}

module.exports = countStudents;
