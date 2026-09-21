export default function getListStudentIds(arr) {
  const boolean = Array.isArray(arr);

  if (!boolean) {
    return [];
  }

  function getId(obj) {
    return obj.id;
  }

  return arr.map(getId);
}
