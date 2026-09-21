export default function updateUniqueItems(myMap) {
  const bool = myMap instanceof Map;
  if (!bool) {
    throw new Error('Cannot process');
  }

  for (const [key, value] of myMap) {
    if (value === 1) {
      myMap.set(key, 100);
    }
  }

  return myMap;
}
