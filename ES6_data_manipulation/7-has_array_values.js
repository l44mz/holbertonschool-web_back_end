export default function hasValuesFromArray(mySet, myArray) {
  for (const a of myArray) {
    if (!mySet.has(a)) {
      return false;
    }
  }
  return true;
}
