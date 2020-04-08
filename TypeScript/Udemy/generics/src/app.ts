// Code goes here!
const names: Array<string> = [];

const promise: Promise<string> = new Promise((resolve) => {
  setTimeout(() => {
    resolve("10");
  }, 2000);
});
promise.then((data) => {
  data.split(" ");
  console.log(data);
});

function merge<T, U>(objA: T, objB: U) {
  return Object.assign(objA, objB);
}
const mergeObj = merge({ name: "Max" }, { age: 30 });
console.log(mergeObj);

interface Lenthy {
  length: number;
}
function countAndDescribe<T extends Lenthy>(element: T): [T, string] {
  let descriptionText = "Got no value.";
  if (element.length === 1) descriptionText = "Got 1 element.";
  else if (element.length > 1)
    descriptionText = `Got ${element.length} elements.`;
  return [element,descriptionText];
}
console.log(countAndDescribe("Hi there!"));
