import getListStudentIds from './1-get_list_student_ids';

export default function getStudentIdsSum(getListStudents) {
  const studentIds = getListStudentIds(getListStudents);

  function addIds(id1, idOthers) {
    return id1 + idOthers;
  }

  return studentIds.reduce(addIds);
}
