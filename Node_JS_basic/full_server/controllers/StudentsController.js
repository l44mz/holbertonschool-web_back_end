import readDatabase from '../utils';

class StudentsController {
  static getAllStudents(request, response) {
    readDatabase(process.argv[2])
      .then((fields) => {
        const lines = ['This is the list of our students'];
        const names = Object.keys(fields).sort((a, b) => a.toLowerCase().localeCompare(b.toLowerCase()));

        names.forEach((field) => {
          lines.push(`Number of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}`);
        });

        response.status(200).send(lines.join('\n'));
      })
      .catch(() => {
        response.status(500).send('Cannot load the database');
      });
  }

  static getAllStudentsByMajor(request, response) {
    const { major } = request.params;

    if (major !== 'CS' && major !== 'SWE') {
      response.status(500).send('Major parameter must be CS or SWE');
      return;
    }

    readDatabase(process.argv[2])
      .then((fields) => {
        const list = fields[major] || [];
        response.status(200).send(`List: ${list.join(', ')}`);
      })
      .catch(() => {
        response.status(500).send('Cannot load the database');
      });
  }
}

export default StudentsController;
