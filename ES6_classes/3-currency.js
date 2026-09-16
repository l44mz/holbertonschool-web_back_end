export default class Currency {
  constructor(code, name) {
    this._code = code;
    this._name = name;
  }

  get code() {
    return this._code;
  }

  set code(codeInstance) {
    this._code = codeInstance;
  }

  get name() {
    return this._name;
  }

  set name(nameInstance) {
    this._name = nameInstance;
  }

  displayFullCurrency() {
    return `${this._name} (${this._code})`;
  }
}
