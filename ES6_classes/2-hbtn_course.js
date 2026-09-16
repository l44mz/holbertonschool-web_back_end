export default class HolbertonCourse {
  constructor(name, length, students) {
    this.name = name;
    this.length = length;
    this.students = students;
  }

  get name() {
    return this._name;
  }

  set name(nameInstance) {
    if (typeof nameInstance !== 'string') {
      throw new TypeError('Name must be a string');
    }
    this._name = nameInstance;
  }

  get length() {
    return this._length;
  }

  set length(lenghtInstance) {
    if (typeof lenghtInstance !== 'number') {
      throw new TypeError('Length must be a number');
    }
    this._length = lenghtInstance;
  }

  get students() {
    return this._students;
  }

  set students(studentInstance) {
    if (!Array.isArray(studentInstance) || !studentInstance.every((student) => typeof student === 'string')) {
      throw new TypeError('Students must be an array of strings');
    }
    this._students = studentInstance;
  }
}
