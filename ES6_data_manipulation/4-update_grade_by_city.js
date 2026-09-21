export default function updateStudentGradeByCity(getListStudents, city, newGrades) {
  function filterByCity(obj) {
    if (obj.location === city) return true;
    return false;
  }

  const trueCity = getListStudents.filter(filterByCity);

  function addGrades(obj) {
    const gradeObj = newGrades.find((grade) => grade.studentId === obj.id);
    return { ...obj, grade: gradeObj ? gradeObj.grade : 'N/A' };
  }

  return trueCity.map(addGrades);
}
