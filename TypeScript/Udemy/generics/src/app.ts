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

interface Lengthy {
  length: number;
}
function countAndDescribe<T extends Lengthy>(element: T): [T, string] {
  let descriptionText = "Got no value.";
  if (element.length === 1) descriptionText = "Got 1 element.";
  else if (element.length > 1)
    descriptionText = `Got ${element.length} elements.`;
  return [element,descriptionText];
}
console.log(countAndDescribe("Hi there!"));

function extractAndConvert<T extends object, U extends keyof T>(
  obj: T,
  key: U
) {
  return "value: " + obj[key];
}
console.log(extractAndConvert({ name: "Max" }, "name"));

class DataStorage<T extends string | number | boolean> {
  private data: T[] = [];
  addItem(item: T) {
    this.data.push(item);
  }
  removeItem(item: T) {
    if (this.data.indexOf(item) === -1) {
      return;
    }
    this.data.splice(this.data.indexOf(item), 1);
  }
  getItem() {
    return [...this.data];
  }
}
const textStorage = new DataStorage<string>();
textStorage.addItem("Ali");
textStorage.addItem("Mahdi");
textStorage.removeItem("Ali");
console.log(textStorage.getItem());

const numberStorage = new DataStorage<number>();
//...

// const objectStorage = new DataStorage<object>();
// const maxObject = { name: "Max" };
// objectStorage.addItem(maxObject);
// objectStorage.addItem({ name: "Ali" });
// objectStorage.removeItem(maxObject);
// console.log(objectStorage.getItem());

interface CourseGoal {
  title: string;
  description: string;
  completeUntil: Date;
}
function createCourseGoal(
  title: string,
  description: string,
  completeUntil: Date
): CourseGoal {
  let courseGoal: Partial<CourseGoal> = {};
  courseGoal.title = title;
  courseGoal.description = description;
  courseGoal.completeUntil = completeUntil;
  return courseGoal as CourseGoal;
}

const studentsNames: Readonly<string[]> = ["Mahdi", "Ali"];
// studentsNames.push("Amir");
// studentsNames.pop("Ali");
