export default function uploadPhoto(filename) {
  const myPromise = new Promise((resolve, reject) => {
    reject(Error(`${filename} cannot be processed`));
  });

  return myPromise;
}
