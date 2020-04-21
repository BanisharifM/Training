const breakfastPromise = new Promise((resolve, reject) => {
  setTimeout(() => {
    resolve("Your order is ready. Come and get it.");
  }, 3000);
});
console.log(breakfastPromise);
breakfastPromise.then((value) => console.log(value));
