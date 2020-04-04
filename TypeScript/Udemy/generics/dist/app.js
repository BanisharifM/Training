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
//# sourceMappingURL=app.js.map