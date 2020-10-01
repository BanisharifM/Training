"use strict";
const names = [];
const promise = new Promise((resolve) => {
    setTimeout(() => {
        resolve("10");
    }, 2000);
});
promise.then((data) => {
    data.split(" ");
    console.log(data);
});
function merge(objA, objB) {
    return Object.assign(objA, objB);
}
const mergeObj = merge({ name: "Max" }, { age: 30 });
console.log(mergeObj);
function countAndDescribe(element) {
    let descriptionText = "Got no value.";
    if (element.length === 1)
        descriptionText = "Got 1 element.";
    else if (element.length > 1)
        descriptionText = `Got ${element.length} elements.`;
    return [element, descriptionText];
}
console.log(countAndDescribe("Hi there!"));
function extractAndConvert(obj, key) {
    return "value: " + obj[key];
}
console.log(extractAndConvert({ name: "Max" }, "name"));
class DataStorage {
    constructor() {
        this.data = [];
    }
    addItem(item) {
        this.data.push(item);
    }
    removeItem(item) {
        if (this.data.indexOf(item) === -1) {
            return;
        }
        this.data.splice(this.data.indexOf(item), 1);
    }
    getItem() {
        return [...this.data];
    }
}
const textStorage = new DataStorage();
textStorage.addItem("Ali");
textStorage.addItem("Mahdi");
textStorage.removeItem("Ali");
console.log(textStorage.getItem());
const numberStorage = new DataStorage();
function createCourseGoal(title, description, completeUntil) {
    let courseGoal = {};
    courseGoal.title = title;
    courseGoal.description = description;
    courseGoal.completeUntil = completeUntil;
    return courseGoal;
}
const studentsNames = ["Mahdi", "Ali"];
//# sourceMappingURL=app.js.map