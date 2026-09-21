export default function getStudentsByLocation(getStudentList, city) {
  function filterOut(obj) {
    if (obj.location === city) return true;
    return false;
  }

  return getStudentList.filter(filterOut);
}
